# DL-Eng: Deep Learning Research & Engineering

`dl-eng` is a modular scaffold for deep learning research and engineering. It targets modern deep learning systems such as transformers, diffusion models, representation learning, and broader generative modeling workflows. The goal is to provide minimum, extensible abstractions for models, learners, and inference — bridging research prototyping and production-ready engineering.

---

## 🏗 Project Architecture

```text
dl-eng/
├── dl_eng/                     # core Python package
│   ├── interfaces/             # contracts between subsystems
│   ├── models/                 # model families and builders
│   ├── learners/               # optimization and training logic
│   ├── inference/              # sampling and inference orchestration
│   └── data/                   # batches, datasets, and loaders
├── experiments/                # experiment-local code, configs, and runtime artifacts
│   └── <project>/
│       ├── config.yaml         # top-level configuration for the project
│       ├── train.py            # script for training models
│       ├── eval.py             # script for evaluating trained models
│       └── runs/               # directory for individual run artifacts
│           └── <run_id>        # e.g., f"{config.name}_{yyyymmdd}_{timestamp}_s{config.seed}_g{git_hash}"
│               ├── config.yaml
│               ├── train_metrics.csv
│               ├── eval_metrics.csv
│               ├── train_curve.png
│               ├── eval_curve.png
│               └── checkpoints/
├── exports/                    # promoted model exports
│   └── <project_v0.x>/         # e.g., 'diffusion_v0.1'
│       ├── config.yaml
│       ├── export_metadata.yaml
│       └── checkpoints/
├── notebooks/
├── scripts/                    # utility scripts (promotion, plotting)
├── tests/
├── pyproject.toml
└── README.md
```

### Mental Model
```text
                ┌──────────────────┐
                │   experiments    │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │    learners      │  training loop + metrics
                └────────┬─────────┘
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
        data           models       inference
          ↓              ↓              ↓
                  interfaces / config
```

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/bowen0701/dl-eng.git
cd dl-eng
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e .
python -m pip install pytest
```

### 1. Training & Evaluation
Train a model for a given project. This creates a new directory under `experiments/<project>/runs/`.
```bash
python3 -m experiments.<project>.train --epochs 100 --seed 42
```
Evaluate a trained run using its `run_id`:
```bash
python3 -m experiments.<project>.eval --run_id <run_id>
```
Training writes per-run outputs under `experiments/<project>/runs/<run_id>/`, including `config.yaml`, `train_metrics.csv`, `eval_metrics.csv`, `train_curve.png`, `eval_curve.png`, and `checkpoints/`.

Run the automated test suite:
```bash
python3 -m pytest tests
```

### 2. Promoting to Exports
Once a run is ready for reuse, promote it into the exports bucket. This automates versioning and metadata generation:
```bash
python3 scripts/promote_run_to_export.py --run_id <run_id> --version 0.1
```
Artifacts will be stored in `exports/<project_v0.x>/`.

### 3. Plotting Learning Curves
Generate training and evaluation plots from a saved run:
```bash
python3 scripts/plot_learning_curves.py --run_id <run_id>
```
Reads `train_metrics.csv` and `eval_metrics.csv` from the run directory and writes `train_curve.png` and `eval_curve.png` back in place.

## 🛠 Engineering Standards
- **Linting / Formatting**: Managed via `ruff`.
- **Configuration**: Type-safe experiment configs using `dataclasses`.
- **Reproducibility**: Every run is stamped with date, timestamp, seed, and git hash.
- **Naming**: Prefer explicit, qualified names (e.g., `tests/test_diffusion_learner.py` over `test_learner.py`).

## 🗺 Roadmap
- TBD
