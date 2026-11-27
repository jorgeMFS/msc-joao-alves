from sklearn.model_selection import LeaveOneGroupOut
import numpy as np

def lodo_splits(sample_table, train_samples, group_col="Source"):

    valid_datasets = []

    for source in sample_table["Source"].unique():

        dataset = sample_table[sample_table["Source"] == source]

        has_controls = (dataset["Intervention"] == "Control").any()
        has_treated = (dataset["Intervention"] != "Control").any()

        if has_controls and has_treated:
            valid_datasets.append(source)

    train_samples_ids = set(train_samples["Sample"])

    folds_final = {}

    for _, test_idx in LeaveOneGroupOut().split(
        sample_table,
        groups=sample_table[group_col]
    ):

        test_dataset = sample_table[group_col].iloc[test_idx].iloc[0]

        if test_dataset in valid_datasets:

            train_idx = np.flatnonzero(
                (sample_table[group_col] != test_dataset) &
                sample_table["Sample"].isin(train_samples_ids)
            )

            folds_final[test_dataset] = (train_idx, test_idx)

    return folds_final