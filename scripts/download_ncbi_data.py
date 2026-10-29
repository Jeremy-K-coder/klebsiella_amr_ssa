import csv
import re
import sys
import urllib.request
from pathlib import Path

# 1.0 SETTINGS

BASE = "https://ftp.ncbi.nlm.nih.gov/pathogen"
AMR_DIR = f"{BASE}/Results/Klebsiella/latest_snps/AMR/"
CATALOG_URL = f"{BASE}/Antimicrobial_resistance/AMRFinderPlus/database/latest/ReferenceGeneCatalog.txt"
BASE_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

SSA_COUNTRIES = [
    "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon",
    "Central African Republic", "Chad", "Comoros", "Congo", "Cote d'Ivoire", "Côte d'Ivoire",
    "Democratic Republic of the Congo", "Djibouti", "Equatorial Guinea", "Eritrea", "Eswatini",
    "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho",
    "Liberia", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Mozambique", "Namibia",
    "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Senegal", "Sierra Leone", "Somalia",
    "South Africa", "South Sudan", "Sudan", "Swaziland", "Tanzania", "Togo", "Uganda", "Zambia",
    "Zimbabwe",
]

KEEP_COLS = [
    "target_acc", "biosample_acc", "bioproject_acc", "scientific_name", "geo_loc_name",
    "collection_date", "isolation_source", "host", "epi_type", "number_amr_genes",
    "AMR_genotypes", "AST_phenotypes",
]

# 2.0 DOWNLOAD

    # 2.1 Find the latest Klebsiella AMR metadata file
listing = urllib.request.urlopen(AMR_DIR).read().decode()
amr_file = re.search(r"PDG\d+\.\d+\.amr\.metadata\.tsv", listing).group(0)
print(f"Source file: {amr_file}")

    # 2.2 Stream the file and keep sub-Saharan African isolates only
RAW_DIR.mkdir(parents=True, exist_ok=True)
out_path = RAW_DIR / "klebsiella_ssa_ncbi.tsv"
kept = 0
with urllib.request.urlopen(AMR_DIR + amr_file) as resp, open(out_path, "w", newline="") as out:
    lines = (line.decode("utf-8", errors="replace").rstrip("\n") for line in resp)
    header = next(lines).lstrip("#").split("\t")
    idx = [header.index(c) for c in KEEP_COLS]
    geo = header.index("geo_loc_name")
    writer = csv.writer(out, delimiter="\t")
    writer.writerow(KEEP_COLS)
    for line in lines:
        row = line.split("\t")
        country = row[geo].split(":")[0].strip()
        if country in SSA_COUNTRIES:
            writer.writerow([row[i].strip('"') for i in idx])
            kept += 1
print(f"Sub-Saharan isolates saved: {kept:,} -> {out_path}")

    # 2.3 Download the AMRFinderPlus gene-to-drug-class catalog
urllib.request.urlretrieve(CATALOG_URL, RAW_DIR / "ReferenceGeneCatalog.txt")
print("Gene catalog saved")
