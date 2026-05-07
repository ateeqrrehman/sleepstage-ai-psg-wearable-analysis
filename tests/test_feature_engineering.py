import pandas as pd

from src.feature_engineering import build_heart_rate_features


def test_build_heart_rate_features_returns_expected_columns():
    df = pd.DataFrame(
        {
            'time_sec': [0, 10, 35, 45],
            'bpm': [60, 65, 70, 72],
        }
    )

    features = build_heart_rate_features(df)

    assert 'hr_mean' in features.columns
    assert 'hr_std' in features.columns
