from pathlib import Path
import pandas as pd

from src.clocks.training_data import clean_samples, training_data
from src.clocks.lodo import lodo_splits
from src.clocks.model_training import transcriptomic_clock_mortality_LODO


path = Path(__file__).resolve().parents[2]

sample_table = pd.read_csv(path / "results" / "table_Zenodo_complete.csv")
exprs = pd.read_csv(path / "data" / "raw" / "Expression_data_absolute_rodents_Scaled.csv")
hyperparameters = pd.read_csv(path / "results" / "hyperparameters_mortality_LODO.csv")

train_samples, train_exprs = training_data(sample_table, exprs)

folds = lodo_splits(sample_table, train_samples)

predictions = transcriptomic_clock_mortality_LODO(
    sample_table = train_samples,
    folds = folds, 
    exprs = train_exprs, 
    hyperparameters = hyperparameters)

import shutil

output_dir = Path("outputs")
output_dir.mkdir(parents=True, exist_ok=True)

shutil.copy(
    path / "results" / "predictions_mortality_LODO.csv",
    output_dir / "predictions_mortality_LODO.csv"
)