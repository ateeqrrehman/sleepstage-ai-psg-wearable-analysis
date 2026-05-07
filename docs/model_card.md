# Model Card

## Models

- Random Forest Classifier
- Logistic Regression Baseline

## Inputs

- Heart-rate statistics
- Motion-magnitude statistics
- Step-count aggregates

## Outputs

Predicted sleep-stage labels aligned to PSG epochs.

## Intended Use

Research-oriented physiological signal analysis and sleep-stage classification.

## Limitations

- Limited subject-scale evaluation
- Wearable-only signal scope
- Potential subject leakage without subject-wise splitting
- Not validated for clinical deployment
