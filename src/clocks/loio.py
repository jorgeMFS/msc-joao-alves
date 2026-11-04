"""Leave one intervention out.

Ponto crítico. O rótulo do relógio de mortalidade tem de ser construído
DENTRO de cada fold, a partir das curvas de sobrevivência das intervenções
de treino apenas. Se se usarem os rótulos publicados pelo tAge, a fuga que a
tese denuncia continua presente.
"""
import numpy as np


def loio_splits(sample_table, group_col=["Source","Family","Component1","Component2"]):

    folds = sample_table[["Source", "Family", "Component1", "Component2"]].drop_duplicates()
    folds = folds[(folds["Family"] != "Control") & (folds["Source"] != "GSE219203")]

    test_fold = {}
    train_fold= {}
    folds_loio = []
    folds_final = {}

    for row in range(len(folds)):
        dataset = folds.iloc[row]["Source"]
        family = folds.iloc[row]["Family"]
        comp1 = folds.iloc[row]["Component1"]
        comp2 = folds.iloc[row]["Component2"]

        test_fold[row] = sample_table[(sample_table["Source"] == dataset)]

        train_fold[row] = sample_table[~(
            (sample_table["Source"] == dataset) |
            (sample_table["Family"] == family) |
            (sample_table["Component1"] == comp1) |
            (sample_table["Component1"] == comp2) |
            (sample_table["Component2"] == comp1) |
            (sample_table["Component2"] == comp2)
            )]

        test_idx = test_fold[row].index

        train_idx = train_fold[row].index

        split = (frozenset(train_idx), frozenset(test_idx))

        folds_loio.append(((dataset, family), split))

    for key, fold in folds_loio:

        train_labels = sorted(fold[0])
        test_labels = sorted(fold[1])

        train_arr = sample_table.index.get_indexer(train_labels)
        test_arr = sample_table.index.get_indexer(test_labels)

        folds_final[key] = (train_arr, test_arr)

    return folds_final



def build_mortality_labels(train_samples, survival_table):
    """Rótulo de mortalidade para as amostras de treino, usando só as
    intervenções presentes em train_samples. A implementar."""
    raise NotImplementedError
