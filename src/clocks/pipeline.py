from pathlib import Path
import pandas as pd

from src.clocks.training_data import clean_samples, training_data
from src.clocks.lodo import lodo_splits
from src.clocks.hyperparameter_tuning import clock_mortality_hyperparameters


path = Path(__file__).resolve().parents[2]

sample_table = pd.read_csv(path / "results" / "table_Zenodo_complete.csv")
exprs = pd.read_csv(path / "data" / "raw" / "Expression_data_absolute_rodents_Scaled.csv")

train_samples, train_exprs = training_data(sample_table, exprs)

folds = lodo_splits(sample_table, clean_samples)

df = clock_mortality_hyperparameters(
    sample_table=sample_table,
    folds=folds,
    exprs=exprs,
    train_exprs=train_exprs,
    train_samples=train_samples
)

import shutil

output_dir = Path("outputs")
output_dir.mkdir(parents=True, exist_ok=True)

shutil.copy(
    path / "results" / "hyperparameters_mortality.csv",
    output_dir / "hyperparameters_mortality.csv"
)