#!/usr/bin/env python3
"""Check the core Loc_1 2021 table sizes and labels."""
from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]

def read_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))

def unique(rows, col):
    return {row[col] for row in rows}

def main():
    features = read_rows(ROOT / "data/features/df38_Loc_1_2021_cleaned_svm_ready_features.csv")
    metadata = read_rows(ROOT / "data/metadata/df38_Loc_1_2021_apple_metadata.csv")
    classes = read_rows(ROOT / "data/metadata/df38_Loc_1_2021_class_counts.csv")
    tree_groups = read_rows(ROOT / "data/splits/df38_Loc_1_2021_tree_groups.csv")
    fold_assignments = read_rows(ROOT / "data/splits/df38_Loc_1_2021_adaptive_loto_fold_assignments.csv")

    print("features rows:", len(features))
    print("metadata rows:", len(metadata))
    print("classes:", len(classes))
    print("tree-group rows:", len(tree_groups))
    print("fold-assignment rows:", len(fold_assignments))
    print("unique apple IDs:", len(unique(features, "apple_id")))
    print("unique PL.Code:", len(unique(features, "PL.Code")))
    print("unique trees:", len(unique(features, "SACCBaum")))

    problems = []
    if len(features) != 907 or len(metadata) != 907:
        problems.append("expected 907 feature and metadata rows")
    if len(classes) != 38 or len(unique(features, "PL.Code")) != 38:
        problems.append("expected 38 PL.Code labels")
    if len(tree_groups) != 907:
        problems.append("expected 907 tree-group rows")
    if len(fold_assignments) != 2721:
        problems.append("expected 2721 fold-assignment rows")
    if len(unique(features, "SACCBaum")) != 113:
        problems.append("expected 113 tree groups")
    if unique(features, "dataset") != {"Loc_1_2021"}:
        problems.append("expected dataset value Loc_1_2021")
    if unique(features, "harvest") != {"2021"}:
        problems.append("expected harvest value 2021")
    if unique(features, "Location") != {"Loc_1"} or unique(features, "Loc") != {"Loc_1"}:
        problems.append("expected public location values to be Loc_1")

    if problems:
        print("FAILED:")
        for problem in problems:
            print("-", problem)
        return 1
    print("repository check passed")
    return 0

if __name__ == "__main__":
    sys.exit(main())
