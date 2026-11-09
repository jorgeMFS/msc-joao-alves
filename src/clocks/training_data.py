import numpy as np

def training_data(sample_table, exprs):

    if "Unnamed: 0" in exprs.columns:
        exprs = exprs.drop(columns=["Unnamed: 0"])

    keep = ~sample_table["Expected_Hazard.log10"].isna()

    keep = (
        keep &
        ~sample_table["Source"].isin(["GSE219203", "GSE149029"]) &
        ~((sample_table["Source"] == "GSE124772") & (sample_table["Tissue"] == "Liver"))
    )

    sample_table = sample_table.loc[keep].reset_index(drop=True)
    exprs = exprs.iloc[:, sample_table["Sample"]]

    return sample_table, exprs