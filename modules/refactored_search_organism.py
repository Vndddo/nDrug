import pandas as pd
import os

# Query Function
def search_organism(input_csv, organism_query, output_excel):
    combined_df = pd.DataFrame()
    chunk_size = 100_000
    matches = []

    print(f"Searching for rows containing organism: '{organism_query}'...")

    for chunk in pd.read_csv(input_csv, chunksize=chunk_size, dtype=str, low_memory=False):
        # Replace NaNs with empty strings to avoid errors in str.contains
        chunk.fillna("", inplace=True)

        # Check if any cell in the row contains the organism (case-insensitive)
        mask = chunk.apply(lambda row: row.astype(str).str.contains(organism_query, case=False).any(), axis=1)
        matching_rows = chunk[mask]
        if not matching_rows.empty:
            matches.append(matching_rows)

    if matches:
        print(f"Found {sum(len(df) for df in matches)} matching rows.")
        # Concatenate all matching chunks
        result_df = pd.concat(matches, ignore_index=True)
        result_df.to_excel(output_excel, index=False)
        print(f"Saved matches to '{output_excel}'")
    else:
        print("No matching rows found.")
