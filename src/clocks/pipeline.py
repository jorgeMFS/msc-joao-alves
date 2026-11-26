# Imports
import pandas as pd

from clocks.training_data import center_data, clean_samples
from clocks.lodo import lodo_splits
from clocks.hyperparameter_tuning import clock_mortality_hyperparameters_LODO


# Load data
exprs = pd.read_csv(
    "/kaggle/input/datasets/joaoalvess/expression/Expression_data_absolute_rodents_Scaled.csv",
    index_col=0
)

sample_table = pd.read_csv(
    "/kaggle/input/datasets/joaoalvess/metadata/table_Zenodo_complete.csv"
)


# Prepare data
centered_sample_table, centered_exprs = center_data(sample_table, exprs)

train_samples, test_samples = clean_samples(centered_sample_table)

folds = lodo_splits(test_samples, train_samples)


# Run pipeline
sel_folds = ["Current", "GSE101657"]

df = clock_mortality_hyperparameters_LODO(
    test_samples,
    centered_exprs,
    folds,
    "/kaggle/working/",
    sel_folds
)

