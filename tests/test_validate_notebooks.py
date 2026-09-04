import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.validate_notebooks import discover_training_notebooks, validate_notebook


def test_repository_contains_exactly_50_training_notebooks():
    notebooks = discover_training_notebooks(ROOT)
    assert len(notebooks) == 50


def test_sequence_is_exactly_01_through_50():
    notebooks = discover_training_notebooks(ROOT)
    sequences = sorted(int(path.name[:2]) for path in notebooks)
    assert sequences == list(range(1, 51))


def test_all_notebooks_follow_contract():
    errors = [
        error
        for path in discover_training_notebooks(ROOT)
        for error in validate_notebook(path)
    ]
    assert errors == []


def test_all_notebooks_are_valid_json():
    for path in discover_training_notebooks(ROOT):
        json.loads(path.read_text(encoding="utf-8"))
