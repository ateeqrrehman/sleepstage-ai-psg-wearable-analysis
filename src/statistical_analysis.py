import pandas as pd
from scipy import stats


def compare_feature_by_stage(df: pd.DataFrame, feature: str, stage_a: int, stage_b: int, target_col: str = 'stage') -> dict:
    group_a = df[df[target_col] == stage_a][feature].dropna()
    group_b = df[df[target_col] == stage_b][feature].dropna()

    statistic, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)

    return {
        'feature': feature,
        'stage_a': stage_a,
        'stage_b': stage_b,
        'statistic': statistic,
        'p_value': p_value,
    }


def correlation_matrix(df: pd.DataFrame, feature_columns: list[str]) -> pd.DataFrame:
    return df[feature_columns].corr()
