# Antimicrobial Resistance Genes in *Klebsiella pneumoniae* across Sub-Saharan Africa

Data visualization project: descriptive and diagnostic analysis of open genomic AMR data from NCBI Pathogen Detection.

## Structure

| Path | Contents |
|---|---|
| `klebsiella_amr_descriptive_diagnostic.ipynb` | Main notebook: data preparation, 3 descriptive and 4 diagnostic questions, observations |
| `scripts/download_ncbi_data.py` | Downloads the latest NCBI *Klebsiella* AMR table (sub-Saharan Africa only) and the AMRFinderPlus gene catalog |
| `data/raw/` | Downloaded data (`klebsiella_ssa_ncbi.tsv`, `ReferenceGeneCatalog.txt`); not tracked in git, kept on Google Drive or recreated with the download script |
| `data/processed/` | Analysis-ready isolate table produced by the notebook |
| `figures/`, `tables/` | Exported charts and summary tables |
| `docs/project_writeup.md` | Project definition write-up |

## Running

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python scripts/download_ncbi_data.py   # optional: refresh data from NCBI
./venv/bin/jupyter nbconvert --to notebook --execute --inplace klebsiella_amr_descriptive_diagnostic.ipynb
```

On Google Colab the notebook mounts Google Drive and uses `MyDrive/data-visualization/klebsiella_amr/` as its base folder. Put the two raw files in `MyDrive/data-visualization/klebsiella_amr/data/raw/`; the processed data, figures and tables are written to `data/processed/`, `figures/` and `tables/` in that folder. To download the raw data straight to Drive from Colab:

```python
!python download_ncbi_data.py /content/drive/MyDrive/data-visualization/klebsiella_amr
```

Run locally, the notebook uses the project folder instead, so run it from the project root.

Data downloaded 28 October 2026 (NCBI file `PDG000000012.2563`, gene catalog `2026-08-07.1`).
