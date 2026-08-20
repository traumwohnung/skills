#!/usr/bin/env python3
"""Validate the structure and minimum quality of a testing evidence matrix."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = (
    "obligation_id",
    "risk",
    "invariant",
    "layer",
    "oracle",
    "positive_case",
    "negative_case",
    "fault_point",
    "cadence",
    "owner",
    "evidence",
    "status",
)

RISKS = {"critical", "high", "medium", "low"}
LAYERS = {
    "unit",
    "property",
    "metamorphic",
    "differential",
    "fuzz",
    "component-integration",
    "contract",
    "slice-e2e",
    "full-e2e",
    "model",
    "mutation",
    "fault",
    "load",
    "soak",
    "canary",
    "production",
}
CADENCES = {"local", "pr", "main", "nightly", "release", "canary", "continuous"}
STATUSES = {"covered", "partial", "gap", "blocked", "not-applicable"}


def split_values(value: str) -> set[str]:
    return {item.strip() for item in value.split(";") if item.strip()}


def validate(path: Path, require_rows: bool) -> list[str]:
    errors: list[str] = []
    try:
        handle = path.open(newline="", encoding="utf-8-sig")
    except OSError as exc:
        return [f"cannot read {path}: {exc}"]

    with handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        missing = [name for name in REQUIRED_COLUMNS if name not in headers]
        if missing:
            return [f"missing required columns: {', '.join(missing)}"]

        rows = list(reader)

    if require_rows and not rows:
        errors.append("matrix has no obligation rows")

    seen: set[str] = set()
    for line, row in enumerate(rows, start=2):
        prefix = f"line {line}"
        obligation_id = row["obligation_id"].strip()
        if not obligation_id:
            errors.append(f"{prefix}: obligation_id is empty")
        elif obligation_id in seen:
            errors.append(f"{prefix}: duplicate obligation_id {obligation_id!r}")
        else:
            seen.add(obligation_id)

        for field in ("invariant", "layer", "oracle", "cadence", "owner", "status"):
            if not row[field].strip():
                errors.append(f"{prefix}: {field} is empty")

        risk = row["risk"].strip()
        if risk not in RISKS:
            errors.append(f"{prefix}: risk {risk!r} must be one of {sorted(RISKS)}")

        layers = split_values(row["layer"])
        invalid_layers = layers - LAYERS
        if invalid_layers:
            errors.append(f"{prefix}: unknown layer(s): {', '.join(sorted(invalid_layers))}")

        cadences = split_values(row["cadence"])
        invalid_cadences = cadences - CADENCES
        if invalid_cadences:
            errors.append(
                f"{prefix}: unknown cadence(s): {', '.join(sorted(invalid_cadences))}"
            )

        status = row["status"].strip()
        if status not in STATUSES:
            errors.append(f"{prefix}: status {status!r} must be one of {sorted(STATUSES)}")

        if status in {"covered", "partial"} and not row["evidence"].strip():
            errors.append(f"{prefix}: {status} obligation requires evidence")

        if risk in {"critical", "high"}:
            for field in ("positive_case", "negative_case"):
                if not row[field].strip():
                    errors.append(f"{prefix}: {risk} obligation requires {field}")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("matrix", type=Path, help="path to evidence-matrix.csv")
    parser.add_argument(
        "--require-rows",
        action="store_true",
        help="fail when the matrix contains only its header",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate(args.matrix, args.require_rows)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    with args.matrix.open(newline="", encoding="utf-8-sig") as handle:
        count = sum(1 for _ in csv.DictReader(handle))
    print(f"OK: {args.matrix} contains {count} valid obligation row(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
