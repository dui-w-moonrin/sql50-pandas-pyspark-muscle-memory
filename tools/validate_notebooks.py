import json
import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = [
    "# 0. Problem",
    "# 1. Setup",
    "# 2. SQL Solution",
    "# 3. pandas Solution",
    "# 4. PySpark Solution",
    "# 5. Pattern Mapping",
    "# 6. Muscle-Memory Round",
]
TRAINING_FILE_RE = re.compile(r"^\d{2}_\d+_.+\.ipynb$")


def _cell_text(cell: dict) -> str:
    source = cell.get("source", [])
    return "".join(source) if isinstance(source, list) else str(source)


def discover_training_notebooks(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.ipynb") if TRAINING_FILE_RE.match(p.name))


def validate_notebook(path: Path) -> list[str]:
    errors = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"{path}: invalid JSON: {exc}"]

    if notebook.get("nbformat") != 4:
        errors.append(f"{path}: nbformat must be 4")

    cells = notebook.get("cells", [])
    all_text = "\n".join(_cell_text(c) for c in cells)
    for heading in REQUIRED_HEADINGS:
        if heading not in all_text:
            errors.append(f"{path}: missing heading {heading}")

    idx = next(
        (i for i, c in enumerate(cells) if "# 6. Muscle-Memory Round" in _cell_text(c)),
        None,
    )
    if idx is not None:
        text = "\n".join(_cell_text(c) for c in cells[idx + 1 :])
        forbidden = [
            r"\bSELECT\s+.+\bFROM\b",
            r"\bresult\s*=",
            r"\.filter\s*\(",
            r"\.groupBy\s*\(",
            r"\.merge\s*\(",
        ]
        if any(re.search(pattern, text, re.I | re.S) for pattern in forbidden):
            errors.append(f"{path}: Muscle-Memory section contains solution-like code")

    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    notebooks = discover_training_notebooks(root)
    errors = [e for path in notebooks for e in validate_notebook(path)]

    for error in errors:
        print(error)

    print(f"Checked {len(notebooks)} notebook(s); {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
