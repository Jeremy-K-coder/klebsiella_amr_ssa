# Antimicrobial Resistance Genes in *Klebsiella pneumoniae* across Sub-Saharan Africa

Data visualization project: descriptive and diagnostic analysis of open genomic AMR data from NCBI Pathogen Detection.

## Structure

| Path | Contents |
|---|---|
| `klebsiella_amr_descriptive_diagnostic.ipynb` | Main notebook: data preparation, 3 descriptive and 4 diagnostic questions, observations |
| `scripts/download_ncbi_data.py` | Downloads the latest NCBI *Klebsiella* AMR table (sub-Saharan Africa only) and the AMRFinderPlus gene catalog |
| `data/raw/` | Downloaded data (`klebsiella_ssa_ncbi.tsv`, `ReferenceGeneCatalog.txt`) |
| `data/processed/` | Analysis-ready isolate table produced by the notebook |
| `figures/`, `tables/` | Exported charts and summary tables |
| `docs/project_writeup.md` / `.docx` | Project definition write-up |

## Running

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python scripts/download_ncbi_data.py   # optional: refresh data from NCBI
./venv/bin/jupyter nbconvert --to notebook --execute --inplace klebsiella_amr_descriptive_diagnostic.ipynb
```

The notebook reads from `data/` using relative paths, so run it from the project root. On Google Colab, upload the project folder and `cd` into it first.

Data downloaded 28 October 2026 (NCBI file `PDG000000012.2563`, gene catalog `2026-08-07.1`).
