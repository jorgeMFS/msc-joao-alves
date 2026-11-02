"""Leave one dataset out.
"""
from sklearn.model_selection import LeaveOneGroupOut

def lodo_splits(sample_table, group_col="Source"):

    control_datasets = set(sample_table[sample_table["Family"] == "Control"][group_col])
    treated_datasets = set(sample_table[sample_table["Family"] != "Control"][group_col])

    # Only datasets with both controls and treated samples
    valid_datasets = control_datasets & treated_datasets

    folds_final = {}

    for train_idx, test_idx in LeaveOneGroupOut().split(sample_table, groups=sample_table[group_col]):

        test_dataset = sample_table[group_col].iloc[test_idx].iloc[0]

        if test_dataset in valid_datasets:
            folds_final[len(folds_final)] = (train_idx, test_idx)

    return folds_final