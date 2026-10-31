"""Leave one dataset out.
"""
from sklearn.model_selection import LeaveOneGroupOut

def lodo_splits(sample_table, group_col="Source"):

    folds_final = []

    for train_idx, test_idx in LeaveOneGroupOut().split(sample_table, groups = sample_table[group_col]):
        folds_final.append((train_idx, test_idx))

    return folds_final


def build_mortality_labels(train_samples, survival_table):
    """Rótulo de mortalidade para as amostras de treino, usando só as
    intervenções presentes em train_samples. A implementar."""
    raise NotImplementedError
