"""Leave one intervention out.

Ponto crítico. O rótulo do relógio de mortalidade tem de ser construído
DENTRO de cada fold, a partir das curvas de sobrevivência das intervenções
de treino apenas. Se se usarem os rótulos publicados pelo tAge, a fuga que a
tese denuncia continua presente.
"""
from sklearn.model_selection import GroupKFold


def loio_splits(sample_table, group_col="intervention"):
    """Um fold por intervenção. sample_table tem uma linha por amostra."""
    groups = sample_table[group_col].values
    n_groups = sample_table[group_col].nunique()
    return GroupKFold(n_splits=n_groups).split(sample_table, groups=groups)


def build_mortality_labels(train_samples, survival_table):
    """Rótulo de mortalidade para as amostras de treino, usando só as
    intervenções presentes em train_samples. A implementar."""
    raise NotImplementedError
