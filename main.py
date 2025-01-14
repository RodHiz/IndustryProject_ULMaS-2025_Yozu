import pandas as pd

# File path to your pre-cleaned Excel sheet
file_path = r"C:\Users\rodri\OneDrive\Documents\School - ULMaS\Industry Project - Yozu\data\network 8-10-24 CLEAN.xlsx"

def load_data(sheet_name):
    """
    Load the Excel sheet into a DataFrame.
    """
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def explore_data(df):
    """
    Perform basic exploration of the dataset.
    """
    print("\nDataset Overview:")
    print(df.info())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nSummary Statistics:")
    print(df.describe())

def save_to_csv(df, output_file):
    """
    Save the DataFrame to a CSV file for further use.
    """
    try:
        df.to_csv(output_file, index=False)
        print(f"Data saved to '{output_file}'.")
    except Exception as e:
        print(f"Error saving data: {e}")

if __name__ == "__main__":
    # Step 1: Load the data
    sheet_name = "network 8-10-24 CLEAN"  # Replace with your actual sheet name
    data = load_data(sheet_name)

    if data is not None:
        # Step 2: Explore the data
        explore_data(data)

        # Step 3: Save the data (optional)
        #output_csv = "precleaned_data.csv"
        #save_to_csv(data, output_csv)
