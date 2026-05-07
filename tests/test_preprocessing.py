import pandas as pd

from src.preprocessing import assign_epoch


def test_assign_epoch_creates_epoch_column():
    df = pd.DataFrame({'time_sec': [0, 29, 30, 61]})
    output = assign_epoch(df)

    assert 'epoch' in output.columns
    assert output['epoch'].tolist() == [0, 0, 1, 2]
