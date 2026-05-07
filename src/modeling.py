from dataclasses import dataclass

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


@dataclass
class TrainTestData:
    x_train: pd.DataFrame
    x_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series


def split_dataset(df: pd.DataFrame, feature_columns: list[str], target_column: str = 'stage', test_size: float = 0.2, random_state: int = 42) -> TrainTestData:
    x = df[feature_columns]
    y = df[target_column]

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y if y.nunique() > 1 else None,
    )

    return TrainTestData(x_train, x_test, y_train, y_test)


def train_random_forest(x_train, y_train, random_state: int = 42) -> RandomForestClassifier:
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=random_state,
        class_weight='balanced',
    )
    model.fit(x_train, y_train)
    return model


def train_logistic_regression(x_train, y_train):
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)

    model = LogisticRegression(
        max_iter=1000,
        class_weight='balanced',
        multi_class='auto',
    )

    model.fit(x_train_scaled, y_train)

    return model, scaler
