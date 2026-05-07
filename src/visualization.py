import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler


def plot_stage_distribution(df: pd.DataFrame, target_col: str = 'stage'):
    ax = df[target_col].value_counts().sort_index().plot(kind='bar')
    ax.set_title('Sleep Stage Distribution')
    ax.set_xlabel('Sleep Stage')
    ax.set_ylabel('Epoch Count')
    plt.tight_layout()
    return ax


def compute_pca_projection(df: pd.DataFrame, feature_columns: list[str]) -> pd.DataFrame:
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(df[feature_columns])

    pca = PCA(n_components=2)
    components = pca.fit_transform(x_scaled)

    return pd.DataFrame(
        {
            'pc1': components[:, 0],
            'pc2': components[:, 1],
            'stage': df['stage'].values,
        }
    )


def plot_confusion_matrix(confusion_matrix, labels=None):
    display = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=labels)
    display.plot()
    plt.tight_layout()
    return display
