from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.preprocessing import assign_epoch


def test_assign_epoch_creates_epoch_column():
    df = pd.DataFrame({'time_sec': [0, 29, 30, 61]})
    output = assign_epoch(df)

    assert 'epoch' in output.columns
    assert output['epoch'].tolist() == [0, 0, 1, 2]
