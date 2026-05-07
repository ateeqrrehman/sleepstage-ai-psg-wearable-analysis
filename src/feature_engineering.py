import numpy as np
import pandas as pd

from src.preprocessing import assign_epoch


def build_heart_rate_features(heart_rate: pd.DataFrame) -> pd.DataFrame:
    hr = assign_epoch(heart_rate)
    return (
        hr.groupby('epoch')['bpm']
        .agg(hr_mean='mean', hr_std='std', hr_min='min', hr_max='max')
        .reset_index()
    )


def build_motion_features(motion: pd.DataFrame) -> pd.DataFrame:
    mot = motion.copy()
    mot['motion_magnitude'] = np.sqrt(mot['ax'] ** 2 + mot['ay'] ** 2 + mot['az'] ** 2)
    mot = assign_epoch(mot)

    return (
        mot.groupby('epoch')['motion_magnitude']
        .agg(motion_mean='mean', motion_std='std', motion_min='min', motion_max='max')
        .reset_index()
    )
