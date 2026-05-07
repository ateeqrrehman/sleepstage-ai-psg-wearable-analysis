import io
from dataclasses import dataclass

import pandas as pd
import requests

BASE_URL = 'https://physionet.org/files/sleep-accel/1.0.0/'
DEFAULT_SUBJECT_ID = '1066528'
SEPARATOR = r'[,\s]+'


@dataclass
class SubjectStreams:
    labels: pd.DataFrame
    heart_rate: pd.DataFrame
    motion: pd.DataFrame
    steps: pd.DataFrame | None


def fetch_text(url: str, timeout: int = 60) -> str:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def build_subject_urls(subject_id: str, base_url: str = BASE_URL) -> dict[str, str]:
    return {
        'labels': base_url + 'labels/' + subject_id + '_labeled_sleep.txt',
        'heart_rate': base_url + 'heart_rate/' + subject_id + '_heartrate.txt',
        'motion': base_url + 'motion/' + subject_id + '_acceleration.txt',
        'steps': base_url + 'steps/' + subject_id + '_steps.txt',
    }


def read_table(text: str, names: list[str]) -> pd.DataFrame:
    return pd.read_csv(io.StringIO(text), sep=SEPARATOR, header=None, names=names, engine='python')


def load_subject_streams(subject_id: str = DEFAULT_SUBJECT_ID) -> SubjectStreams:
    urls = build_subject_urls(subject_id)
    labels = read_table(fetch_text(urls['labels']), ['time_sec', 'stage'])
    heart_rate = read_table(fetch_text(urls['heart_rate']), ['time_sec', 'bpm'])
    motion = read_table(fetch_text(urls['motion']), ['time_sec', 'ax', 'ay', 'az'])
    try:
        steps = read_table(fetch_text(urls['steps']), ['time_sec', 'steps'])
    except requests.HTTPError:
        steps = None
    return SubjectStreams(labels=labels, heart_rate=heart_rate, motion=motion, steps=steps)
