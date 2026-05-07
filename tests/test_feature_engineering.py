import pandas as pd



def assign_epoch(df: pd.DataFrame, time_col: str = 'time_sec', epoch_sec: int = 30) -> pd.DataFrame:
    output = df.copy()
    output['epoch'] = (output[time_col] // epoch_sec).astype(int)
    return output



def build_heart_rate_features(heart_rate: pd.DataFrame) -> pd.DataFrame:
    hr = assign_epoch(heart_rate)
    return (
        hr.groupby('epoch')['bpm']
        .agg(hr_mean='mean', hr_std='std', hr_min='min', hr_max='max')
        .reset_index()
    )



def test_build_heart_rate_features_returns_expected_columns():
    df = pd.DataFrame({
        'time_sec': [0, 10, 35, 45],
        'bpm': [60, 65, 70, 72],
    })

    features = build_heart_rate_features(df)

    assert 'hr_mean' in features.columns
    assert 'hr_std' in features.columns
