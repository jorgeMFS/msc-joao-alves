from sklearn.linear_model import ElasticNet
from sklearn.impute import SimpleImputer


def transcriptomic_clock_mortality(sample_table, folds, exprs):

    imputer = SimpleImputer(strategy="median")

    results = {}
    models = {}

    grid = {
        "alpha": np.logspace(-5, 2, 15),
        "l1_ratio": [0, 0.1, 0.25, 0.5, 0.75, 0.9, 1]
    }

    for dataset, fold in folds.items():

        train_idx = fold[0]
        test_idx = fold[1]

        X_train = exprs[sample_table["Sample"].loc[train_idx]].T
        X_test = exprs[sample_table["Sample"].loc[test_idx]].T

        mask = X_train.notna().mean(axis=0) > 0.2

        X_train = X_train.loc[:, mask]
        X_test = X_test.loc[:, mask]

        X_train = pd.DataFrame(
            imputer.fit_transform(X_train),
            index=X_train.index,
            columns=X_train.columns
            )

        X_test = pd.DataFrame(
            imputer.transform(X_test),
            index=X_test.index,
            columns=X_test.columns
            )

        y_train = sample_table["Age.days"].loc[train_idx]
        y_test = sample_table["Age.days"].loc[test_idx]

        search = GridSearchCV(
            ElasticNet(),
            grid,
            cv=5,
            scoring="r2",
            n_jobs=-1
        )

        search.fit(X_train, y_train)
        print(search.best_params_)

        model = search.best_estimator_

        models[dataset] = model

        predictions = model.predict(X_test)

        corr = pd.Series(predictions, index=y_test.index).corr(sample_table["Expected_Hazard.log10"].loc[test_idx], method = "pearson")

        results[dataset] = corr

    mean_R = np.mean(list(results.values()))

    return results, models, mean_R