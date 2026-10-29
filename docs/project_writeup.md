---
title: "Define and Classify an Analytical Problem"
subtitle: "Antimicrobial Resistance Genes in *Klebsiella pneumoniae* across Sub-Saharan Africa"
author: "Jeremy Kirunda"
---

**Topic:** Genomic surveillance of antimicrobial resistance (AMR) genes in *Klebsiella pneumoniae* across sub-Saharan Africa

# 1. Research gap

*Klebsiella pneumoniae* is one of the leading bacterial causes of deaths associated with antimicrobial resistance worldwide, and sub-Saharan Africa carries the highest death rate attributable to AMR of any region (Antimicrobial Resistance Collaborators, 2022). It is a major cause of hospital-acquired infections and neonatal sepsis in the region (Sands et al., 2021). Carbapenem-resistant and third-generation cephalosporin-resistant *Enterobacterales*, which include *K. pneumoniae*, are on the World Health Organization's *critical* priority list (WHO, 2024).

Ministries of Health, national AMR coordinating committees and hospital infection-control teams need an up-to-date picture of which resistance mechanisms are circulating, and where, in order to:

- Update empirical treatment guidelines for serious infections, such as sepsis, before culture and susceptibility results are available.
- Prioritise infection-prevention, laboratory and stewardship resources in the countries and settings with the highest burden of carbapenem resistance.
- Detect early warning signals of emerging high-risk resistance genes, such as new carbapenemases or mobile colistin resistance.

The operational gap is twofold:

- **Routine data are thin and hard to access.** Laboratory capacity for bacteriology is limited in many African countries. The largest multi-country compilation of susceptibility data (14 countries, 2016–2019) is held under controlled access (MAAP, 2025). National surveillance data, such as Uganda's 2018–2021 analysis, are not openly shared.
- **Open genomic data are not turned into decision-ready views.** Thousands of *K. pneumoniae* genomes from African studies are deposited in public databases and automatically screened for resistance genes. They are rarely summarised in a form that non-technical decision-makers can use.

# 2. Unit of analysis and outcome of interest

**Unit of analysis:** an individual sequenced *K. pneumoniae* isolate collected in a sub-Saharan African country and deposited in the NCBI Pathogen Detection database.

**Outcome of interest:** the isolate's resistance genotype, that is, which acquired resistance genes it carries as detected by NCBI's AMRFinderPlus. It is summarised as:

- carriage of **ESBL/AmpC genes** (resistance to third-generation cephalosporins);
- carriage of **carbapenemase genes** (resistance to carbapenems, the last-line antibiotics), and their family (OXA-48-like, NDM, KPC, VIM);
- carriage of **colistin resistance** determinants;
- the **number of antibiotic classes** affected, and **multidrug-resistant (MDR) genotype** status (3 or more classes).

# 3. Main descriptive variables

- **Geographic origin:** country and African Union region (Eastern, Southern, Western and Central Africa), as used by Africa CDC.
- **Collection year:** to observe trends over time.
- **Isolation source:** specimen group (blood, urine, gut carriage, wound/skin/pus, respiratory, other clinical, animal/environment).
- **Antibiotic class affected:** for example cephalosporins, carbapenems, aminoglycosides, quinolones and sulfonamides, assigned from NCBI's Reference Gene Catalog.
- **Presence of specific AMR genes:** for example *blaCTX-M-15*, *blaOXA-181*, *blaNDM-1* and *mcr* genes.
- **Study (BioProject):** the research project that contributed the isolate, used to check for sampling bias.

# 4. Data source

**NCBI Pathogen Detection**, *Klebsiella* AMR metadata table (<https://ftp.ncbi.nlm.nih.gov/pathogen/Results/Klebsiella/latest_snps/AMR/>). It is downloaded and filtered to sub-Saharan Africa with `scripts/download_ncbi_data.py`. Resistance genes are mapped to antibiotic classes using the **AMRFinderPlus Reference Gene Catalog** (Feldgarden et al., 2021).

The data downloaded on 28 October 2026 contain 10,441 sub-Saharan *Klebsiella* isolates, of which 9,761 are *K. pneumoniae*, from 25 countries. Of the isolates with a recorded collection year, 97% were collected in 2015 or later.

| Variable | Field name(s) in dataset | Role |
|---|---|---|
| Pathogen species | `scientific_name` | Inclusion filter |
| Geographic origin | `geo_loc_name` → `country`, `region` | Explanatory / grouping |
| Collection date | `collection_date` → `year` | Explanatory / time axis |
| Isolation source | `isolation_source`, `host` → `specimen` | Explanatory / grouping |
| Study | `bioproject_acc` | Explanatory (sampling bias) |
| AMR genes present | `AMR_genotypes` | Explanatory / outcome source |
| Antibiotic class affected | Reference Gene Catalog `class`, `subclass` | Grouping variable |
| ESBL/AmpC, carbapenemase, colistin, MDR genotype | derived from `AMR_genotypes` | Outcome of interest |

# 5. Focused analytical problem statement

AMR in *K. pneumoniae* is a severe and growing threat in sub-Saharan Africa. Published evidence is fragmented:

- Large multi-country susceptibility datasets exist, but they are aggregated or held under controlled access (MAAP, 2025).
- National analyses, such as Uganda's 2018–2021 surveillance report, describe one country at a time.
- Genomic studies typically examine a single hospital, outbreak or cohort.

Meanwhile, openly available genomes from many African studies are automatically screened for resistance genes by NCBI, but no accessible descriptive and diagnostic analysis has systematically quantified the prevalence of key resistance mechanisms across countries, specimen types and years using this single open resource. Such an analysis also needs to test whether apparent differences are real or artefacts of how isolates were sampled.

This project addresses that gap by building a descriptive and diagnostic analytics pipeline on NCBI Pathogen Detection *K. pneumoniae* data from sub-Saharan Africa. The pipeline characterises:

- **what** resistance mechanisms circulate, **where** and **when**; and
- **why** the observed patterns differ between countries and over time.

# 6. Output useful to the intended decision-maker

The intended decision-makers are:

- Ministries of Health and national AMR coordinating committees (for example Uganda's AMR National Coordinating Committee);
- Africa CDC;
- hospital infection-prevention and control committees.

The useful output is an **interactive AMR genomic surveillance dashboard** for exploring resistance patterns at a glance. It would include:

- a map of sub-Saharan Africa showing ESBL/AmpC, carbapenemase and MDR prevalence by country;
- filters for country, region, specimen type and collection year;
- a heatmap of antibiotic classes affected by country, and a breakdown of carbapenemase families;
- trend charts shown per country, not pooled, with each country's sample size, so that sampling artefacts are visible;
- a country profile, for example Uganda against its Eastern African neighbours.

# 7. Analytics type

- **Descriptive analytics:** summarises what resistance mechanisms are present, how common they are, and where and when isolates were collected.
- **Diagnostic analytics:** explains why patterns differ, such as South Africa's high carbapenemase burden, the apparent changes over time, the high MDR rate, and Uganda's lower ESBL rate. It does this by drilling down into specimen type, contributing study, sampling composition and gene co-occurrence.

# References

1. Antimicrobial Resistance Collaborators. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. *The Lancet*. 2022;399(10325):629–655.
2. World Health Organization. *WHO Bacterial Priority Pathogens List, 2024*. Geneva: WHO; 2024.
3. Sands K, et al. Characterization of antimicrobial-resistant Gram-negative bacteria that cause neonatal sepsis in seven low- and middle-income countries. *Nature Microbiology*. 2021;6:512–523.
4. Antimicrobial resistance in Africa: a retrospective analysis of data from 14 countries, 2016–2019. *PLOS Medicine*. 2025. doi:10.1371/journal.pmed.1004638.
5. Increasing trends of antibiotic resistance in Uganda: analysis of the national antimicrobial resistance surveillance data, 2018–2021. *BMC Infectious Diseases*. 2024. doi:10.1186/s12879-024-09806-y.
6. Feldgarden M, et al. AMRFinderPlus and the Reference Gene Catalog facilitate examination of the genomic links among antimicrobial resistance, stress response, and virulence. *Scientific Reports*. 2021;11:12728.
7. NCBI Pathogen Detection. <https://www.ncbi.nlm.nih.gov/pathogens/>
