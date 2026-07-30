#!/usr/bin/env python3
"""Recompute model metric summaries and compare them with the released table."""
from pathlib import Path
import csv
import statistics
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data/results/df38_Loc_1_2021_model_fold_metrics_raw.csv"
EXPECTED = ROOT / "data/results/df38_Loc_1_2021_model_metrics_summary_percent.csv"
METRICS = ["Apl_Top1", "Apl_Top3", "Apl_Top5", "Balanced_Acc", "Macro_F1", "New_Field_Exact_MajVote_3", "New_Field_Exact_MajVote_5"]

def read_rows(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))

def main():
    groups = defaultdict(list)
    for row in read_rows(SRC):
        groups[(row["Model"], row["Eval_Domain"], row["Phase"])].append(row)

    rows = []
    for (model, domain, phase), items in sorted(groups.items()):
        out = {"Model": model, "Eval_Domain": domain, "Phase": phase, "n_folds": str(len(items))}
        for metric in METRICS:
            vals = []
            for item in items:
                try:
                    vals.append(float(item[metric]) * 100)
                except Exception:
                    pass
            if vals:
                out[metric + "_mean_percent"] = f"{statistics.mean(vals):.3f}"
                out[metric + "_sd_percent"] = f"{statistics.stdev(vals):.3f}" if len(vals) > 1 else ""
        rows.append(out)

    expected = read_rows(EXPECTED)
    fields = list(expected[0].keys()) if expected else []
    normalized_rows = [{field: row.get(field, "") for field in fields} for row in rows]

    if normalized_rows != expected:
        raise SystemExit("metric summary does not match the released table")
    print("metric summary matches released table")

if __name__ == "__main__":
    main()
