from sklearn.linear_model import ElasticNet
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from pathlib import Path
import pandas as pd
import numpy as np



def transcriptomic_clock_mortality(sample_table, folds, exprs, hyperparameters):

    path = Path("C:/Users/João Alves/Desktop/Thesis/msc-joao-alves/results/")

    exprs = exprs.drop(columns=["Unnamed: 0"])

    predictions = sample_table
    predictions["Predicted_Expected_Hazard.log10"] = pd.NA

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

        X_train = exprs[sample_table["Sample"].iloc[train_idx]].T
        X_test = exprs[sample_table["Sample"].iloc[test_idx]].T

        #Remove genes detected in less than 20% of the samples
        mask = X_train.notna().mean(axis=0) > 0.2

        X_train = X_train.loc[:, mask]
        X_test = X_test.loc[:, mask]

        y_train = sample_table["Expected_Hazard.log10"].iloc[train_idx]

        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)

        predictions.loc[]





    return predictions