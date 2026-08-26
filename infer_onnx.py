#!/usr/bin/env python3
"""
Gipformer ONNX Inference - Vietnamese ASR
Uses sherpa-onnx for fast, cross-platform speech recognition.

Usage:
    python infer_onnx.py --audio data/audio1.wav
    python infer_onnx.py --audio data/audio1.wav --quantize int8
    python infer_onnx.py --audio data/audio1.wav --version 1
    python infer_onnx.py --audio data/audio1.wav --model-dir ./huggingface/gipformer1.5-65M-rnnt
    python infer_onnx.py --audio file1.wav file2.wav --num-threads 4
"""

import argparse
import sys
import time
from pathlib import Path

import soundfile as sf

try:
    import sherpa_onnx
except ImportError as e:
    print(f"Error: could not import sherpa-onnx ({e}).")
    print("Install it with: pip install sherpa-onnx sherpa-onnx-core")
    print(
        "Note: as of sherpa-onnx 1.13, the native libs (libonnxruntime.so) live "
        "in the separate 'sherpa-onnx-core' package — both must be installed."
    )
    sys.exit(1)

try:
    from huggingface_hub import hf_hub_download
except ImportError:
    print("Error: huggingface_hub is not installed.")
    print("Install it with: pip install huggingface_hub")
    sys.exit(1)

# HuggingFace repo per model version. Both repos use the same canonical
# filenames (encoder.onnx, decoder.onnx, joiner.onnx, tokens.txt, ...).
REPO_IDS = {
    "1": "g-group-ai-lab/gipformer-65M-rnnt",
    "1.5": "g-group-ai-lab/gipformer1.5-65M-rnnt",
}
DEFAULT_VERSION = "1.5"

SAMPLE_RATE = 16000
FEATURE_DIM = 80

ONNX_FILES = {
    "fp32": {
        "encoder": "encoder.onnx",
        "decoder": "decoder.onnx",
        "joiner": "joiner.onnx",
    },
    "int8": {
        "encoder": "encoder.int8.onnx",
        "decoder": "decoder.int8.onnx",
        "joiner": "joiner.int8.onnx",
    },
}

TOKENS_FILE = "tokens.txt"


def load_model(
    quantize: str = "int8",
    version: str = DEFAULT_VERSION,
    model_dir: str = None,
) -> dict:
    """Resolve the ONNX model files, downloading them from HuggingFace if needed.

    Args:
        quantize: "fp32" for full precision, "int8" for quantized (smaller, faster).
        version: Model version key, see REPO_IDS.
        model_dir: Local directory holding the model files. When given, nothing
            is downloaded and the files are read straight from disk.

    Returns:
        Dict with local paths to encoder, decoder, joiner, and tokens files.
    """
    filenames = dict(ONNX_FILES[quantize], tokens=TOKENS_FILE)

    if model_dir:
        directory = Path(model_dir).expanduser()
        if not directory.is_dir():
            print(f"Error: model directory not found: {directory}")
            sys.exit(1)

        print(f"Loading {quantize} model from {directory}...")
        paths = {}
        for key, filename in filenames.items():
            path = directory / filename
            if not path.exists():
                print(f"Error: missing '{filename}' in {directory}")
                sys.exit(1)
            paths[key] = str(path)
        return paths

    repo_id = REPO_IDS[version]
    print(f"Downloading {quantize} model from {repo_id}...")

    try:
        paths = {
            key: hf_hub_download(repo_id=repo_id, filename=filename)
            for key, filename in filenames.items()
        }
    except Exception as e:
        print(f"Error: could not fetch the model from {repo_id} ({e}).")
        print("Pass --model-dir to load the model from a local directory instead.")
        sys.exit(1)

    print("Model downloaded successfully.")
    return paths


def read_audio(filename: str) -> tuple:
    """Read an audio file and return float32 samples and sample rate.

    Supports WAV, FLAC, OGG, and other formats via soundfile.
    """
    samples, sample_rate = sf.read(filename, dtype="float32")

    # Convert stereo to mono if needed
    if samples.ndim > 1:
        samples = samples.mean(axis=1)

    return samples, sample_rate


def create_recognizer(
    model_paths: dict,
    num_threads: int = 4,
    decoding_method: str = "greedy_search",
) -> sherpa_onnx.OfflineRecognizer:
    """Create a sherpa-onnx OfflineRecognizer for transducer decoding."""
    return sherpa_onnx.OfflineRecognizer.from_transducer(
        encoder=model_paths["encoder"],
        decoder=model_paths["decoder"],
        joiner=model_paths["joiner"],
        tokens=model_paths["tokens"],
        num_threads=num_threads,
        sample_rate=SAMPLE_RATE,
        feature_dim=FEATURE_DIM,
        decoding_method=decoding_method,
    )


def transcribe(recognizer: sherpa_onnx.OfflineRecognizer, audio_path: str) -> str:
    """Transcribe a single audio file.

    Returns the recognized text.
    """
    samples, sample_rate = read_audio(audio_path)

    stream = recognizer.create_stream()
    stream.accept_waveform(sample_rate, samples)
    recognizer.decode_streams([stream])

    return stream.result.text.strip()


def main():
    parser = argparse.ArgumentParser(
        description="Gipformer ONNX Inference - Vietnamese ASR",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
        "  python infer_onnx.py --audio data/audio1.wav\n"
        "  python infer_onnx.py --audio data/audio1.wav --quantize fp32\n"
        "  python infer_onnx.py --audio data/audio1.wav --version 1\n"
        "  python infer_onnx.py --audio data/audio1.wav --model-dir ./local/model\n"
        "  python infer_onnx.py --audio f1.wav f2.wav --num-threads 4\n",
    )
    parser.add_argument(
        "--audio",
        type=str,
        nargs="+",
        required=True,
        help="Path(s) to audio file(s) to transcribe",
    )
    parser.add_argument(
        "--version",
        type=str,
        choices=sorted(REPO_IDS),
        default=DEFAULT_VERSION,
        help=f"Gipformer model version (default: {DEFAULT_VERSION})",
    )
    parser.add_argument(
        "--model-dir",
        type=str,
        default=None,
        help="Load the model from a local directory instead of HuggingFace",
    )
    parser.add_argument(
        "--quantize",
        type=str,
        choices=["fp32", "int8"],
        default="fp32",
        help="Model precision: fp32 (full, default) or int8 (quantized)",
    )
    parser.add_argument(
        "--num-threads",
        type=int,
        default=4,
        help="Number of threads for inference (default: 4)",
    )
    parser.add_argument(
        "--decoding-method",
        type=str,
        choices=["greedy_search", "modified_beam_search"],
        default="modified_beam_search",
        help="Decoding method (default: modified_beam_search)",
    )
    args = parser.parse_args()

    # Resolve model files
    model_paths = load_model(args.quantize, args.version, args.model_dir)

    # Create recognizer
    recognizer = create_recognizer(
        model_paths,
        num_threads=args.num_threads,
        decoding_method=args.decoding_method,
    )

    # Transcribe each audio file
    for audio_path in args.audio:
        start = time.time()
        text = transcribe(recognizer, audio_path)
        elapsed = time.time() - start

        audio_info = sf.info(audio_path)
        duration = audio_info.duration
        rtf = elapsed / duration if duration > 0 else 0

        print(f"\n  File: {audio_path}")
        print(f"  Text: {text}")
        print(f"  Time: {elapsed:.2f}s | Audio: {duration:.2f}s | RTF: {rtf:.3f}")


if __name__ == "__main__":
    main()
