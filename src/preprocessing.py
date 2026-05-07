import pandas as pd


def assign_epoch(df: pd.DataFrame, time_col: str = 'time_sec', epoch_sec: int = 30) -> pd.DataFrame:
    output = df.copy()
    output['epoch'] = (output[time_col] // epoch_sec).astype(int)
    return output


def clean_sleep_labels(labels: pd.DataFrame) -> pd.DataFrame:
    output = labels.copy()
    output = output.dropna(subset=['time_sec', 'stage'])
    output['stage'] = output['stage'].astype(int)
    return assign_epoch(output)
