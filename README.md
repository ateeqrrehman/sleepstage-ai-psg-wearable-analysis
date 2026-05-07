# SleepStage AI: PSG-Aligned Wearable Signal Modeling for Sleep Stage Classification

**SleepStage AI** is a research-oriented machine learning project for classifying sleep stages using wearable physiological signals aligned with polysomnography-labeled sleep-stage epochs. The project uses heart rate, wrist accelerometry, and step-count streams from the PhysioNet Sleep-Accel dataset to build an end-to-end ML workflow for data ingestion, 30-second epoch alignment, physiological feature engineering, statistical analysis, dimensionality reduction, supervised classification, model evaluation, and reproducible experimentation.

The project investigates how AI can extract meaningful sleep-stage structure from synchronized wearable signals and establish a foundation for future multimodal PSG and wearable sleep modeling.

---

## Research Question

Can machine learning classify sleep stages from synchronized wearable streams aligned to PSG stage labels, and can these signals reveal physiological structure that supports multimodal sleep-study interpretation?

---

## Problem Context

Polysomnography is the gold-standard clinical method for studying sleep. A PSG study records multiple physiological signals, including brain activity, eye movement, muscle tone, airflow, oxygen saturation, ECG, heart rate, and body movement. In practice, many scoring workflows focus on a smaller subset of manually interpreted channels.

This project explores whether AI can use synchronized wearable signals such as heart rate, wrist movement, and steps to identify sleep-stage structure. The work focuses on PSG-aligned wearable modeling as a practical first step toward broader AI-enhanced sleep-study interpretation, latent biomarker discovery, and more comprehensive physiological signal analysis.

---

## Dataset

This project uses the PhysioNet dataset **Motion and heart rate from a wrist worn wearable and labeled sleep from polysomnography** by Walch et al.

Dataset source: https://physionet.org/content/sleep-accel/1.0.0/

Each subject includes synchronized files for:

- PSG sleep-stage labels
- Heart rate
- Wrist accelerometry
- Step count

Sleep-stage labels are represented as 30-second epochs with classes including Wake, N1, N2, N3, and REM. The dataset is suitable for epoch-level supervised learning and physiological pattern analysis.

---

## Variables and Modeling Target

| Category | Variables |
|---|---|
| Input signals | Heart rate, wrist acceleration, step count, derived motion magnitude |
| Engineered features | Heart-rate statistics, motion statistics, step aggregates, epoch-level feature summaries |
| Target label | PSG sleep-stage label per 30-second epoch |
| Modeling task | Multi-class sleep-stage classification |

Potential confounders include subject-level physiology, age, sex, health status, medication use, caffeine, and sleep-lab conditions. The project design emphasizes subject-aware evaluation, within-subject normalization, and careful interpretation of wearable-only signals.

---

## Hypothesis

Different sleep stages produce distinguishable physiological patterns across wearable signals. Deep sleep may show reduced movement and lower autonomic variability, REM may show characteristic autonomic fluctuation, and wakefulness may show higher activity. A supervised model trained on PSG-aligned wearable features should learn meaningful sleep-stage structure above chance-level prediction and support interpretation of latent physiological patterns.

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

The repository includes modular source code, dependency specifications, documentation, testing, and CI validation. Reproducibility is supported through:

- Public PhysioNet dataset access
- Subject-level ingestion utilities
- Deterministic model random states where applicable
- Documented preprocessing and feature-engineering logic
- Research notebook for traceability
- Reusable Python modules for pipeline execution

---

## Ethics and Clinical Scope

This project is a research prototype for physiological signal analysis and sleep-stage classification. It is not a clinical diagnostic system, medical device, or substitute for professional sleep-medicine interpretation.

Physiological data can encode sensitive behavioral and health-related patterns. Model outputs should be interpreted as research signals requiring validation, not as clinical conclusions.

---

## Future Research Directions

Planned research extensions include:

- Subject-wise train/test splits to reduce leakage across individuals
- Expanded multi-subject evaluation
- Class-imbalance analysis across sleep stages
- Additional time-series features such as rolling heart-rate variability and motion entropy
- Deep learning baselines for temporal modeling
- Model calibration and uncertainty estimation
- Broader multimodal integration with PSG signal channels
- Deployment-oriented API prototype for research demonstration
