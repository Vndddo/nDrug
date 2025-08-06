# nDrug
# Natural Product Drug Discovery Toolkit

This repository provides a Python-based pipeline for natural compound screening and disease-target prediction. It supports both full automation and standalone script execution.

---

## Project Overview
Natural products are a valuable source of therapeutic leads. This toolkit helps researchers streamline three essential stages in early-phase natural product screening:

1. **Compound Data Retrieval from Collection of Open Natural Products database (COCONUT)**
2. **Therapeutic Target Data Retrieval from Therapeutic Target Database (TTD)**
3. **Pharmacological Network Building of Compound - Target Interaction**

---

## Structure
- `modules/`: Python scripts used in the pipeline.
- `standalone/`: Same logic, but runnable directly as separate scripts.
- `input/`: Place input files here.
- `output/`: Results will be saved here.

---

## How to Use
### Option 1: Full Pipeline
- **Purpose**: Automates retrieval of IUPAC names, molecular formulae, and SMILES strings from PubChem.
- **Input**: Excel file containing compound names.
- **Output**: Excel file with enriched compound information.
- **Usage**:
```bash
python run_ndrug_pipeline.py
```

