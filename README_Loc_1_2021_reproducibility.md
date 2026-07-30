# Loc_1 2021 Public Reproducibility Files

This repository contains the public analysis files for the Loc_1 2021 38-class comparative evaluation.

The released feature table is ready for SVM-style tabular analysis. It contains 907 fruit-level records from harvest 2021 at Loc_1 and 38 `PL.Code` classes. The retained cultivar-name field is `Sorte`.

Large image and segmentation archives are hosted separately and are not duplicated in this repository. They are available from the ETH Research Collection: [https://doi.org/10.3929/ethz-c-000803685](https://doi.org/10.3929/ethz-c-000803685).

## Repository Contents

- `data/features/`: tabular fruit descriptors and feature-level descriptive statistics.
- `data/metadata/`: fruit-level metadata and class counts.
- `data/splits/`: tree-group definitions and adaptive leave-one-tree-out fold assignments.
- `data/results/`: model metrics and confusion-matrix tables.
- `docs/`: data dictionary and feature descriptions.
- `figures/`: rendered figures corresponding to the included result tables.
- `scripts/`: small checks for row counts, split reconstruction, and metric-summary reconstruction.
- `repository_contents.csv`: file-by-file description of the repository contents.

## Key Tables

- `data/features/df38_Loc_1_2021_cleaned_svm_ready_features.csv`: main feature table; one row per fruit.
- `data/splits/df38_Loc_1_2021_adaptive_loto_fold_assignments.csv`: train/test membership for each fruit in each fold.
- `data/results/df38_Loc_1_2021_model_metrics_summary_percent.csv`: model-level metric summary in percent.
- `data/results/df38_vit384_loto_confusion_matrix_percent.csv`: class-level confusion matrix for the ViT-B/16 384 px evaluation.

## Checks

Run from the repository root:

```bash
python scripts/check_repository.py
python scripts/reproduce_metric_summary.py
python scripts/generate_split_definitions.py
```

Or run all checks with:

```bash
python scripts/run_all_checks.py
```
