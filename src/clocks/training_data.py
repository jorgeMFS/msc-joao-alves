def clean_samples(sample_table):
    keep = ~sample_table["Expected_Hazard.log10"].isna()
    
    keep = (
        keep &
        ~sample_table["Source"].isin(["GSE219203", "GSE149029"]) &
        ~((sample_table["Source"] == "GSE124772") & (sample_table["Tissue"] == "Liver"))
    )
    
    train_samples = sample_table.loc[keep].reset_index(drop=True)

    return train_samples


def clean_expression(exprs):

    if "Unnamed: 0" in exprs.columns:
        clean_exprs = exprs.drop(columns=["Unnamed: 0"])

    return clean_exprs
