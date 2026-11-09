import numpy as np

def clean_samples(sample_table):
    keep = ~sample_table["Expected_Hazard.log10"].isna()
    
    keep = (
        keep &
        ~sample_table["Source"].isin(["GSE219203", "GSE149029"]) &
        ~((sample_table["Source"] == "GSE124772") & (sample_table["Tissue"] == "Liver"))
    )
    
    sample_table = sample_table.loc[keep].reset_index(drop=True)

    return sample_table


def training_data(sample_table, exprs):

    sample_table = clean_samples(sample_table)

    if "Unnamed: 0" in exprs.columns:
        exprs = exprs.drop(columns=["Unnamed: 0"])

    exprs = exprs.loc[:, sample_table["Sample"]]

    return sample_table, exprs