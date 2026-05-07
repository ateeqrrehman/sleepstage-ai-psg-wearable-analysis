# SleepStage AI: Polysomnography-Aligned Wearable Signal Modeling for Sleep Stage Classification

**SleepStage AI** is a research-oriented machine learning project for classifying sleep stages using wearable physiological signals aligned with polysomnography-labeled sleep-stage epochs. The project uses heart rate, wrist accelerometry, and step-count streams from the PhysioNet Sleep-Accel dataset to build an end-to-end workflow for ingestion, cleaning, 30-second epoch alignment, feature engineering, exploratory analysis, statistical testing, dimensionality reduction, supervised classification, and model evaluation.

This repository is structured as a professional ML research and engineering project rather than a single notebook. The notebook remains available as a research walkthrough, while reusable pipeline logic is organized into modular Python files under `src/`.

---

## Research Question

Can machine learning classify sleep stages from synchronized wearable streams aligned to PSG stage labels, and can these signals reveal meaningful physiological structure that supports future multimodal PSG and wearable sleep modeling?

---

## Problem Context

Polysomnography is the gold-standard clinical method for studying sleep. A PSG study records multiple physiological signals, but many clinical workflows rely on a subset of manually interpreted channels. This project explores whether AI can use wearable signals aligned with PSG labels to identify sleep-stage structure and support deeper interpretation of sleep-study data.

The current implementation focuses on wearable signals and PSG labels as a first step toward broader multimodal sleep-study modeling.

---

## Dataset

This project uses the PhysioNet dataset **Motion and heart rate from a wrist worn wearable and labeled sleep from polysomnography** by Walch et al.

Dataset source: https://physionet.org/content/sleep-accel/1.0.0/

Each subject includes synchronized files for:

- PSG sleep-stage labels
- Heart rate
- Wrist accelerometry
- Step count

Sleep-stage labels are represented as 30-second epochs, which makes the dataset suitable for epoch-level classification.

---

## Methodology

The project workflow includes:

1. Data ingestion from PhysioNet subject-level text files
2. Parsing PSG labels, heart rate, acceleration, and steps
3. Cleaning and timestamp handling
4. 30-second epoch assignment
5. Heart-rate feature engineering
6. Motion-magnitude feature engineering
7. Step-count aggregation
8. Feature alignment with PSG sleep-stage labels
9. Exploratory visualization and PCA
10. Statistical comparison across sleep stages
11. Random Forest classification
12. Logistic Regression baseline modeling
13. Confusion matrix and classification-report evaluation
14. Feature-importance interpretation

---

## Repository Structure

```text
.
├── notebooks/
│   └── sleepstage_ai_psg_wearable_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── data_ingestion.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── statistical_analysis.py
│   ├── modeling.py
│   ├── evaluation.py
│   └── visualization.py
├── docs/
│   ├── research_report.md
│   ├── model_card.md
│   ├── data_card.md
│   ├── ethics_privacy.md
│   └── reproducibility.md
├── results/
│   ├── figures/
│   ├── metrics/
│   └── reports/
├── tests/
│   ├── test_preprocessing.py
│   └── test_feature_engineering.py
├── .github/workflows/
│   └── ci.yml
├── README.md
├── requirements.txt
├── .gitignore
└── CITATION.cff
```

---

## Technical Stack

| Area | Tools |
|---|---|
| Programming | Python |
| Data Processing | pandas, NumPy |
| Statistical Analysis | SciPy |
| Machine Learning | scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Notebook Workflow | Google Colab / Jupyter |
| CI/CD | GitHub Actions |
| Testing | pytest |

---

## Model Development

The project includes two supervised learning approaches:

- **Random Forest Classifier** for nonlinear tabular feature modeling and feature-importance analysis
- **Logistic Regression Baseline** for interpretable baseline comparison after feature scaling

Model evaluation focuses on:

- Accuracy
- Confusion matrix
- Classification report
- Per-class precision, recall, and F1-score
- Feature importance
- PCA-based structure exploration

---

## Reproducibility

The repository includes a modular source-code structure, requirements file, documentation, and CI workflow. Reproducibility is supported through:

- Public PhysioNet dataset access
- Subject-level data ingestion utilities
- Deterministic model random states where applicable
- Documented preprocessing and feature-engineering logic
- Notebook walkthrough for research traceability
- Source modules for reusable execution

---

## Important Scope Note

This project is a research prototype for physiological signal analysis and sleep-stage classification. It is **not** a clinical diagnostic system, medical device, or substitute for professional sleep-medicine interpretation.

---

## Future Work

Planned extensions include:

- Subject-wise train/test splits to reduce leakage across individuals
- Expanded multi-subject evaluation
- Class-imbalance analysis across sleep stages
- Additional time-series features such as rolling heart-rate variability and motion entropy
- Deep learning baselines for temporal modeling
- Model calibration and uncertainty estimation
- Broader multimodal integration with PSG signal channels
- Deployment-oriented API prototype for research demonstration
