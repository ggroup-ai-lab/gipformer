# Gipformer - Efficient Vietnamese Speech Recognition

[![Demo](https://img.shields.io/badge/Demo-gipformer--demo-yellow?logo=huggingface)](https://huggingface.co/spaces/g-group-ai-lab/gipformer-demo)
[![Model](https://img.shields.io/badge/Model-gipformer1.5--65M--rnnt-blue?logo=huggingface)](https://huggingface.co/g-group-ai-lab/gipformer1.5-65M-rnnt)
[![Model](https://img.shields.io/badge/Model-gipformer--65M--rnnt-blue?logo=huggingface)](https://huggingface.co/g-group-ai-lab/gipformer-65M-rnnt)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Highlights

- **State-of-the-art accuracy** — Demonstrates top-tier performance across major Vietnamese ASR benchmarks, delivering highly precise and reliable transcription quality.
- **Robust handling of telephonic domains** — Excels in processing challenging, noisy real-world call center recordings across all major Vietnamese regional accents.
- **Domain-leading accuracy** — Best WER on the technology, finance, education, public administration and medical benchmarks.
- **Outstanding parameter efficiency** — Ranks among the smallest ASR models currently available.
- **Seamless edge deployment** — Its naturally low resource requirements enable ultra-fast inference on mobile and embedded systems, making it perfectly suited for offline, on-device applications.
- **Built-in data privacy** — By supporting full local execution, the model ensures sensitive audio data is processed securely on-device, eliminating the need for third-party cloud services.
- *gipformer-65M-rnnt* and *gipformer1.5-65M-rnnt* are both based on the Zipformer Transducer architecture.

## Benchmark Results (WER%)

Lower is better; **bold** = best in each column.

> **Normalization:** Both predictions and labels are normalized before computing WER — lowercased, punctuation removed, and numbers converted to spoken form.

| Model | Params | tele-medium | tele-hard-north | tele-hard-middle | tele-hard-south | vi-asr-tech | vi-asr-edu | vi-asr-finance | vi-asr-pubadmin | vivos | Common-Voice | vlsp-t1 | VietMed | MultiMED | LSVSC | Fleurs | ViMD |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| vinai/PhoWhisper-small | 244M | 33.96 | 55.88 | 65.41 | 62.35 | 56.81 | 51.87 | 47.36 | 41.46 | 6.23 | 11.55 | 15.99 | 25.50 | 26.02 | 11.23 | 16.11 | 14.09 |
| vinai/PhoWhisper-medium | 769M | 26.46 | 51.20 | 59.04 | 55.39 | 47.93 | 43.00 | 41.60 | 34.81 | 4.93 | 8.37 | 14.06 | 24.90 | 24.76 | 10.25 | 14.44 | 11.34 |
| vinai/PhoWhisper-large | 1.5B | 26.82 | 50.39 | 59.44 | 56.70 | 42.94 | 44.99 | 40.54 | 33.78 | 4.73 | 8.60 | 13.70 | 24.37 | 24.47 | 10.08 | 12.62 | 11.18 |
| Qualcomm-AI-Research/PhoASR-whisper-small | 244M | 30.73 | 50.30 | 56.66 | 54.12 | 44.35 | 41.65 | — | 35.99 | 5.87 | 9.73 | 14.60 | 23.10 | 22.78 | **7.59** | 13.97 | 9.75 |
| nvidia/parakeet-ctc-0.6b-Vietnamese | 600M | 31.82 | 55.33 | 61.65 | 56.70 | 48.69 | 45.86 | 43.16 | 38.84 | 7.76 | 11.40 | 17.00 | 23.53 | 23.79 | 10.46 | 16.11 | 12.95 |
| khanhld/chunkformer-large-vie | 110M | 27.60 | 46.30 | 51.91 | 49.09 | 39.81 | 37.20 | 34.31 | 29.30 | 4.18 | 6.94 | 14.09 | 19.59 | 22.60 | 8.85 | 14.17 | 11.77 |
| nguyenvulebinh/wav2vec2-base-vi | 95M | 23.71 | 40.49 | 48.90 | 46.33 | 59.86 | 53.06 | 49.66 | 39.82 | 6.60 | 12.61 | 13.14 | 22.96 | 23.03 | 9.89 | 20.09 | 11.42 |
| zipformer-rnnt | 65M | 20.30 | 42.21 | 49.01 | 47.86 | 36.81 | 30.26 | 29.13 | 18.62 | 6.92 | 11.48 | 14.54 | 21.90 | 22.05 | 10.23 | 14.76 | 10.15 |
| Qwen/Qwen3-ASR-1.7B | 1.7B | 26.34 | 46.80 | 59.85 | 51.84 | 27.95 | 29.93 | 34.09 | 31.83 | 7.17 | 10.76 | 16.29 | 20.21 | 20.11 | 9.64 | **10.13** | 11.16 |
| Qwen/Qwen3-ASR-0.6B | 600M | 32.29 | 48.57 | 61.88 | 55.43 | 37.52 | 36.97 | 38.31 | 38.65 | 10.23 | 16.68 | 18.62 | 22.51 | 22.65 | 10.96 | 13.11 | 14.37 |
| hynt/Zipformer-30M-RNNT-6000h | 30M | 19.53 | 38.13 | 44.73 | 41.58 | 29.77 | 25.91 | 25.86 | 17.92 | 4.55 | **4.16** | **11.78** | 19.91 | 19.88 | 9.04 | 13.03 | 7.18 |
| g-group-ai-lab/gipformer-65M-rnnt | 65M | 15.53 | **25.10** | **32.27** | 32.62 | 36.59 | 29.81 | 29.67 | 20.09 | **4.12** | 6.63 | 13.39 | 19.41 | 19.35 | 8.96 | 12.92 | 7.17 |
| **g-group-ai-lab/gipformer1.5-65M-rnnt** | **65M** | **15.44** | 26.24 | 33.31 | **32.48** | **27.49** | **23.32** | **22.34** | **14.82** | 4.25 | 6.45 | 13.37 | **19.23** | **19.17** | 8.97 | 12.65 | **7.00** |

### Dataset Descriptions

**Private test sets (call center domain):**

- **tele-medium** — Call center recordings with medium difficulty
- **tele-hard-north** — Low-quality call center audio, hard-to-hear speakers — Northern Vietnamese accent
- **tele-hard-middle** — Low-quality call center audio, hard-to-hear speakers — Central Vietnamese accent
- **tele-hard-south** — Low-quality call center audio, hard-to-hear speakers — Southern Vietnamese accent

**Public test sets:**

- **[vi-asr-tech-test](https://huggingface.co/datasets/g-group-ai-lab/vi-asr-tech-test)** — Technology: consumer electronics reviews, software tutorials, programming and IT walkthroughs
- **[vi-asr-edu-test](https://huggingface.co/datasets/g-group-ai-lab/vi-asr-edu-test)** — Education: study-abroad consulting, exam guidance, university and training-course introductions
- **[vi-asr-finance-test](https://huggingface.co/datasets/g-group-ai-lab/vi-asr-finance-test)** — Finance: stock market commentary, trading platforms, banking and crypto
- **[vi-asr-pubadmin-test](https://huggingface.co/datasets/g-group-ai-lab/vi-asr-pubadmin-test)** — Public administration: administrative procedures, licensing guidance, civil records
- **vivos** — Vietnamese read speech corpus
- **Common-Voice** — Mozilla Common Voice, Vietnamese subset
- **vlsp-t1** — VLSP 2020 ASR Shared Task 1
- **VietMed** — Vietnamese medical domain
- **MultiMED** — Multi-domain medical conversations
- **LSVSC** — Large-Scale Vietnamese Speech Corpus
- **Fleurs** — Google's Few-shot Learning Evaluation of Universal Representations of Speech, Vietnamese subset
- **ViMD** — Vietnamese Multi-Domain

### Call Center Domain: Where It Matters Most

Call center ASR is one of the most challenging real-world domains — noisy phone
lines, overlapping speech, diverse regional accents, and spontaneous
conversation. The gipformer family holds the best result on all call
center test sets.

## Quick Start

This project uses [**uv**](https://github.com/astral-sh/uv) for dependency
management. Install uv first ([instructions](https://docs.astral.sh/uv/getting-started/installation/)),
then:

```bash
# Core (ONNX inference) — works on every platform (CPU/GPU/mobile)
uv sync

# + PyTorch / icefall stack (research & fine-tuning) — Linux + CUDA only
uv sync --extra pytorch
```

`uv sync` creates an isolated `.venv` and installs the pinned dependencies from
`pyproject.toml` / `uv.lock`. **Activate it once**, then run `python ...`
directly — all examples below assume an activated venv:

```bash
source .venv/bin/activate          # Linux / macOS
```

### ONNX Inference (Recommended)

The simplest way to run the model. Supports CPU, GPU, mobile, and embedded devices.

```bash
# Full infer with fp32
python infer_onnx.py --audio data/audio1.wav

# INT8 quantized (smaller & faster)
python infer_onnx.py --audio data/audio1.wav --quantize int8

# Multiple files
python infer_onnx.py --audio data/audio1.wav data/audio2.wav data/audio3.wav

# Pick a model version (default: 1.5)
python infer_onnx.py --audio data/audio1.wav --version 1

# Load from a local model directory instead of downloading
python infer_onnx.py --audio data/audio1.wav --model-dir [path-to-model]
```

### PyTorch Inference (Advanced)

For research and fine-tuning. Requires a Linux machine with CUDA. Install the
extra first with `uv sync --extra pytorch`.

```bash
# Basic usage
python infer_pytorch.py --audio data/audio1.wav

# Use GPU
python infer_pytorch.py --audio data/audio1.wav --device cuda

# Multiple files
python infer_pytorch.py --audio data/audio1.wav data/audio2.wav data/audio3.wav

# Pick a model version (default: 1.5)
python infer_pytorch.py --audio data/audio1.wav --version 1

# Load from a local model directory instead of downloading
python infer_pytorch.py --audio data/audio1.wav --model-dir [path-to-model]
```

## Citation

```bibtex
@misc{gipformer,
  title={Gipformer - Efficient Vietnamese Speech Recognition},
  author={G-Group AI Lab},
  year={2026},
  url={https://huggingface.co/g-group-ai-lab/gipformer1.5-65M-rnnt}
}
```

## License

This project is licensed under the MIT License.

## Acknowledgments

- [k2](https://github.com/k2-fsa/k2)
- [icefall](https://github.com/k2-fsa/icefall)
- [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx)
