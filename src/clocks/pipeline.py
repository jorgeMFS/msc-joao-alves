from pathlib import Path
import pandas as pd
import numpy as np

from src.clocks.training_data import clean_samples, clean_expression
from src.clocks.lodo import lodo_splits
#from src.clocks.model_training import transcriptomic_clock_mortality_LODO
from src.clocks.hyperparameter_tuning import clock_mortality_hyperparameters_LODO


path = Path(__file__).resolve().parents[2]

sample_table = pd.read_csv(path / "results" / "table_Zenodo_complete.csv")
exprs = pd.read_csv(path / "data" / "raw" / "Expression_data_absolute_rodents_Scaled.csv")

train_samples = clean_samples(sample_table)
exprs = clean_expression(exprs)

folds = lodo_splits(sample_table, train_samples)

df = clock_mortality_hyperparameters_LODO(sample_table, exprs, folds)

import shutil

output_dir = Path("outputs")
output_dir.mkdir(parents=True, exist_ok=True)

shutil.copy(
    path / "results" / "hyperparameters_mortality_LODO.csv",
    output_dir / "hyperparameters_mortality_LODO.csv"
)