import pandas as pd


def assign_epoch(df: pd.DataFrame, time_col: str = 'time_sec', epoch_sec: int = 30) -> pd.DataFrame:
    output = df.copy()
    output['epoch'] = (output[time_col] // epoch_sec).astype(int)
    return output


def test_assign_epoch_creates_epoch_column():
    df = pd.DataFrame({'time_sec': [0, 29, 30, 61]})
    output = assign_epoch(df)

    assert 'epoch' in output.columns
    assert output['epoch'].tolist() == [0, 0, 1, 2]
