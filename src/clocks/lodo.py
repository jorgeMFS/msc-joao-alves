"""Leave one dataset out."""

from sklearn.model_selection import LeaveOneGroupOut

def lodo_splits(sample_table, group_col="Source"):

    train_samples = clean_samples(sample_table)

    control_datasets = set(sample_table[sample_table["Family"] == "Control"][group_col])
    treated_datasets = set(sample_table[sample_table["Family"] != "Control"][group_col])

    # Only datasets with both controls and treated samples
    valid_datasets = control_datasets & treated_datasets

    folds_final = {}

    for _, test_idx in LeaveOneGroupOut().split(sample_table, groups=sample_table[group_col]):

        test_dataset = sample_table[group_col].iloc[test_idx].iloc[0]

        if test_dataset in valid_datasets:
            test_idx = test_idx
            train_idx = train_samples.index[train_samples[group_col] != test_dataset].to_numpy()

            folds_final[test_dataset] = (train_idx, test_idx)

    return folds_final