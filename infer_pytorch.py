#!/usr/bin/env python3
"""
Gipformer PyTorch Inference - Vietnamese ASR
Uses icefall/k2 for native PyTorch speech recognition.

Usage:
    python infer_pytorch.py --audio data/audio1.wav
    python infer_pytorch.py --audio data/audio1.wav --device cuda
    python infer_pytorch.py --audio file1.wav file2.wav
    python infer_pytorch.py --audio data/audio1.wav --decoding-method modified_beam_search
"""

import argparse
import importlib.abc
import importlib.util
import math
import os
import subprocess
import sys
import time
import types
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)
os.environ.setdefault("GIT_PYTHON_REFRESH", "quiet")
os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")

try:
    from huggingface_hub import hf_hub_download
except ImportError:
    print("Error: huggingface_hub is not installed.")
    print("Install it with: pip install huggingface_hub")
    sys.exit(1)

REPO_ID = "g-group-ai-lab/gipformer-65M-rnnt"
ICEFALL_REPO = "https://github.com/k2-fsa/icefall.git"
SAMPLE_RATE = 16000
DEFAULT_ICEFALL_DIR = Path.home() / ".cache" / "gipformer" / "icefall"

PT_FILES = {
    "checkpoint": "epoch-35-avg-6.pt",
    "bpe_model": "bpe.model",
    "tokens": "tokens.txt",
}


# ── Lhotse mock (only used for training, not inference) ──────────────────────


class _MockModule(types.ModuleType):
    """Returns a dummy class for any attribute access."""

    class _Dummy:
        def __init__(self, *a, **kw):
            pass

        def __call__(self, *a, **kw):
            return self

        def __getattr__(self, name):
            return type(self)()

    def __getattr__(self, name):
        return self._Dummy


class _LhotseFinder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    """Import hook that provides mock lhotse modules.

    lhotse is a training-only dependency; inference never touches it. Rather
    than require the heavy package, we satisfy icefall's `import lhotse...`
    with dummy modules.

    Uses the find_spec / exec_module protocol — the legacy find_module /
    load_module API was removed in Python 3.12.
    """

    def find_spec(self, fullname, path=None, target=None):
        if fullname == "lhotse" or fullname.startswith("lhotse."):
            return importlib.util.spec_from_loader(fullname, self, is_package=True)
        return None

    def create_module(self, spec):
        mod = _MockModule(spec.name)
        mod.__path__ = []
        mod.__file__ = "<mocked>"
        mod.__version__ = "0.0.0"
        return mod

    def exec_module(self, module):
        pass


# ── Setup ────────────────────────────────────────────────────────────────────


def setup_icefall(icefall_dir: Path) -> None:
    """Clone icefall (sparse + shallow) if needed and configure sys.path."""
    marker = icefall_dir / "icefall" / "__init__.py"
    if not marker.exists():
        print("Setting up icefall (one-time download)...")
        icefall_dir.parent.mkdir(parents=True, exist_ok=True)
        if icefall_dir.exists():
            import shutil

            shutil.rmtree(icefall_dir)

        subprocess.run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "--filter=blob:none",
                "--sparse",
                ICEFALL_REPO,
                str(icefall_dir),
            ],
            check=True,
        )
        subprocess.run(
            ["git", "sparse-checkout", "set", "icefall", "egs/librispeech/ASR"],
            cwd=str(icefall_dir),
            check=True,
        )
        print("Icefall setup complete.")

    # Mock lhotse before any icefall imports
    sys.meta_path.insert(0, _LhotseFinder())

    # Add icefall to sys.path
    for p in [
        str(icefall_dir),
        str(icefall_dir / "egs" / "librispeech" / "ASR"),
        str(icefall_dir / "egs" / "librispeech" / "ASR" / "zipformer"),
    ]:
        if p not in sys.path:
            sys.path.insert(0, p)


def download_model() -> dict:
    """Download PyTorch model files from HuggingFace."""
    print(f"Downloading model from {REPO_ID}...")
    paths = {}
    for key, filename in PT_FILES.items():
        paths[key] = hf_hub_download(repo_id=REPO_ID, filename=filename)
    print("Model downloaded successfully.")
    return paths


# ── Main ─────────────────────────────────────────────────────────────────────


def main():
    # Pre-parse to get icefall directory before importing icefall modules
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument(
        "--icefall-dir", type=str, default=str(DEFAULT_ICEFALL_DIR)
    )
    pre_args, _ = pre_parser.parse_known_args()

    setup_icefall(Path(pre_args.icefall_dir))

    # Deferred imports (require icefall in sys.path)
    import k2
    import kaldifeat
    import sentencepiece as spm
    import torch
    import torchaudio
    from beam_search import greedy_search_batch, modified_beam_search
    from torch.nn.utils.rnn import pad_sequence
    from train import add_model_arguments, get_model, get_params

    # Full argument parser
    parser = argparse.ArgumentParser(
        description="Gipformer PyTorch Inference - Vietnamese ASR",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
        "  python infer_pytorch.py --audio data/audio1.wav\n"
        "  python infer_pytorch.py --audio data/audio1.wav --device cuda\n"
        "  python infer_pytorch.py --audio f1.wav f2.wav\n",
    )
    parser.add_argument(
        "--audio",
        type=str,
        nargs="+",
        required=True,
        help="Path(s) to audio file(s) to transcribe",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="auto",
        help="Device: cpu, cuda, cuda:N, or auto (default: auto)",
    )
    parser.add_argument(
        "--decoding-method",
        type=str,
        choices=["greedy_search", "modified_beam_search"],
        default="modified_beam_search",
        help="Decoding method (default: modified_beam_search)",
    )
    parser.add_argument(
        "--beam-size",
        type=int,
        default=4,
        help="Beam size for modified_beam_search (default: 4)",
    )
    parser.add_argument(
        "--context-size",
        type=int,
        default=2,
        help="Decoder context size (default: 2)",
    )
    parser.add_argument(
        "--icefall-dir",
        type=str,
        default=str(DEFAULT_ICEFALL_DIR),
        help="Path to icefall clone (default: ~/.cache/gipformer/icefall)",
    )

    add_model_arguments(parser)
    args = parser.parse_args()

    # Build params (temporarily point GIT_DIR to icefall to avoid git warnings)
    old_git_dir = os.environ.get("GIT_DIR")
    os.environ["GIT_DIR"] = str(Path(pre_args.icefall_dir) / ".git")
    params = get_params()
    if old_git_dir is None:
        os.environ.pop("GIT_DIR", None)
    else:
        os.environ["GIT_DIR"] = old_git_dir
    params.update(vars(args))

    # Download model files
    model_paths = download_model()

    # Token table (for blank_id and vocab_size)
    token_table = k2.SymbolTable.from_file(model_paths["tokens"])
    params.blank_id = token_table["<blk>"]
    params.unk_id = token_table["<unk>"]

    # Count tokens excluding disambiguation symbols
    num_tokens = 0
    for s in token_table.symbols:
        if not s.startswith("#"):
            num_tokens += 1
    # Exclude token ID 0 (blank) from count
    if token_table["<blk>"] == 0:
        num_tokens -= 1
    params.vocab_size = num_tokens + 1

    # Device
    if args.device == "auto":
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
        device = torch.device(args.device)
    print(f"Using device: {device}")

    # Build and load model
    model = get_model(params)

    checkpoint = torch.load(
        model_paths["checkpoint"], map_location="cpu", weights_only=False
    )
    if isinstance(checkpoint, dict) and "model" in checkpoint:
        model.load_state_dict(checkpoint["model"], strict=False)
    else:
        model.load_state_dict(checkpoint, strict=False)

    model.to(device)
    model.eval()

    print(f"Model parameters: {sum(p.numel() for p in model.parameters()):,}")

    # Sentencepiece for text decoding
    sp = spm.SentencePieceProcessor()
    sp.load(model_paths["bpe_model"])

    # Feature extractor
    opts = kaldifeat.FbankOptions()
    opts.device = device
    opts.frame_opts.dither = 0
    opts.frame_opts.snip_edges = False
    opts.frame_opts.samp_freq = SAMPLE_RATE
    opts.mel_opts.num_bins = 80
    opts.mel_opts.high_freq = -400
    fbank = kaldifeat.Fbank(opts)

    # Transcribe each audio file
    with torch.no_grad():
        for audio_path in args.audio:
            start = time.time()

            # Load audio, resample if needed
            wave, sr = torchaudio.load(audio_path)
            if sr != SAMPLE_RATE:
                wave = torchaudio.functional.resample(wave, sr, SAMPLE_RATE)
            wave = wave[0].contiguous().to(device)
            audio_duration = wave.shape[0] / SAMPLE_RATE

            # Extract features
            features = fbank([wave])
            feature_lengths = torch.tensor([features[0].size(0)], device=device)
            features = pad_sequence(
                features, batch_first=True, padding_value=math.log(1e-10)
            )

            # Encode
            encoder_out, encoder_out_lens = model.forward_encoder(
                features, feature_lengths
            )

            # Decode
            if args.decoding_method == "greedy_search":
                hyp_tokens = greedy_search_batch(
                    model=model,
                    encoder_out=encoder_out,
                    encoder_out_lens=encoder_out_lens,
                )
            else:
                hyp_tokens = modified_beam_search(
                    model=model,
                    encoder_out=encoder_out,
                    encoder_out_lens=encoder_out_lens,
                    beam=args.beam_size,
                )

            # Convert tokens to text
            text = sp.decode(hyp_tokens[0])

            elapsed = time.time() - start
            rtf = elapsed / audio_duration if audio_duration > 0 else 0

            print(f"\n  File: {audio_path}")
            print(f"  Text: {text}")
            print(f"  Time: {elapsed:.2f}s | Audio: {audio_duration:.2f}s | RTF: {rtf:.3f}")


if __name__ == "__main__":
    main()
