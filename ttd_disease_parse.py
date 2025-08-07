import re
import os
import pandas as pd

# Define base directories
INPUT_DIR = "input"
OUTPUT_DIR = "output"

# Parsing Function
def parse_ttd_file(filepath):
    results = []
    current_target = {}
    
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) < 3:
                continue

            target_id, tag, value = parts[0], parts[1], parts[2]

            # New TARGETID block
            if tag == "TARGETID":
                # Save the previous target if complete
                if current_target.get('TARGETID') and current_target.get('TARGNAME') and current_target.get('INDICATIONS'):
                    results.append(current_target)
                # Start new
                current_target = {
                    'TARGETID': value,
                    'TARGNAME': '',
                    'TARGCODE': '',
                    'INDICATIONS': []
                }

            elif tag == "TARGNAME":
                current_target['TARGNAME'] = value
                match = re.search(r'\(([^()]+)\)', value)
                current_target['TARGCODE'] = match.group(1) if match else None

            elif tag == "INDICATI":
                status = value
                disease = parts[3] if len(parts) > 3 else ''
                current_target['INDICATIONS'].append((status, disease))

    # Saving last target
    if current_target.get('TARGETID') and current_target.get('TARGNAME') and current_target.get('INDICATIONS'):
        results.append(current_target)

    return results

# Script Execution
def main():
    filepath = os.path.join(INPUT_DIR, "ttd_data.txt")
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")

    print("Parsing file...")
    targets = parse_ttd_file(filepath)
    print(f"Total targets parsed: {len(targets)}")


    if not targets:
        print("No entries found.")
        return

# Flatten entries
    rows = []
    for t in targets:
        for status, disease in t['INDICATIONS']:
            rows.append({
                'TARGETID': t['TARGETID'],
                'TARGNAME': t['TARGNAME'],
                'TARGCODE': t['TARGCODE'],
                'INDICATI': disease,
                'STATUS': status
            })

    df = pd.DataFrame(rows)

# Saving Results
    output_file = os.path.join(OUTPUT_DIR, "ttd_disease_parsed.xlsx")
    df.to_excel(output_file, index=False)

    print(f"Parsed {len(df)} indication entries.")
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    main()
