from sklearn.linear_model import ElasticNet
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.exceptions import ConvergenceWarning
from pathlib import Path
import pandas as pd
import numpy as np
import warnings


def transcriptomic_clock_mortality_LODO(sample_table, exprs, folds, hyperparameters, output_path):

    output_path = Path(output_path)

    non_convergence = {}

    predictions = sample_table.copy()
    predictions["Expected_Hazard_centered"] = predictions["Expected_Hazard.log10"]
    predictions["Predicted_Expected_Hazard"] = pd.NA

    class GeneFilter(BaseEstimator, TransformerMixin):

        def fit(self, X, y=None):
            self.mask_ = X.notna().mean(axis=0) >= 0.2
            return self

        def transform(self, X):
            return X.loc[:, self.mask_]

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
            ("gene_filter", GeneFilter()),
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler(with_mean=True, with_std=False)),
            ("estimator", ElasticNet(alpha=alpha, l1_ratio = l1_ratio))
            ])

        train_idx = fold[0]
        test_idx = fold[1]

        X_train = exprs[predictions["Sample"].iloc[train_idx]].T
        X_test = exprs[predictions["Sample"].iloc[test_idx]].T

        y_train = predictions["Expected_Hazard_centered"].iloc[train_idx]

        with warnings.catch_warnings(record=True) as caught_warnings:
            warnings.simplefilter("always", ConvergenceWarning)

            pipeline.fit(X_train, y_train)

        non_convergence[dataset] = sum(
            issubclass(w.category, ConvergenceWarning)
            for w in caught_warnings
        )

        y_pred = pipeline.predict(X_test)

        predictions.loc[
            predictions.index[test_idx],
            "Predicted_Expected_Hazard"
        ] = y_pred
        

    predictions.to_csv(path / "results" / "predictions_mortality_LODO.csv", index=False, encoding = "utf-8")

    pd.DataFrame(
        non_convergence.items(), columns=["Dataset", "Non_converged"]).to_csv(
        path / "results" / "non_convergence_LODO.csv",
        index=False
    )

    return predictions