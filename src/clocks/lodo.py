from sklearn.model_selection import LeaveOneGroupOut
import numpy as np

def lodo_splits(sample_table, train_samples, group_col="Source"):

    train_samples_ids = set(train_samples["Sample"])

    folds_final = {}

    for _, test_idx in LeaveOneGroupOut().split(
        sample_table,
        groups=sample_table[group_col]
    ):

        test_dataset = sample_table[group_col].iloc[test_idx].iloc[0]

        train_idx = np.flatnonzero(
            (sample_table[group_col] != test_dataset) &
            sample_table["Sample"].isin(train_samples_ids)
        )

        folds_final[test_dataset] = (train_idx, test_idx)

    return folds_final