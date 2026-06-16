"""Rank creator/content signals for brief generation."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


def score_signal(row: dict) -> float:
    momentum = float(row.get("momentum", 0))
    relevance = float(row.get("relevance", 0))
    saturation = float(row.get("saturation", 0))
    effort = float(row.get("effort", 0))
    raw = (momentum * 0.35) + (relevance * 0.35) + ((1 - saturation) * 0.2) + ((1 - effort) * 0.1)
    return round(raw, 3)


def read_signals(path: Path) -> list[dict]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python -m creator_signal_agent.analyze examples/signals.csv")

    rows = read_signals(Path(sys.argv[1]))
    ranked = sorted(rows, key=score_signal, reverse=True)
    for row in ranked:
        score = score_signal(row)
        review = "review" if score < 0.65 else "brief-ready"
        print(f"{score:.3f} {review} - {row['topic']} ({row['platform']})")


if __name__ == "__main__":
    main()
