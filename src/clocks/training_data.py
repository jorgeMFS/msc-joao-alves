def clean_samples(sample_table):
    keep = ~sample_table["Expected_Hazard.log10"].isna()
    
    keep = (
        keep &
        ~sample_table["Source"].isin(["GSE219203", "GSE149029"]) &
        ~((sample_table["Source"] == "GSE124772") & (sample_table["Tissue"] == "Liver"))
    )
    
    train_samples = sample_table.loc[keep].reset_index(drop=True)

    return train_samples


def center_data(sample_table, exprs):

    centered_sample_table = sample_table.copy()
    centered_sample_table["Expected_Hazard_centered"] = centered_sample_table["Expected_Hazard.log10"]

    centered_exprs = exprs.copy()

    for source, tissue in centered_sample_table[["Source", "Tissue"]].drop_duplicates().itertuples(index=False, name=None):

        control_mask_samples = (
            (centered_sample_table["Source"] == source) &
            (centered_sample_table["Tissue"] == tissue) &
            (centered_sample_table["Intervention"] == "Control") &
            (centered_sample_table["Expected_Hazard.log10"].notna())
        )

        control_mask_exprs = (
            (centered_sample_table["Source"] == source) &
            (centered_sample_table["Tissue"] == tissue) &
            (centered_sample_table["Intervention"] == "Control")
        )

        control_list = centered_sample_table.loc[control_mask_exprs, "Sample"]

        group_mask_samples = (
            (centered_sample_table["Source"] == source) &
            (centered_sample_table["Tissue"] == tissue)
        )

        group_list = centered_sample_table.loc[group_mask_samples, "Sample"]

        control_median_samples = np.median(
            centered_sample_table.loc[control_mask_samples, "Expected_Hazard.log10"]
        )
        
        centered_sample_table.loc[group_mask_samples, "Expected_Hazard_centered"] = (
            centered_sample_table.loc[group_mask_samples, "Expected_Hazard.log10"] - control_median_samples
        )

        if len(control_list) > 0:
            control_median_exprs = np.median(
                centered_exprs.loc[:, control_list], axis = 1
            )

            centered_exprs.loc[:,group_list] = (
                centered_exprs.loc[:, group_list] - control_median_exprs
            )
        

    return centered_sample_table, centered_exprs