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

## How to Use
### Option 1: Full Pipeline
#### run_ndrug_pipeline.py
- **Purpose**: Automates retrieval of natural compounds data of queried organisms, target data collation of specific disease, and build compound - target relations.
- **Input**: Compound of interest, disease of interest, TTD database, COCONUT database.
- **Output**: Excel file of compound - target relations.
- **Usage**:
```bash
python run_ndrug_pipeline.py
```

### Option 2: Standalone Script
Each can be run individually from the `standalone/` folder.
#### search_organism.py
- **Purpose**: Automates retrieval of natural compounds data of queried organisms.
- **Input**: Compound of interest, COCONUT database.
- **Output**: Excel file of nautral compound of queried organism.
- **Usage**:
```bash
python standalone/search_organism.py
```
#### combine_predicition.py
- **Purpose**: Automates retrieval of natural compounds data of queried organisms, target data collation of specific disease, and build compound - target relations.
- **Input**: Excel/ CSV files containing compounds predicted target manually obtained from SwissTargetPrediction.
- **Output**: Combined file of predicted target.
- **Usage**:
```bash
python standalone/combine_prediction.py
```
#### ttd_disease_query.py
- **Purpose**: Collate target data of queried disease.
- **Input**: Disease of interest and TTD database.
- **Output**: Excel file of target data.
- **Usage**:
```bash
python standalone/ttd_disease_query.py
```
#### filter_natural_target.py
- **Purpose**: Build compound - target relations from overlapped targeting.
- **Input**: Excel file of compounds predicted targets and compiled target data.
- **Output**: Excel file of compound - target relations.
- **Usage**:
```bash
python standalone/filter_natural_target.py
```
---

## Setup
```bash
pip install -r requirements.txt
```

Make sure folders exist:

```bash
mkdir input output
```

Then place:
- compound CSV file in `input/`
- SwissTargetPrediction results in `input/predictions/`
- TTD `.txt` file in `input/`
