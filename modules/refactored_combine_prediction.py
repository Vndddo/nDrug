import pandas as pd
import os
from glob import glob

# Function combining all target prediction CSVs
def combine_target_prediction(folder_path, output_path):
    combined_df = pd.DataFrame()
    csv_files = glob(os.path.join(folder_path, "*.csv"))

    if not csv_files:
        print("No CSV files found in the provided directory.")
        return

    for file in csv_files:
        df = pd.read_csv(file)
        compound_name = os.path.splitext(os.path.basename(file))[0]
        df['Compound_Name'] = compound_name
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    combined_df.to_excel(output_path, index=False)
    print(f"Done! Combined Excel file saved to: {output_path}")
