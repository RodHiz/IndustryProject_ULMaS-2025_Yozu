import pandas as pd

# Load datasets
temp_df = pd.read_csv(r"C:\Users\rodri\OneDrive\Documents\School - ULMaS\Industry Project - Yozu\researchFiles_temp\leedsTempConditions.csv")
precip_df = pd.read_csv(r"C:\Users\rodri\OneDrive\Documents\School - ULMaS\Industry Project - Yozu\researchFiles_temp\leedsPrecipQuant.csv")

# Merge on the 'date' column using a left join
merged_df = temp_df.merge(precip_df, on="datetime", how="left")

# Save the merged dataset
merged_df.to_csv("leedsWeather.csv", index=False)

# Display the first few rows
print(merged_df.head())
