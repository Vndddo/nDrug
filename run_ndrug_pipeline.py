import os
from modules.refactored_search_organism import search_organism
from modules.refactored_combine_prediction import combine_target_prediction
from modules.refactored_ttd_disease_query import query_disease_targets
from modules.refactored_filter_natural_target import filter_overlapping_targets

# Define base directories
INPUT_DIR = "input"
OUTPUT_DIR = "output"

def main():
    # Step 1: Search organism
    input_csv = os.path.join(INPUT_DIR, "coconut_csv-07-2025.csv") # Update database
    organism = input("Enter organism name to search for: ").strip()
    filtered_output = os.path.join(OUTPUT_DIR, f"filtered_{organism.replace(' ', '_')}.xlsx")
    search_organism(input_csv, organism, filtered_output)
    print(f"Filtered file saved to: {filtered_output}")

    input("Please curate with SwissTargetPrediction and place the CSVs into 'input/predictions/' folder. Press Enter to continue...")

    # Step 2: Combine predictions
    prediction_folder = os.path.join(INPUT_DIR, "predictions")
    combined_output = os.path.join(OUTPUT_DIR, "combined_target_prediction.xlsx")
    combine_target_prediction(prediction_folder, combined_output)
    print(f"Combined predictions saved to: {combined_output}")

    # Step 3: Query disease targets
    ttd_file = os.path.join(INPUT_DIR, "ttd_data.txt")
    disease = input("Enter disease name to search: ").strip()
    disease_output = os.path.join(OUTPUT_DIR, f"ttd_disease_{disease.replace(' ', '_')}.xlsx")
    query_disease_targets(ttd_file, disease, disease_output)
    print(f"Disease target results saved to: {disease_output}")

    # Step 4: Filter overlap
    overlap_output = os.path.join(OUTPUT_DIR, f"overlap_{organism.replace(' ', '_')}_{disease.replace(' ', '_')}.xlsx")
    filter_overlapping_targets(combined_output, disease_output, overlap_output)
    print(f"Final overlap saved to: {overlap_output}")

if __name__ == "__main__":
    main()
