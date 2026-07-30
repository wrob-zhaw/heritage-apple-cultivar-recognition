#!/usr/bin/env python3
"""Recreate adaptive tree-holdout split assignments and compare with the released table."""
from pathlib import Path
import csv
import random
from collections import defaultdict, Counter

ROOT = Path(__file__).resolve().parents[1]
FEATURES = ROOT / "data/features/df38_Loc_1_2021_cleaned_svm_ready_features.csv"
EXPECTED = ROOT / "data/splits/df38_Loc_1_2021_adaptive_loto_fold_assignments.csv"
CORE_FIELDS = ["fold", "apple_id", "PL.Code", "tree_id", "role", "split_strategy", "heldout_tree_id"]

def read_rows(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))

def chunk_list(items, n):
    k, m = divmod(len(items), n)
    chunks = []
    start = 0
    for i in range(n):
        end = start + k + (1 if i < m else 0)
        chunks.append(items[start:end])
        start = end
    return chunks

def regenerated_rows():
    rows = read_rows(FEATURES)
    by_var = defaultdict(list)
    seen = set()
    for row in rows:
        key = (row["apple_id"], row["PL.Code"])
        if key in seen:
            continue
        seen.add(key)
        by_var[row["PL.Code"]].append({"apple_id": row["apple_id"], "PL.Code": row["PL.Code"], "tree_id": row["SACCBaum"]})

    rng = random.Random(42)
    output = []
    for code in sorted(by_var):
        group = by_var[code]
        counts = Counter(item["tree_id"] for item in group)
        trees = sorted(counts, key=lambda tree: (counts[tree], tree))
        n_trees = len(trees)
        if n_trees >= 3:
            holdout = trees[:3]
            strategy = "strict_loto"
            chunks = []
        elif n_trees == 2:
            holdout = [trees[0], trees[1], trees[0]]
            strategy = "two_tree_loto"
            chunks = []
        else:
            ids = sorted(item["apple_id"] for item in group)
            rng.shuffle(ids)
            chunks = chunk_list(ids, 3)
            holdout = [trees[0]] * 3
            strategy = "single_tree_fallback"
        for fold in range(3):
            test_ids = set(chunks[fold]) if n_trees == 1 else {item["apple_id"] for item in group if item["tree_id"] == holdout[fold]}
            for item in group:
                output.append({
                    "fold": str(fold),
                    "apple_id": item["apple_id"],
                    "PL.Code": code,
                    "tree_id": item["tree_id"],
                    "role": "test" if item["apple_id"] in test_ids else "train_val",
                    "split_strategy": strategy,
                    "heldout_tree_id": holdout[fold],
                })
    return output

def core(row):
    return {field: row.get(field, "") for field in CORE_FIELDS}

def main():
    expected = [core(row) for row in read_rows(EXPECTED)]
    regenerated = [core(row) for row in regenerated_rows()]
    if regenerated != expected:
        raise SystemExit("regenerated split assignments do not match the released table")
    print("split assignments match released table")

if __name__ == "__main__":
    main()
