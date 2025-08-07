import pandas as pd
import re
import os

# Define base directories
INPUT_DIR = "input"
OUTPUT_DIR = "output"

# Character Mapping (Greek to Latin)
greek_to_latin = {
    'alpha': 'A',
    'beta': 'B',
    'gamma': 'G',
    'delta': 'D',
    'epsilon': 'E',
    'kappa': 'K',
    'lambda': 'L',
    'omega': 'O',
    'theta': 'T'
}

# Target Name Normalisation
def normalize_target_code(name):
    if pd.isna(name):
        return ""
    name = name.lower()
    name = re.sub(r'[-\s]', '', name)  # Remove dashes and spaces
    for greek, latin in greek_to_latin.items():
        name = name.replace(greek, latin)
    return name.upper()

# Filtering Function
def filter_overlapping_targets(compound_file, gen_disease_file, output_file):  
    # Loading Data
    compound_df = pd.read_excel(compound_file)
    disease_df = pd.read_excel(gen_disease_file)

    # Check required columns exist
    if "Common name" not in compound_df.columns:
        raise ValueError("Missing 'Common name' column in compound file.")
    if "TARGCODE" not in disease_df.columns:
        raise ValueError("Missing 'TARGCODE' column in disease file.")

    # Normalize Target IDs
    compound_df["Normalized_Target"] = compound_df["Common name"].apply(normalize_target_code)
    disease_df["Normalized_Target"] = disease_df["TARGCODE"].apply(normalize_target_code)

    # Merging Dataframe
    overlap_df = pd.merge(compound_df, disease_df, on="Normalized_Target", how="inner")

    # Save by Indication
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        compound_df.to_excel(writer, sheet_name="Compound_Targets", index=False)
        disease_df.to_excel(writer, sheet_name="Disease_Targets", index=False)
        overlap_df.to_excel(writer, sheet_name="Overlap", index=False)

        indications = overlap_df["INDICATI"].dropna().unique()
        for indication in indications:
            # Sanitize sheet name
            sheet_name = str(indication)[:31].replace('/', '_').replace('\\', '_')
            # Filter rows matching this indication
            sub_df = overlap_df[overlap_df["INDICATI"] == indication]
            # Write to sheet
            sub_df.to_excel(writer, sheet_name=sheet_name, index=False)


    print(f"Done. {len(overlap_df)} overlapping targets found.")
    print(f"{len(indications)} unique indication sheets created.")
    print(f"Results saved to: {output_file}")

def main():
    compound_file = os.path.join(OUTPUT_DIR, "combined_targ_pred.xlsx")
    gen_disease_file = os.path.join(OUTPUT_DIR, f"ttd_disease_parsed.xlsx")
    output_file = os.path.join(OUTPUT_DIR, "filtered_targets.xlsx")
    filter_overlapping_targets(compound_file, gen_disease_file, output_file)

if __name__ == "__main__":
    main()

