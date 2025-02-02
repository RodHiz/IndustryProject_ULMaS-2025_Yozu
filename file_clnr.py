import pandas as pd

# Load datasets
road_data = pd.read_csv(r"C:\Users\rodri\OneDrive\Documents\School - ULMaS\Industry Project - Yozu\researchFiles_temp\newCLEANnetwork.csv")
pothole_data = pd.read_csv(r"C:\Users\rodri\OneDrive\Documents\School - ULMaS\Industry Project - Yozu\researchFiles_temp\lcc_pothole_reports_data_mill.csv")

# Clean column names (remove spaces, lowercase)
pothole_data.columns = pothole_data.columns.str.strip().str.lower()
road_data.columns = road_data.columns.str.strip().str.lower()

# Rename address columns for consistency
pothole_data.rename(columns={'address1': 'address 1', 'address2': 'address 2'}, inplace=True)

# Debugging: Check if addresses align before merging
print("Pothole Addresses Sample:", pothole_data[['address 1', 'address 2']].dropna().head())
print("Road Addresses Sample:", road_data[['address 1', 'address 2']].dropna().head())

# Merge using Address 1 and Address 2
merged_data = pothole_data.merge(road_data, on=['address 1', 'address 2'], how='left')

# Handle missing values
merged_data.fillna({'speed limit': 30, 'urban/rural': 'Unknown', 'road type': 'Unknown'}, inplace=True)

# Save merged dataset
merged_data.to_csv('merged_pothole_road_data.csv', index=False)
# Define the columns you want to keep
columns_to_keep = ['address 1', 'address 2','easting','northing', 'order_cost', 'ordered_date', 'result', 'speed limit', 'urban/rural','length']

# Drop all other columns
merged_data = merged_data[columns_to_keep]

# Save cleaned dataset
merged_data.to_csv('cleanedRoadData.csv', index=False)

print("Cleaned data saved as 'cleanedRoadData.csv'")
