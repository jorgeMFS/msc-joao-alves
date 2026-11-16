from sklearn.linear_model import ElasticNet
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from pathlib import Path
import pandas as pd
import numpy as np

def transcriptomic_clock_mortality_LODO(sample_table, folds, exprs, hyperparameters):

    path = Path(__file__).resolve().parents[2]

    if "Unnamed: 0" in exprs.columns:
        exprs = exprs.drop(columns=["Unnamed: 0"])

    predictions = sample_table.copy()
    predictions["Expected_Hazard_centered"] = predictions["Expected_Hazard.log10"]
    predictions["Predicted_Expected_Hazard"] = pd.NA

    for source, tissue in predictions[["Source", "Tissue"]].drop_duplicates().itertuples(index=False, name=None):

        control_mask = (
            (predictions["Source"] == source) &
            (predictions["Tissue"] == tissue) &
            (predictions["Intervention"] == "Control") &
            (predictions["Expected_Hazard.log10"].notna())
        )

        group_mask = (
            (predictions["Source"] == source) &
            (predictions["Tissue"] == tissue)
        )

        control_median = np.median(
            predictions.loc[control_mask, "Expected_Hazard.log10"]
        )
        
        predictions.loc[group_mask, "Expected_Hazard_centered"] = (
            predictions.loc[group_mask, "Expected_Hazard.log10"] - control_median
        )

        control_samples = predictions.loc[control_mask, "Sample"]
        group_samples = predictions.loc[group_mask, "Sample"]

        control_expr_median = exprs[control_samples].median(axis=1)

        exprs[group_samples] = exprs[group_samples].sub(control_expr_median, axis=0)

    for dataset, fold in folds.items():

        hp_fold = hyperparameters[hyperparameters["Dataset"]==dataset]
        alpha = hp_fold["Alpha"].iloc[0]
        l1_ratio = hp_fold["L1 Ratio"].iloc[0]

        pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler(with_mean=True, with_std=False)),
            ("estimator", ElasticNet(alpha=alpha, l1_ratio = l1_ratio))
            ])

        train_idx = fold[0]
        test_idx = fold[1]

        X_train = exprs[predictions["Sample"].iloc[train_idx]].T
        X_test = exprs[predictions["Sample"].iloc[test_idx]].T

        #Remove genes detected in less than 20% of the samples
        mask = X_train.notna().mean(axis=0) >= 0.2

        X_train = X_train.loc[:, mask]
        X_test = X_test.loc[:, mask]

        y_train = predictions["Expected_Hazard_centered"].iloc[train_idx]

        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)

        predictions.loc[
            predictions.index[test_idx],
            "Predicted_Expected_Hazard"
        ] = y_pred
        

    predictions.to_csv(path / "results" / "predictions_mortality_LODO.csv", index=False, encoding = "utf-8")

    return predictions