# Gipformer - Efficient Vietnamese Speech Recognition

[![Demo][badge-demo]][demo]
[![Model][badge-v15]][model-v15]
[![Model][badge-v1]][model-v1]
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

> **Normalization:** Both predictions and labels are normalized before computing WER — lowercased, diacritics removed, and numbers converted to spoken form.

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

<!-- Link and badge definitions.
     The three Hugging Face badges embed the official logo from
     huggingface.co/front/assets/huggingface_logo-noborder.svg as a data URI:
     shields.io only accepts its own named logos or inline data, and the file
     ships without a viewBox, so a square one is added to stop it being cropped.
     Kept down here because each badge URL is ~6 KB. -->

[demo]: https://huggingface.co/spaces/g-group-ai-lab/gipformer-demo
[model-v15]: https://huggingface.co/g-group-ai-lab/gipformer1.5-65M-rnnt
[model-v1]: https://huggingface.co/g-group-ai-lab/gipformer-65M-rnnt

[badge-demo]: https://img.shields.io/badge/Demo-gipformer--demo-yellow?logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjQuNzUgMyA4NSA4NSIgZmlsbD0ibm9uZSI%2BPHBhdGggZmlsbD0iI0ZGRDIxRSIgZD0iTTQ3LjIxIDc2LjVhMzQuNzUgMzQuNzUgMCAxIDAgMC02OS41IDM0Ljc1IDM0Ljc1IDAgMCAwIDAgNjkuNVoiLz48cGF0aCBmaWxsPSIjRkY5RDBCIiBkPSJNODEuOTYgNDEuNzVhMzQuNzUgMzQuNzUgMCAxIDAtNjkuNSAwIDM0Ljc1IDM0Ljc1IDAgMCAwIDY5LjUgMFptLTczLjUgMGEzOC43NSAzOC43NSAwIDEgMSA3Ny41IDAgMzguNzUgMzguNzUgMCAwIDEtNzcuNSAwWiIvPjxwYXRoIGZpbGw9IiMzQTNCNDUiIGQ9Ik01OC41IDMyLjNjMS4yOC40NCAxLjc4IDMuMDYgMy4wNyAyLjM4YTUgNSAwIDEgMC02Ljc2LTIuMDdjLjYxIDEuMTUgMi41NS0uNzIgMy43LS4zMlpNMzQuOTUgMzIuM2MtMS4yOC40NC0xLjc5IDMuMDYtMy4wNyAyLjM4YTUgNSAwIDEgMSA2Ljc2LTIuMDdjLS42MSAxLjE1LTIuNTYtLjcyLTMuNy0uMzJaIi8%2BPHBhdGggZmlsbD0iI0ZGMzIzRCIgZD0iTTQ2Ljk2IDU2LjI5YzkuODMgMCAxMy04Ljc2IDEzLTEzLjI2IDAtMi4zNC0xLjU3LTEuNi00LjA5LS4zNi0yLjMzIDEuMTUtNS40NiAyLjc0LTguOSAyLjc0LTcuMTkgMC0xMy02Ljg4LTEzLTIuMzhzMy4xNiAxMy4yNiAxMyAxMy4yNloiLz48cGF0aCBmaWxsPSIjM0EzQjQ1IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zOS40MyA1NGE4LjcgOC43IDAgMCAxIDUuMy00LjQ5Yy40LS4xMi44MS41NyAxLjI0IDEuMjguNC42OC44MiAxLjM3IDEuMjQgMS4zNy40NSAwIC45LS42OCAxLjMzLTEuMzUuNDUtLjcuODktMS4zOCAxLjMyLTEuMjVhOC42MSA4LjYxIDAgMCAxIDUgNC4xN2MzLjczLTIuOTQgNS4xLTcuNzQgNS4xLTEwLjcgMC0yLjM0LTEuNTctMS42LTQuMDktLjM2bC0uMTQuMDdjLTIuMzEgMS4xNS01LjM5IDIuNjctOC43NyAyLjY3cy02LjQ1LTEuNTItOC43Ny0yLjY3Yy0yLjYtMS4yOS00LjIzLTIuMS00LjIzLjI5IDAgMy4wNSAxLjQ2IDguMDYgNS40NyAxMC45N1oiIGNsaXAtcnVsZT0iZXZlbm9kZCIvPjxwYXRoIGZpbGw9IiNGRjlEMEIiIGQ9Ik03MC43MSAzN2EzLjI1IDMuMjUgMCAxIDAgMC02LjUgMy4yNSAzLjI1IDAgMCAwIDAgNi41Wk0yNC4yMSAzN2EzLjI1IDMuMjUgMCAxIDAgMC02LjUgMy4yNSAzLjI1IDAgMCAwIDAgNi41Wk0xNy41MiA0OGMtMS42MiAwLTMuMDYuNjYtNC4wNyAxLjg3YTUuOTcgNS45NyAwIDAgMC0xLjMzIDMuNzYgNy4xIDcuMSAwIDAgMC0xLjk0LS4zYy0xLjU1IDAtMi45NS41OS0zLjk0IDEuNjZhNS44IDUuOCAwIDAgMC0uOCA3IDUuMyA1LjMgMCAwIDAtMS43OSAyLjgyYy0uMjQuOS0uNDggMi44LjggNC43NGE1LjIyIDUuMjIgMCAwIDAtLjM3IDUuMDJjMS4wMiAyLjMyIDMuNTcgNC4xNCA4LjUyIDYuMSAzLjA3IDEuMjIgNS44OSAyIDUuOTEgMi4wMWE0NC4zMyA0NC4zMyAwIDAgMCAxMC45MyAxLjZjNS44NiAwIDEwLjA1LTEuOCAxMi40Ni01LjM0IDMuODgtNS42OSAzLjMzLTEwLjktMS43LTE1LjkyLTIuNzctMi43OC00LjYyLTYuODctNS03Ljc3LS43OC0yLjY2LTIuODQtNS42Mi02LjI1LTUuNjJhNS43IDUuNyAwIDAgMC00LjYgMi40NmMtMS0xLjI2LTEuOTgtMi4yNS0yLjg2LTIuODJBNy40IDcuNCAwIDAgMCAxNy41MiA0OFptMCA0Yy41MSAwIDEuMTQuMjIgMS44Mi42NSAyLjE0IDEuMzYgNi4yNSA4LjQzIDcuNzYgMTEuMTguNS45MiAxLjM3IDEuMzEgMi4xNCAxLjMxIDEuNTUgMCAyLjc1LTEuNTMuMTUtMy40OC0zLjkyLTIuOTMtMi41NS03LjcyLS42OC04LjAxLjA4LS4wMi4xNy0uMDIuMjQtLjAyIDEuNyAwIDIuNDUgMi45MyAyLjQ1IDIuOTNzMi4yIDUuNTIgNS45OCA5LjNjMy43NyAzLjc3IDMuOTcgNi44IDEuMjIgMTAuODMtMS44OCAyLjc1LTUuNDcgMy41OC05LjE2IDMuNTgtMy44MSAwLTcuNzMtLjktOS45Mi0xLjQ2LS4xMS0uMDMtMTMuNDUtMy44LTExLjc2LTcgLjI4LS41NC43NS0uNzYgMS4zNC0uNzYgMi4zOCAwIDYuNyAzLjU0IDguNTcgMy41NC40MSAwIC43LS4xNy44My0uNi43OS0yLjg1LTEyLjA2LTQuMDUtMTAuOTgtOC4xNy4yLS43My43MS0xLjAyIDEuNDQtMS4wMiAzLjE0IDAgMTAuMiA1LjUzIDExLjY4IDUuNTMuMTEgMCAuMi0uMDMuMjQtLjEuNzQtMS4yLjMzLTIuMDQtNC45LTUuMi01LjIxLTMuMTYtOC44OC01LjA2LTYuOC03LjMzLjI0LS4yNi41OC0uMzggMS0uMzggMy4xNyAwIDEwLjY2IDYuODIgMTAuNjYgNi44MnMyLjAyIDIuMSAzLjI1IDIuMWMuMjggMCAuNTItLjEuNjgtLjM4Ljg2LTEuNDYtOC4wNi04LjIyLTguNTYtMTEuMDEtLjM0LTEuOS4yNC0yLjg1IDEuMzEtMi44NVoiLz48cGF0aCBmaWxsPSIjRkZEMjFFIiBkPSJNMzguNiA3Ni42OWMyLjc1LTQuMDQgMi41NS03LjA3LTEuMjItMTAuODQtMy43OC0zLjc3LTUuOTgtOS4zLTUuOTgtOS4zcy0uODItMy4yLTIuNjktMi45Yy0xLjg3LjMtMy4yNCA1LjA4LjY4IDguMDEgMy45MSAyLjkzLS43OCA0LjkyLTIuMjkgMi4xNy0xLjUtMi43NS01LjYyLTkuODItNy43Ni0xMS4xOC0yLjEzLTEuMzUtMy42My0uNi0zLjEzIDIuMi41IDIuNzkgOS40MyA5LjU1IDguNTYgMTEtLjg3IDEuNDctMy45My0xLjcxLTMuOTMtMS43MXMtOS41Ny04LjcxLTExLjY2LTYuNDRjLTIuMDggMi4yNyAxLjU5IDQuMTcgNi44IDcuMzMgNS4yMyAzLjE2IDUuNjQgNCA0LjkgNS4yLS43NSAxLjItMTIuMjgtOC41My0xMy4zNi00LjQtMS4wOCA0LjExIDExLjc3IDUuMyAxMC45OCA4LjE1LS44IDIuODUtOS4wNi01LjM4LTEwLjc0LTIuMTgtMS43IDMuMjEgMTEuNjUgNi45OCAxMS43NiA3LjAxIDQuMyAxLjEyIDE1LjI1IDMuNDkgMTkuMDgtMi4xMloiLz48cGF0aCBmaWxsPSIjRkY5RDBCIiBkPSJNNzcuNCA0OGMxLjYyIDAgMy4wNy42NiA0LjA3IDEuODdhNS45NyA1Ljk3IDAgMCAxIDEuMzMgMy43NiA3LjEgNy4xIDAgMCAxIDEuOTUtLjNjMS41NSAwIDIuOTUuNTkgMy45NCAxLjY2YTUuOCA1LjggMCAwIDEgLjggNyA1LjMgNS4zIDAgMCAxIDEuNzggMi44MmMuMjQuOS40OCAyLjgtLjggNC43NGE1LjIyIDUuMjIgMCAwIDEgLjM3IDUuMDJjLTEuMDIgMi4zMi0zLjU3IDQuMTQtOC41MSA2LjEtMy4wOCAxLjIyLTUuOSAyLTUuOTIgMi4wMWE0NC4zMyA0NC4zMyAwIDAgMS0xMC45MyAxLjZjLTUuODYgMC0xMC4wNS0xLjgtMTIuNDYtNS4zNC0zLjg4LTUuNjktMy4zMy0xMC45IDEuNy0xNS45MiAyLjc4LTIuNzggNC42My02Ljg3IDUuMDEtNy43Ny43OC0yLjY2IDIuODMtNS42MiA2LjI0LTUuNjJhNS43IDUuNyAwIDAgMSA0LjYgMi40NmMxLTEuMjYgMS45OC0yLjI1IDIuODctMi44MkE3LjQgNy40IDAgMCAxIDc3LjQgNDhabTAgNGMtLjUxIDAtMS4xMy4yMi0xLjgyLjY1LTIuMTMgMS4zNi02LjI1IDguNDMtNy43NiAxMS4xOGEyLjQzIDIuNDMgMCAwIDEtMi4xNCAxLjMxYy0xLjU0IDAtMi43NS0xLjUzLS4xNC0zLjQ4IDMuOTEtMi45MyAyLjU0LTcuNzIuNjctOC4wMWExLjU0IDEuNTQgMCAwIDAtLjI0LS4wMmMtMS43IDAtMi40NSAyLjkzLTIuNDUgMi45M3MtMi4yIDUuNTItNS45NyA5LjNjLTMuNzggMy43Ny0zLjk4IDYuOC0xLjIyIDEwLjgzIDEuODcgMi43NSA1LjQ3IDMuNTggOS4xNSAzLjU4IDMuODIgMCA3LjczLS45IDkuOTMtMS40Ni4xLS4wMyAxMy40NS0zLjggMTEuNzYtNy0uMjktLjU0LS43NS0uNzYtMS4zNC0uNzYtMi4zOCAwLTYuNzEgMy41NC04LjU3IDMuNTQtLjQyIDAtLjcxLS4xNy0uODMtLjYtLjgtMi44NSAxMi4wNS00LjA1IDEwLjk3LTguMTctLjE5LS43My0uNy0xLjAyLTEuNDQtMS4wMi0zLjE0IDAtMTAuMiA1LjUzLTExLjY4IDUuNTMtLjEgMC0uMTktLjAzLS4yMy0uMS0uNzQtMS4yLS4zNC0yLjA0IDQuODgtNS4yIDUuMjMtMy4xNiA4LjktNS4wNiA2LjgtNy4zMy0uMjMtLjI2LS41Ny0uMzgtLjk4LS4zOC0zLjE4IDAtMTAuNjcgNi44Mi0xMC42NyA2Ljgycy0yLjAyIDIuMS0zLjI0IDIuMWEuNzQuNzQgMCAwIDEtLjY4LS4zOGMtLjg3LTEuNDYgOC4wNS04LjIyIDguNTUtMTEuMDEuMzQtMS45LS4yNC0yLjg1LTEuMzEtMi44NVoiLz48cGF0aCBmaWxsPSIjRkZEMjFFIiBkPSJNNTYuMzMgNzYuNjljLTIuNzUtNC4wNC0yLjU2LTcuMDcgMS4yMi0xMC44NCAzLjc3LTMuNzcgNS45Ny05LjMgNS45Ny05LjNzLjgyLTMuMiAyLjctMi45YzEuODYuMyAzLjIzIDUuMDgtLjY4IDguMDEtMy45MiAyLjkzLjc4IDQuOTIgMi4yOCAyLjE3IDEuNTEtMi43NSA1LjYzLTkuODIgNy43Ni0xMS4xOCAyLjEzLTEuMzUgMy42NC0uNiAzLjEzIDIuMi0uNSAyLjc5LTkuNDIgOS41NS04LjU1IDExIC44NiAxLjQ3IDMuOTItMS43MSAzLjkyLTEuNzFzOS41OC04LjcxIDExLjY2LTYuNDRjMi4wOCAyLjI3LTEuNTggNC4xNy02LjggNy4zMy01LjIzIDMuMTYtNS42MyA0LTQuOSA1LjIuNzUgMS4yIDEyLjI4LTguNTMgMTMuMzYtNC40IDEuMDggNC4xMS0xMS43NiA1LjMtMTAuOTcgOC4xNS44IDIuODUgOS4wNS01LjM4IDEwLjc0LTIuMTggMS42OSAzLjIxLTExLjY1IDYuOTgtMTEuNzYgNy4wMS00LjMxIDEuMTItMTUuMjYgMy40OS0xOS4wOC0yLjEyWiIvPjwvc3ZnPg%3D%3D
[badge-v15]: https://img.shields.io/badge/Model-gipformer1.5--65M--rnnt-blue?logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjQuNzUgMyA4NSA4NSIgZmlsbD0ibm9uZSI%2BPHBhdGggZmlsbD0iI0ZGRDIxRSIgZD0iTTQ3LjIxIDc2LjVhMzQuNzUgMzQuNzUgMCAxIDAgMC02OS41IDM0Ljc1IDM0Ljc1IDAgMCAwIDAgNjkuNVoiLz48cGF0aCBmaWxsPSIjRkY5RDBCIiBkPSJNODEuOTYgNDEuNzVhMzQuNzUgMzQuNzUgMCAxIDAtNjkuNSAwIDM0Ljc1IDM0Ljc1IDAgMCAwIDY5LjUgMFptLTczLjUgMGEzOC43NSAzOC43NSAwIDEgMSA3Ny41IDAgMzguNzUgMzguNzUgMCAwIDEtNzcuNSAwWiIvPjxwYXRoIGZpbGw9IiMzQTNCNDUiIGQ9Ik01OC41IDMyLjNjMS4yOC40NCAxLjc4IDMuMDYgMy4wNyAyLjM4YTUgNSAwIDEgMC02Ljc2LTIuMDdjLjYxIDEuMTUgMi41NS0uNzIgMy43LS4zMlpNMzQuOTUgMzIuM2MtMS4yOC40NC0xLjc5IDMuMDYtMy4wNyAyLjM4YTUgNSAwIDEgMSA2Ljc2LTIuMDdjLS42MSAxLjE1LTIuNTYtLjcyLTMuNy0uMzJaIi8%2BPHBhdGggZmlsbD0iI0ZGMzIzRCIgZD0iTTQ2Ljk2IDU2LjI5YzkuODMgMCAxMy04Ljc2IDEzLTEzLjI2IDAtMi4zNC0xLjU3LTEuNi00LjA5LS4zNi0yLjMzIDEuMTUtNS40NiAyLjc0LTguOSAyLjc0LTcuMTkgMC0xMy02Ljg4LTEzLTIuMzhzMy4xNiAxMy4yNiAxMyAxMy4yNloiLz48cGF0aCBmaWxsPSIjM0EzQjQ1IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zOS40MyA1NGE4LjcgOC43IDAgMCAxIDUuMy00LjQ5Yy40LS4xMi44MS41NyAxLjI0IDEuMjguNC42OC44MiAxLjM3IDEuMjQgMS4zNy40NSAwIC45LS42OCAxLjMzLTEuMzUuNDUtLjcuODktMS4zOCAxLjMyLTEuMjVhOC42MSA4LjYxIDAgMCAxIDUgNC4xN2MzLjczLTIuOTQgNS4xLTcuNzQgNS4xLTEwLjcgMC0yLjM0LTEuNTctMS42LTQuMDktLjM2bC0uMTQuMDdjLTIuMzEgMS4xNS01LjM5IDIuNjctOC43NyAyLjY3cy02LjQ1LTEuNTItOC43Ny0yLjY3Yy0yLjYtMS4yOS00LjIzLTIuMS00LjIzLjI5IDAgMy4wNSAxLjQ2IDguMDYgNS40NyAxMC45N1oiIGNsaXAtcnVsZT0iZXZlbm9kZCIvPjxwYXRoIGZpbGw9IiNGRjlEMEIiIGQ9Ik03MC43MSAzN2EzLjI1IDMuMjUgMCAxIDAgMC02LjUgMy4yNSAzLjI1IDAgMCAwIDAgNi41Wk0yNC4yMSAzN2EzLjI1IDMuMjUgMCAxIDAgMC02LjUgMy4yNSAzLjI1IDAgMCAwIDAgNi41Wk0xNy41MiA0OGMtMS42MiAwLTMuMDYuNjYtNC4wNyAxLjg3YTUuOTcgNS45NyAwIDAgMC0xLjMzIDMuNzYgNy4xIDcuMSAwIDAgMC0xLjk0LS4zYy0xLjU1IDAtMi45NS41OS0zLjk0IDEuNjZhNS44IDUuOCAwIDAgMC0uOCA3IDUuMyA1LjMgMCAwIDAtMS43OSAyLjgyYy0uMjQuOS0uNDggMi44LjggNC43NGE1LjIyIDUuMjIgMCAwIDAtLjM3IDUuMDJjMS4wMiAyLjMyIDMuNTcgNC4xNCA4LjUyIDYuMSAzLjA3IDEuMjIgNS44OSAyIDUuOTEgMi4wMWE0NC4zMyA0NC4zMyAwIDAgMCAxMC45MyAxLjZjNS44NiAwIDEwLjA1LTEuOCAxMi40Ni01LjM0IDMuODgtNS42OSAzLjMzLTEwLjktMS43LTE1LjkyLTIuNzctMi43OC00LjYyLTYuODctNS03Ljc3LS43OC0yLjY2LTIuODQtNS42Mi02LjI1LTUuNjJhNS43IDUuNyAwIDAgMC00LjYgMi40NmMtMS0xLjI2LTEuOTgtMi4yNS0yLjg2LTIuODJBNy40IDcuNCAwIDAgMCAxNy41MiA0OFptMCA0Yy41MSAwIDEuMTQuMjIgMS44Mi42NSAyLjE0IDEuMzYgNi4yNSA4LjQzIDcuNzYgMTEuMTguNS45MiAxLjM3IDEuMzEgMi4xNCAxLjMxIDEuNTUgMCAyLjc1LTEuNTMuMTUtMy40OC0zLjkyLTIuOTMtMi41NS03LjcyLS42OC04LjAxLjA4LS4wMi4xNy0uMDIuMjQtLjAyIDEuNyAwIDIuNDUgMi45MyAyLjQ1IDIuOTNzMi4yIDUuNTIgNS45OCA5LjNjMy43NyAzLjc3IDMuOTcgNi44IDEuMjIgMTAuODMtMS44OCAyLjc1LTUuNDcgMy41OC05LjE2IDMuNTgtMy44MSAwLTcuNzMtLjktOS45Mi0xLjQ2LS4xMS0uMDMtMTMuNDUtMy44LTExLjc2LTcgLjI4LS41NC43NS0uNzYgMS4zNC0uNzYgMi4zOCAwIDYuNyAzLjU0IDguNTcgMy41NC40MSAwIC43LS4xNy44My0uNi43OS0yLjg1LTEyLjA2LTQuMDUtMTAuOTgtOC4xNy4yLS43My43MS0xLjAyIDEuNDQtMS4wMiAzLjE0IDAgMTAuMiA1LjUzIDExLjY4IDUuNTMuMTEgMCAuMi0uMDMuMjQtLjEuNzQtMS4yLjMzLTIuMDQtNC45LTUuMi01LjIxLTMuMTYtOC44OC01LjA2LTYuOC03LjMzLjI0LS4yNi41OC0uMzggMS0uMzggMy4xNyAwIDEwLjY2IDYuODIgMTAuNjYgNi44MnMyLjAyIDIuMSAzLjI1IDIuMWMuMjggMCAuNTItLjEuNjgtLjM4Ljg2LTEuNDYtOC4wNi04LjIyLTguNTYtMTEuMDEtLjM0LTEuOS4yNC0yLjg1IDEuMzEtMi44NVoiLz48cGF0aCBmaWxsPSIjRkZEMjFFIiBkPSJNMzguNiA3Ni42OWMyLjc1LTQuMDQgMi41NS03LjA3LTEuMjItMTAuODQtMy43OC0zLjc3LTUuOTgtOS4zLTUuOTgtOS4zcy0uODItMy4yLTIuNjktMi45Yy0xLjg3LjMtMy4yNCA1LjA4LjY4IDguMDEgMy45MSAyLjkzLS43OCA0LjkyLTIuMjkgMi4xNy0xLjUtMi43NS01LjYyLTkuODItNy43Ni0xMS4xOC0yLjEzLTEuMzUtMy42My0uNi0zLjEzIDIuMi41IDIuNzkgOS40MyA5LjU1IDguNTYgMTEtLjg3IDEuNDctMy45My0xLjcxLTMuOTMtMS43MXMtOS41Ny04LjcxLTExLjY2LTYuNDRjLTIuMDggMi4yNyAxLjU5IDQuMTcgNi44IDcuMzMgNS4yMyAzLjE2IDUuNjQgNCA0LjkgNS4yLS43NSAxLjItMTIuMjgtOC41My0xMy4zNi00LjQtMS4wOCA0LjExIDExLjc3IDUuMyAxMC45OCA4LjE1LS44IDIuODUtOS4wNi01LjM4LTEwLjc0LTIuMTgtMS43IDMuMjEgMTEuNjUgNi45OCAxMS43NiA3LjAxIDQuMyAxLjEyIDE1LjI1IDMuNDkgMTkuMDgtMi4xMloiLz48cGF0aCBmaWxsPSIjRkY5RDBCIiBkPSJNNzcuNCA0OGMxLjYyIDAgMy4wNy42NiA0LjA3IDEuODdhNS45NyA1Ljk3IDAgMCAxIDEuMzMgMy43NiA3LjEgNy4xIDAgMCAxIDEuOTUtLjNjMS41NSAwIDIuOTUuNTkgMy45NCAxLjY2YTUuOCA1LjggMCAwIDEgLjggNyA1LjMgNS4zIDAgMCAxIDEuNzggMi44MmMuMjQuOS40OCAyLjgtLjggNC43NGE1LjIyIDUuMjIgMCAwIDEgLjM3IDUuMDJjLTEuMDIgMi4zMi0zLjU3IDQuMTQtOC41MSA2LjEtMy4wOCAxLjIyLTUuOSAyLTUuOTIgMi4wMWE0NC4zMyA0NC4zMyAwIDAgMS0xMC45MyAxLjZjLTUuODYgMC0xMC4wNS0xLjgtMTIuNDYtNS4zNC0zLjg4LTUuNjktMy4zMy0xMC45IDEuNy0xNS45MiAyLjc4LTIuNzggNC42My02Ljg3IDUuMDEtNy43Ny43OC0yLjY2IDIuODMtNS42MiA2LjI0LTUuNjJhNS43IDUuNyAwIDAgMSA0LjYgMi40NmMxLTEuMjYgMS45OC0yLjI1IDIuODctMi44MkE3LjQgNy40IDAgMCAxIDc3LjQgNDhabTAgNGMtLjUxIDAtMS4xMy4yMi0xLjgyLjY1LTIuMTMgMS4zNi02LjI1IDguNDMtNy43NiAxMS4xOGEyLjQzIDIuNDMgMCAwIDEtMi4xNCAxLjMxYy0xLjU0IDAtMi43NS0xLjUzLS4xNC0zLjQ4IDMuOTEtMi45MyAyLjU0LTcuNzIuNjctOC4wMWExLjU0IDEuNTQgMCAwIDAtLjI0LS4wMmMtMS43IDAtMi40NSAyLjkzLTIuNDUgMi45M3MtMi4yIDUuNTItNS45NyA5LjNjLTMuNzggMy43Ny0zLjk4IDYuOC0xLjIyIDEwLjgzIDEuODcgMi43NSA1LjQ3IDMuNTggOS4xNSAzLjU4IDMuODIgMCA3LjczLS45IDkuOTMtMS40Ni4xLS4wMyAxMy40NS0zLjggMTEuNzYtNy0uMjktLjU0LS43NS0uNzYtMS4zNC0uNzYtMi4zOCAwLTYuNzEgMy41NC04LjU3IDMuNTQtLjQyIDAtLjcxLS4xNy0uODMtLjYtLjgtMi44NSAxMi4wNS00LjA1IDEwLjk3LTguMTctLjE5LS43My0uNy0xLjAyLTEuNDQtMS4wMi0zLjE0IDAtMTAuMiA1LjUzLTExLjY4IDUuNTMtLjEgMC0uMTktLjAzLS4yMy0uMS0uNzQtMS4yLS4zNC0yLjA0IDQuODgtNS4yIDUuMjMtMy4xNiA4LjktNS4wNiA2LjgtNy4zMy0uMjMtLjI2LS41Ny0uMzgtLjk4LS4zOC0zLjE4IDAtMTAuNjcgNi44Mi0xMC42NyA2Ljgycy0yLjAyIDIuMS0zLjI0IDIuMWEuNzQuNzQgMCAwIDEtLjY4LS4zOGMtLjg3LTEuNDYgOC4wNS04LjIyIDguNTUtMTEuMDEuMzQtMS45LS4yNC0yLjg1LTEuMzEtMi44NVoiLz48cGF0aCBmaWxsPSIjRkZEMjFFIiBkPSJNNTYuMzMgNzYuNjljLTIuNzUtNC4wNC0yLjU2LTcuMDcgMS4yMi0xMC44NCAzLjc3LTMuNzcgNS45Ny05LjMgNS45Ny05LjNzLjgyLTMuMiAyLjctMi45YzEuODYuMyAzLjIzIDUuMDgtLjY4IDguMDEtMy45MiAyLjkzLjc4IDQuOTIgMi4yOCAyLjE3IDEuNTEtMi43NSA1LjYzLTkuODIgNy43Ni0xMS4xOCAyLjEzLTEuMzUgMy42NC0uNiAzLjEzIDIuMi0uNSAyLjc5LTkuNDIgOS41NS04LjU1IDExIC44NiAxLjQ3IDMuOTItMS43MSAzLjkyLTEuNzFzOS41OC04LjcxIDExLjY2LTYuNDRjMi4wOCAyLjI3LTEuNTggNC4xNy02LjggNy4zMy01LjIzIDMuMTYtNS42MyA0LTQuOSA1LjIuNzUgMS4yIDEyLjI4LTguNTMgMTMuMzYtNC40IDEuMDggNC4xMS0xMS43NiA1LjMtMTAuOTcgOC4xNS44IDIuODUgOS4wNS01LjM4IDEwLjc0LTIuMTggMS42OSAzLjIxLTExLjY1IDYuOTgtMTEuNzYgNy4wMS00LjMxIDEuMTItMTUuMjYgMy40OS0xOS4wOC0yLjEyWiIvPjwvc3ZnPg%3D%3D
[badge-v1]: https://img.shields.io/badge/Model-gipformer--65M--rnnt-blue?logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjQuNzUgMyA4NSA4NSIgZmlsbD0ibm9uZSI%2BPHBhdGggZmlsbD0iI0ZGRDIxRSIgZD0iTTQ3LjIxIDc2LjVhMzQuNzUgMzQuNzUgMCAxIDAgMC02OS41IDM0Ljc1IDM0Ljc1IDAgMCAwIDAgNjkuNVoiLz48cGF0aCBmaWxsPSIjRkY5RDBCIiBkPSJNODEuOTYgNDEuNzVhMzQuNzUgMzQuNzUgMCAxIDAtNjkuNSAwIDM0Ljc1IDM0Ljc1IDAgMCAwIDY5LjUgMFptLTczLjUgMGEzOC43NSAzOC43NSAwIDEgMSA3Ny41IDAgMzguNzUgMzguNzUgMCAwIDEtNzcuNSAwWiIvPjxwYXRoIGZpbGw9IiMzQTNCNDUiIGQ9Ik01OC41IDMyLjNjMS4yOC40NCAxLjc4IDMuMDYgMy4wNyAyLjM4YTUgNSAwIDEgMC02Ljc2LTIuMDdjLjYxIDEuMTUgMi41NS0uNzIgMy43LS4zMlpNMzQuOTUgMzIuM2MtMS4yOC40NC0xLjc5IDMuMDYtMy4wNyAyLjM4YTUgNSAwIDEgMSA2Ljc2LTIuMDdjLS42MSAxLjE1LTIuNTYtLjcyLTMuNy0uMzJaIi8%2BPHBhdGggZmlsbD0iI0ZGMzIzRCIgZD0iTTQ2Ljk2IDU2LjI5YzkuODMgMCAxMy04Ljc2IDEzLTEzLjI2IDAtMi4zNC0xLjU3LTEuNi00LjA5LS4zNi0yLjMzIDEuMTUtNS40NiAyLjc0LTguOSAyLjc0LTcuMTkgMC0xMy02Ljg4LTEzLTIuMzhzMy4xNiAxMy4yNiAxMyAxMy4yNloiLz48cGF0aCBmaWxsPSIjM0EzQjQ1IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zOS40MyA1NGE4LjcgOC43IDAgMCAxIDUuMy00LjQ5Yy40LS4xMi44MS41NyAxLjI0IDEuMjguNC42OC44MiAxLjM3IDEuMjQgMS4zNy40NSAwIC45LS42OCAxLjMzLTEuMzUuNDUtLjcuODktMS4zOCAxLjMyLTEuMjVhOC42MSA4LjYxIDAgMCAxIDUgNC4xN2MzLjczLTIuOTQgNS4xLTcuNzQgNS4xLTEwLjcgMC0yLjM0LTEuNTctMS42LTQuMDktLjM2bC0uMTQuMDdjLTIuMzEgMS4xNS01LjM5IDIuNjctOC43NyAyLjY3cy02LjQ1LTEuNTItOC43Ny0yLjY3Yy0yLjYtMS4yOS00LjIzLTIuMS00LjIzLjI5IDAgMy4wNSAxLjQ2IDguMDYgNS40NyAxMC45N1oiIGNsaXAtcnVsZT0iZXZlbm9kZCIvPjxwYXRoIGZpbGw9IiNGRjlEMEIiIGQ9Ik03MC43MSAzN2EzLjI1IDMuMjUgMCAxIDAgMC02LjUgMy4yNSAzLjI1IDAgMCAwIDAgNi41Wk0yNC4yMSAzN2EzLjI1IDMuMjUgMCAxIDAgMC02LjUgMy4yNSAzLjI1IDAgMCAwIDAgNi41Wk0xNy41MiA0OGMtMS42MiAwLTMuMDYuNjYtNC4wNyAxLjg3YTUuOTcgNS45NyAwIDAgMC0xLjMzIDMuNzYgNy4xIDcuMSAwIDAgMC0xLjk0LS4zYy0xLjU1IDAtMi45NS41OS0zLjk0IDEuNjZhNS44IDUuOCAwIDAgMC0uOCA3IDUuMyA1LjMgMCAwIDAtMS43OSAyLjgyYy0uMjQuOS0uNDggMi44LjggNC43NGE1LjIyIDUuMjIgMCAwIDAtLjM3IDUuMDJjMS4wMiAyLjMyIDMuNTcgNC4xNCA4LjUyIDYuMSAzLjA3IDEuMjIgNS44OSAyIDUuOTEgMi4wMWE0NC4zMyA0NC4zMyAwIDAgMCAxMC45MyAxLjZjNS44NiAwIDEwLjA1LTEuOCAxMi40Ni01LjM0IDMuODgtNS42OSAzLjMzLTEwLjktMS43LTE1LjkyLTIuNzctMi43OC00LjYyLTYuODctNS03Ljc3LS43OC0yLjY2LTIuODQtNS42Mi02LjI1LTUuNjJhNS43IDUuNyAwIDAgMC00LjYgMi40NmMtMS0xLjI2LTEuOTgtMi4yNS0yLjg2LTIuODJBNy40IDcuNCAwIDAgMCAxNy41MiA0OFptMCA0Yy41MSAwIDEuMTQuMjIgMS44Mi42NSAyLjE0IDEuMzYgNi4yNSA4LjQzIDcuNzYgMTEuMTguNS45MiAxLjM3IDEuMzEgMi4xNCAxLjMxIDEuNTUgMCAyLjc1LTEuNTMuMTUtMy40OC0zLjkyLTIuOTMtMi41NS03LjcyLS42OC04LjAxLjA4LS4wMi4xNy0uMDIuMjQtLjAyIDEuNyAwIDIuNDUgMi45MyAyLjQ1IDIuOTNzMi4yIDUuNTIgNS45OCA5LjNjMy43NyAzLjc3IDMuOTcgNi44IDEuMjIgMTAuODMtMS44OCAyLjc1LTUuNDcgMy41OC05LjE2IDMuNTgtMy44MSAwLTcuNzMtLjktOS45Mi0xLjQ2LS4xMS0uMDMtMTMuNDUtMy44LTExLjc2LTcgLjI4LS41NC43NS0uNzYgMS4zNC0uNzYgMi4zOCAwIDYuNyAzLjU0IDguNTcgMy41NC40MSAwIC43LS4xNy44My0uNi43OS0yLjg1LTEyLjA2LTQuMDUtMTAuOTgtOC4xNy4yLS43My43MS0xLjAyIDEuNDQtMS4wMiAzLjE0IDAgMTAuMiA1LjUzIDExLjY4IDUuNTMuMTEgMCAuMi0uMDMuMjQtLjEuNzQtMS4yLjMzLTIuMDQtNC45LTUuMi01LjIxLTMuMTYtOC44OC01LjA2LTYuOC03LjMzLjI0LS4yNi41OC0uMzggMS0uMzggMy4xNyAwIDEwLjY2IDYuODIgMTAuNjYgNi44MnMyLjAyIDIuMSAzLjI1IDIuMWMuMjggMCAuNTItLjEuNjgtLjM4Ljg2LTEuNDYtOC4wNi04LjIyLTguNTYtMTEuMDEtLjM0LTEuOS4yNC0yLjg1IDEuMzEtMi44NVoiLz48cGF0aCBmaWxsPSIjRkZEMjFFIiBkPSJNMzguNiA3Ni42OWMyLjc1LTQuMDQgMi41NS03LjA3LTEuMjItMTAuODQtMy43OC0zLjc3LTUuOTgtOS4zLTUuOTgtOS4zcy0uODItMy4yLTIuNjktMi45Yy0xLjg3LjMtMy4yNCA1LjA4LjY4IDguMDEgMy45MSAyLjkzLS43OCA0LjkyLTIuMjkgMi4xNy0xLjUtMi43NS01LjYyLTkuODItNy43Ni0xMS4xOC0yLjEzLTEuMzUtMy42My0uNi0zLjEzIDIuMi41IDIuNzkgOS40MyA5LjU1IDguNTYgMTEtLjg3IDEuNDctMy45My0xLjcxLTMuOTMtMS43MXMtOS41Ny04LjcxLTExLjY2LTYuNDRjLTIuMDggMi4yNyAxLjU5IDQuMTcgNi44IDcuMzMgNS4yMyAzLjE2IDUuNjQgNCA0LjkgNS4yLS43NSAxLjItMTIuMjgtOC41My0xMy4zNi00LjQtMS4wOCA0LjExIDExLjc3IDUuMyAxMC45OCA4LjE1LS44IDIuODUtOS4wNi01LjM4LTEwLjc0LTIuMTgtMS43IDMuMjEgMTEuNjUgNi45OCAxMS43NiA3LjAxIDQuMyAxLjEyIDE1LjI1IDMuNDkgMTkuMDgtMi4xMloiLz48cGF0aCBmaWxsPSIjRkY5RDBCIiBkPSJNNzcuNCA0OGMxLjYyIDAgMy4wNy42NiA0LjA3IDEuODdhNS45NyA1Ljk3IDAgMCAxIDEuMzMgMy43NiA3LjEgNy4xIDAgMCAxIDEuOTUtLjNjMS41NSAwIDIuOTUuNTkgMy45NCAxLjY2YTUuOCA1LjggMCAwIDEgLjggNyA1LjMgNS4zIDAgMCAxIDEuNzggMi44MmMuMjQuOS40OCAyLjgtLjggNC43NGE1LjIyIDUuMjIgMCAwIDEgLjM3IDUuMDJjLTEuMDIgMi4zMi0zLjU3IDQuMTQtOC41MSA2LjEtMy4wOCAxLjIyLTUuOSAyLTUuOTIgMi4wMWE0NC4zMyA0NC4zMyAwIDAgMS0xMC45MyAxLjZjLTUuODYgMC0xMC4wNS0xLjgtMTIuNDYtNS4zNC0zLjg4LTUuNjktMy4zMy0xMC45IDEuNy0xNS45MiAyLjc4LTIuNzggNC42My02Ljg3IDUuMDEtNy43Ny43OC0yLjY2IDIuODMtNS42MiA2LjI0LTUuNjJhNS43IDUuNyAwIDAgMSA0LjYgMi40NmMxLTEuMjYgMS45OC0yLjI1IDIuODctMi44MkE3LjQgNy40IDAgMCAxIDc3LjQgNDhabTAgNGMtLjUxIDAtMS4xMy4yMi0xLjgyLjY1LTIuMTMgMS4zNi02LjI1IDguNDMtNy43NiAxMS4xOGEyLjQzIDIuNDMgMCAwIDEtMi4xNCAxLjMxYy0xLjU0IDAtMi43NS0xLjUzLS4xNC0zLjQ4IDMuOTEtMi45MyAyLjU0LTcuNzIuNjctOC4wMWExLjU0IDEuNTQgMCAwIDAtLjI0LS4wMmMtMS43IDAtMi40NSAyLjkzLTIuNDUgMi45M3MtMi4yIDUuNTItNS45NyA5LjNjLTMuNzggMy43Ny0zLjk4IDYuOC0xLjIyIDEwLjgzIDEuODcgMi43NSA1LjQ3IDMuNTggOS4xNSAzLjU4IDMuODIgMCA3LjczLS45IDkuOTMtMS40Ni4xLS4wMyAxMy40NS0zLjggMTEuNzYtNy0uMjktLjU0LS43NS0uNzYtMS4zNC0uNzYtMi4zOCAwLTYuNzEgMy41NC04LjU3IDMuNTQtLjQyIDAtLjcxLS4xNy0uODMtLjYtLjgtMi44NSAxMi4wNS00LjA1IDEwLjk3LTguMTctLjE5LS43My0uNy0xLjAyLTEuNDQtMS4wMi0zLjE0IDAtMTAuMiA1LjUzLTExLjY4IDUuNTMtLjEgMC0uMTktLjAzLS4yMy0uMS0uNzQtMS4yLS4zNC0yLjA0IDQuODgtNS4yIDUuMjMtMy4xNiA4LjktNS4wNiA2LjgtNy4zMy0uMjMtLjI2LS41Ny0uMzgtLjk4LS4zOC0zLjE4IDAtMTAuNjcgNi44Mi0xMC42NyA2Ljgycy0yLjAyIDIuMS0zLjI0IDIuMWEuNzQuNzQgMCAwIDEtLjY4LS4zOGMtLjg3LTEuNDYgOC4wNS04LjIyIDguNTUtMTEuMDEuMzQtMS45LS4yNC0yLjg1LTEuMzEtMi44NVoiLz48cGF0aCBmaWxsPSIjRkZEMjFFIiBkPSJNNTYuMzMgNzYuNjljLTIuNzUtNC4wNC0yLjU2LTcuMDcgMS4yMi0xMC44NCAzLjc3LTMuNzcgNS45Ny05LjMgNS45Ny05LjNzLjgyLTMuMiAyLjctMi45YzEuODYuMyAzLjIzIDUuMDgtLjY4IDguMDEtMy45MiAyLjkzLjc4IDQuOTIgMi4yOCAyLjE3IDEuNTEtMi43NSA1LjYzLTkuODIgNy43Ni0xMS4xOCAyLjEzLTEuMzUgMy42NC0uNiAzLjEzIDIuMi0uNSAyLjc5LTkuNDIgOS41NS04LjU1IDExIC44NiAxLjQ3IDMuOTItMS43MSAzLjkyLTEuNzFzOS41OC04LjcxIDExLjY2LTYuNDRjMi4wOCAyLjI3LTEuNTggNC4xNy02LjggNy4zMy01LjIzIDMuMTYtNS42MyA0LTQuOSA1LjIuNzUgMS4yIDEyLjI4LTguNTMgMTMuMzYtNC40IDEuMDggNC4xMS0xMS43NiA1LjMtMTAuOTcgOC4xNS44IDIuODUgOS4wNS01LjM4IDEwLjc0LTIuMTggMS42OSAzLjIxLTExLjY1IDYuOTgtMTEuNzYgNy4wMS00LjMxIDEuMTItMTUuMjYgMy40OS0xOS4wOC0yLjEyWiIvPjwvc3ZnPg%3D%3D
