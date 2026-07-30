# Data Dictionary

## Identifiers

- `apple_id`: fruit-level identifier.
- `dataset`: public subset identifier. All rows use `Loc_1_2021`.
- `harvest`: harvest year. All rows use `2021`.
- `Location` and `Loc`: public location label. All rows use `Loc_1`.
- `SACCBaum`: tree identifier used to define tree-holdout splits.
- `PL.Code`: class label used for model training and evaluation.
- `Sorte`: cultivar/accession name retained for readability.

## Feature Table

`data/features/df38_Loc_1_2021_cleaned_svm_ready_features.csv` contains one row per fruit. It includes identifiers, public class labels, shape descriptors, RGB/Lab color summaries, and GLCM texture descriptors.

`data/features/df38_Loc_1_2021_feature_distribution.csv` summarizes each released feature column with descriptive statistics.

## Metadata Tables

`data/metadata/df38_Loc_1_2021_apple_metadata.csv` contains the public metadata fields for the 907 fruit records.

`data/metadata/df38_Loc_1_2021_class_counts.csv` gives the number of fruits and trees per `PL.Code` class.

## Split Tables

`data/splits/df38_Loc_1_2021_tree_groups.csv` maps each fruit to its class and tree.

`data/splits/df38_Loc_1_2021_adaptive_loto_fold_assignments.csv` contains one row per fruit per fold. Rows marked `test` belong to the held-out tree for that class and fold; rows marked `train_val` remain available for training/validation.

`data/splits/df38_Loc_1_2021_adaptive_loto_fold_summary.csv` summarizes the number of fruits, classes, and trees in each fold/role combination.

## Result Tables

`data/results/df38_Loc_1_2021_model_fold_metrics_raw.csv` contains fold-level metric values.

`data/results/df38_Loc_1_2021_model_metrics_summary_percent.csv` contains the corresponding model-level summary metrics in percent.

`data/results/df38_vit384_loto_confusion_matrix_percent.csv` contains the class-by-class confusion matrix for the ViT-B/16 384 px evaluation.

The remaining ViT result tables list class support and the strongest off-diagonal confusion pairs.
