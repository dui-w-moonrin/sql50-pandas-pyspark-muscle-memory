import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.validate_notebooks import discover_training_notebooks, validate_notebook


def test_day1_contains_ten_notebooks():
    notebooks = discover_training_notebooks(ROOT)
    assert len(notebooks) == 10


def test_day1_notebooks_follow_contract():
    errors = [
        error
        for path in discover_training_notebooks(ROOT)
        for error in validate_notebook(path)
    ]
    assert errors == []


def test_day1_canonical_sequences():
    sequences = sorted(int(path.name[:2]) for path in discover_training_notebooks(ROOT))
    assert sequences == [1, 2, 5, 6, 13, 15, 17, 20, 27, 47]


def test_all_notebooks_are_valid_json():
    for path in discover_training_notebooks(ROOT):
        json.loads(path.read_text(encoding="utf-8"))
