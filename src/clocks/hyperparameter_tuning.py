from sklearn.linear_model import ElasticNet
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV, GroupKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from pathlib import Path
import pandas as pd
import numpy as np

def clock_mortality_hyperparameters(sample_table, folds, exprs):

    path = Path("C:/Users/João Alves/Desktop/Thesis/msc-joao-alves/results/")

    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler(with_mean=True, with_std=False)),
        ("estimator", ElasticNet())
        ])

    grid = {
        "estimator__alpha": np.logspace(-5, 2, 15),
        "estimator__l1_ratio": [0, 0.1, 0.25, 0.5, 0.75, 0.9, 1]
    }

    df = pd.DataFrame()

    for dataset, fold in folds.items():

        train_idx = fold[0]
        test_idx = fold[1]

        groups_train = sample_table["Source"].iloc[train_idx]

        X_train = exprs[sample_table["Sample"].iloc[train_idx]].T
        X_test = exprs[sample_table["Sample"].iloc[test_idx]].T

        #Remove genes detected in less than 20% of the samples
        mask = X_train.notna().mean(axis=0) >= 0.2 

        X_train = X_train.loc[:, mask]
        X_test = X_test.loc[:, mask]

        keep = ~sample_table["Expected_Hazard.log10"].isna()
        keep = (
            keep &
            ~sample_table["Source"].isin(["GSE219203", "GSE149029"]) &
            ~((sample_table["Source"] == "GSE124772") & (sample_table["Tissue"] == "Liver"))
        )
        sample_table = sample_table.loc[keep].reset_index(drop=True)
        exprs = exprs.iloc[:, keep.to_numpy()]

        y_train = sample_table["Expected_Hazard.log10"].iloc[train_idx]

        search = GridSearchCV(
            pipeline,
            grid,
            cv=GroupKFold(n_splits=5),
            scoring="r2",
            n_jobs=-1
        )

        search.fit(X_train, y_train, groups=groups_train)

        data = pd.DataFrame({
            "Dataset": [dataset],
            "Alpha": [search.best_params_["estimator__alpha"]],
            "L1 Ratio": [search.best_params_["estimator__l1_ratio"]]
        })

        df=pd.concat([df, data], ignore_index=True)

    df.to_csv(path/"hyperparameters_mortality.csv", index=False, encoding = "utf-8")

    return df
