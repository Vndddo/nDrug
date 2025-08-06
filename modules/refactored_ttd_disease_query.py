import re
import pandas as pd

#Parsing Function
def parse_ttd_file(filepath):
    results = []
    current_target = {}
    
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) < 3:
                continue
            
            _, tag, value = parts[0], parts[1], parts[2]

            #New TARGETID block
            if tag == "TARGETID":
                # Save the previous target if complete
                if current_target.get('TARGETID') and current_target.get('TARGNAME') and current_target.get('INDICATIONS'):
                    results.append(current_target)
                #Start new
                current_target = {'TARGETID': value, 'TARGNAME': '', 'TARGCODE': '', 'INDICATIONS': []}
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

# Search Function
def query_disease_targets(filepath, query, output_file):
    print("Parsing file...")
    targets = parse_ttd_file(filepath)
    print(f"Total targets parsed: {len(targets)}")
    query_lower = query.lower()
    hits = []
    for target in targets:
        for status, disease in target.get('INDICATIONS', []):
            if query_lower in disease.lower():
                hits.append({
                    'TARGETID': target['TARGETID'],
                    'TARGNAME': target['TARGNAME'],
                    'TARGCODE': target['TARGCODE'],
                    'INDICATI': disease,
                    'STATUS': status
                })
    if not hits:
        print("No matching entries found.")
        return
    df = pd.DataFrame(hits)
    df.to_excel(output_file, index=False)
    print(f"Found {len(hits)} entries. Results saved to: {output_file}")
