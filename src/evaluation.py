import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def evaluate_classifier(model, x_test, y_test) -> dict:
    predictions = model.predict(x_test)
    return {
        'accuracy': accuracy_score(y_test, predictions),
        'classification_report': classification_report(y_test, predictions, output_dict=True),
        'confusion_matrix': confusion_matrix(y_test, predictions),
    }


def feature_importance_table(model, feature_columns: list[str]) -> pd.DataFrame:
    if not hasattr(model, 'feature_importances_'):
        raise ValueError('Model does not expose feature_importances_.')
    return pd.DataFrame({'feature': feature_columns, 'importance': model.feature_importances_}).sort_values('importance', ascending=False).reset_index(drop=True)
