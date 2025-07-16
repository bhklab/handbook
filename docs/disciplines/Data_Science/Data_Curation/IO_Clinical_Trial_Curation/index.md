# Immuno-Oncology Clinical Trial Curation

**Welcome to the Immuno-Oncology Curation Guide!**

Whether you're new to the lab or need a quick refresher, this guide walks you through the process of curating Immuno-Oncology (IO) clinical trial datasets into structured, analysis-ready R objects. The goal is to standardize raw and processed data into clean **MultiAssayExperiment (MAE)** objects for use in downstream analysis and collaborative research.

## What Is IO Curation?

IO curation is the process of transforming clinical trial data into reusable, analysis-ready formats compatible with R-based workflows.

Each curated dataset includes two key components:

1. **Clinical metadata**: Patient/sample-level information such as treatment, response, survival, demographics.  
2. **Molecular profiles**: Expression data (RNA-seq or microarray), and when available SNV and CNA data. These are formatted as [SummarizedExperiment (SE) or RangedSummarizedExperiment (RangedSE)](https://bioconductor.org/packages/devel/bioc/vignettes/SummarizedExperiment/inst/doc/SummarizedExperiment.html)  objects, depending on the assay type.
3. **Annotation data**: Row-level annotations (e.g., Ensembl ID, gene name) are stored within each assay.

We curate all data into the [**MultiAssayExperiment (MAE)**](https://www.bioconductor.org/packages/devel/bioc/vignettes/MultiAssayExperiment/inst/doc/MultiAssayExperiment.html) format. All publicly available curated datasets are located on [ORCESTRA](https://www.orcestra.ca/clinical_icb). We recommend downloading one to explore the clinical metadata and molecular assay structure.

## Step-by-Step Workflow

An example of a clinical data processing pipeline is available [ICB_Van_Allen Snakemake](https://github.com/BHKLAB-Pachyderm/ICB_Van_Allen-snakemake.git).

The standard curation process includes:

1. **Access and download source data** (raw or processed)  
2. **Process or import molecular data** (e.g., RNA-seq, SNV, CNA), ensuring standardized formats and identifiers  
3. **Process and clean clinical metadata**, harmonizing variable names, response labels, and survival fields  
4. **Add standardized annotations** (e.g., drug names, gene identifiers, tissue types)  
5. **Create `SE` or `RangedSE` objects**, depending on assay type  
6. **Assemble the final `MAE` object**, integrating all data components  
7. **Review a reference IO dataset**, curated example on [ORCESTRA](https://www.orcestra.ca/clinical_icb).

## 1. Download Source Data

Begin by reviewing the original publication to confirm study design, molecular assays, and whether the data is public or private.

#### Dataset Categories

- **Private datasets**: Stored internally (e.g., Box, institutional drives). May include PHI and require ethics approval.
- **Public datasets**: Available via [GEO](https://www.ncbi.nlm.nih.gov/geo/), [dbGaP](https://www.ncbi.nlm.nih.gov/gap/), [Zenodo](https://zenodo.org), and [EGA](https://ega-archive.org).

### 1.1 Molecular Data

If raw RNA (FASTQ files) are not available, look for processed files by modality:

- RNA-seq: TPM or count matrices (CSV, TSV, Excel)  
- RNA-seq: Isoform-level expression (optional but recommended)  
- Microarray: Normalized expression matrices (e.g., quantile normalized)
- DNA (SNV): VCF, MAF, or binary gene-level mutation calls  
- DNA (CNA): Gene-by-sample matrices or segment files

### 1.2 Expression and Mutation Data

[RNA sequencing (RNA-seq)](https://bhklab.github.io/handbook/dev/disciplines/Bioinformatics/Data_Types/rnaseq/) quantifies gene expression by aligning RNA reads to a reference genome.

There are two options depending on data availability:

* **If only processed RNA-seq data is available**:
  Use the provided gene-level TPM or count matrices (CSV, TSV, or Excel format). Include isoform (transcript-level) data when available.

* **If RNA-seq FASTQ files are available**:
  Use the [kallisto Snakemake pipeline](https://bhklab.github.io/handbook/dev/disciplines/Bioinformatics/Tools/RNAseq_Pipelines/kallisto/) available on [HPC4Health (H4H)](https://bhklab.github.io/handbook/dev/software_development/Remote_Development/High_Performance_Computing_for_Health/).
  FASTQ files are typically stored at: `/cluster/projects/bhklab/rawdata/EGA/`
  The pipeline is located in `pipelines/kallisto_snakemake_pipeline/`, with setup instructions in `README.md`. Expression values can be extracted using [this script](https://github.com/BHKLAB-DataProcessing/ICB_Common/blob/main/code/process_kallisto_output.R).

  For *microarray data*, follow the same structure using quantile-normalized expression matrices.
  For *SNV data*, use either pre-processed mutation calls, or extract SNVs directly from FASTQ files using appropriate variant-calling pipelines (e.g., [WES and RNA-seq reference](https://www.researchgate.net/figure/Analysis-Pipeline-for-WGS-WES-and-RNA-seq-Flow-chart-demonstratessequential-use-of_fig1_334573016)).


<!-- ## COMMENT: Farnoosh will improve this part -->
### 1.3 Clinical Metadata 

Clinical metadata should be collected as CSV or Excel files and should include:

- Patient/sample identifiers
- Treatment and response information
- OS/PFS time and event censoring (highly preferred)

## 2. Process Molecular Data

You will need **TPM values** for downstream analysis, whether derived from raw FASTQ files or already processed expression data. The final output should be **log-transformed TPM**.

* If you have **TPM**, use:

  ```r
  log2(TPM + 0.001)
  ```

* If you have **raw counts**, convert to TPM using:

  ```r
  GetTPM <- function(counts, gene_length) {
    x <- counts / gene_length
    return(t(t(x) * 1e6 / colSums(x)))
  }
  ```

Other data types:
* **SNV data**: Binary gene × sample matrix preferred
* **CNA data**: Gene-level amplifications, deletions, or summary scores
* Ensure row and column names are clean, and sample IDs are consistent across all data types
* See helpful utility functions in the [`ICB_Common/code`](https://github.com/BHKLAB-DataProcessing/ICB_Common/tree/main/code) repository

## 3. Process Clinical Data

Format clinical metadata as:

- **Rows**: patient/sample IDs  
- **Columns**: clinical attributes

### 3.1 Mandatory Columns

| **Column name**                          | **Description**                                                                                                                                                                                                                                            |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Patientid**                            | This column contains unique patient identifiers                                                                                                                                                                                                            |
| **treatmentid**                          | This column contains the treatment regimen of each patient. Individual drug names are separated by ":" and standardized based on the lab's nomenclature. For example, the drug combo "FAC" is represented as "5-fluorouracil:Doxorubicin:Cyclophosphamide" |
| **response**                             | This column contains the response status of the patients to the given treatment - Responders (R) and Non-responders (NR)                                                                                                                                   |
| **tissueid**                             | Cancer type standardized based on the lab's nomenclature from [Oncotree](http://oncotree.mskcc.org/). Example:  “Breast”                                                                                                                                                                 |
| **survival_time_pfs/survival_time_os**   | The time starting from taking the treatment to the occurrence of the event of interest. The event name like "pfs", "os" must be appended to survival_time to differentiate the survival measure. Example for data in this column: “2.6”                    |
| **survival_unit**                        | The unit in which the survival time is measured. If the event is measured in other units such as “day”, or “year”, it must be converted to "month" for consistency                                                                                         |
| **event_occurred_pfs/event_occurred_os** | Binary measurement showing whether the event of interest occurred (1) or not (0).  The event name like "pfs", "os" must be appended to event_occurred to differentiate the survival measure                                                                |


!!!note
    Common columns must be the first set of columns appearing in the metadata, followed by any additional columns. You may add other metadata columns available in the source data, but the standardized columns above should be present first.

### 3.2 Additional Columns 

The table below shows the other common columns across the 19 ICB datasets curated

| Column name         | Description                                                                                                                                                                                                                                   | type            |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| age                 | Age                                                                                                                                                                                                                                           | source          |
| AMP                 | Sum of total AMP/coverage; calculated from CNA values                                                                                                                                                                                         | in-lab curation |
| cancer\_type        | Type of cancer tissue                                                                                                                                                                                                                         | source          |
| CIN                 | Calculated from CNA values                                                                                                                                                                                                                    | in-lab curation |
| CNA\_tot            | Sum of total CNA/coverage; calculated from CNA values                                                                                                                                                                                         | in-lab curation |
| DEL                 | Sum of total DEL/coverage; calculated from CNA values                                                                                                                                                                                         | in-lab curation |
| dna                 | DNA sequencing type. eg: whole exome sequencing                                                                                                                                                                                               | source          |
| dna\_info           | Method for normalizing DNA sequencing data                                                                                                                                                                                                    | in-lab curation |
| histo               | Histological info such as subtype                                                                                                                                                                                                             | source          |
| indel\_nsTMB\_perMb | -                                                                                                                                                                                                                                             | in-lab curation |
| indel\_nsTMB\_raw   | -                                                                                                                                                                                                                                             | in-lab curation |
| indel\_TMB\_perMb   | -                                                                                                                                                                                                                                             | in-lab curation |
| indel\_TMB\_raw     | -                                                                                                                                                                                                                                             | in-lab curation |
| nsTMB\_perMb        | -                                                                                                                                                                                                                                             | in-lab curation |
| nsTMB\_raw          | -                                                                                                                                                                                                                                             | in-lab curation |
| recist              | Annotated using [RECIST](https://recist.eortc.org/). The most commonly used responses are CR, PR, SD, PD.                                                                                                                                     | source          |
| response.other.info | Same data as Responders (R) and Non-responders (NR)                                                                                                                                                                                           | source          |
| rna                 | Type of rna processed data. eg: TPM                                                                                                                                                                                                           | source          |
| rna\_info           | Method for normalizing RNA sequencing data                                                                                                                                                                                                    | in-lab curation |
| sex                 | Sex of the patient - Male or Female                                                                                                                                                                                                           | source          |
| stage               | Cancer stage                                                                                                                                                                                                                                  | source          |
| survival\_type      | PFS or OS or both (denoted by '/'). If both, added by in-lab curation                                                                                                                                                                         | in-lab curation |
| TMB\_perMb          | TMB per megabase (Mb) calculated where: TMB = mutns/target; mutns = number of non-synonymous mutations; and target = target size of the sequencing. See Supplementary Table S2 of [PMID: 36055464](https://pubmed.ncbi.nlm.nih.gov/36055464/) | in-lab curation |
| TMB\_raw            | Tumor Mutation Burden raw values                                                                                                                                                                                                              | in-lab curation |
| treatment           | Drug target or drug name                                                                                                                                                                                                                      | source          |

## 4. Add Annotations  <!-- links for gene or drug annotation is not informative. It refers to the repo that includes different scripts or information. Please improve this part which is really important. -->

Lab standardized annotation data are stored in [BHKLab-Pachyderm's](https://github.com/BHKLAB-Pachyderm/Annotations) 

### 4.1 Gene Annotations

Check the gene annotation version used in the original dataset (typically stated in the reference paper or supplement).  

Then download the matching file from the BHKLab [Annotations repository](https://github.com/BHKLAB-Pachyderm/Annotations). Using `Gencode.v19.annotation.RData` and `Gencode.v40.annotation.RData` files are preferred: 

- [**Gencode v19**](https://github.com/BHKLAB-Pachyderm/Annotations/blob/master/Gencode.v19.annotation.RData)  
- [**Gencode v40**](https://github.com/BHKLAB-Pachyderm/Annotations/blob/master/Gencode.v40.annotation.RData)  

Each `.RData` file includes`features_gene`, `features_transcript`, and `tx2gene`.  

!!! note
     The goal is to **retain as many genes as possible** and match the original reference. Using a mismatched annotation version can lead to a loss of gene entries—this is not preferred.

### 4.2 Drug Annotations

Standardize treatment names using BHKLab’s drug annotation files, using [drugs_with_ids.csv](https://github.com/BHKLAB-DataProcessing/Annotations/blob/master/drugs_with_ids.csv).

If the treatment is not listed there, search external databases such as [**PubChem**](https://pubchem.ncbi.nlm.nih.gov/) to verify the correct drug name.

!!!note
    For the `treatment` column, immunotherapy regimens are currently grouped into the following categories:
    
    - **PD-1/PD-L1**: Immune checkpoint inhibitors targeting PD-1 or PD-L1
    - **CTLA4**: Checkpoint inhibitors targeting CTLA-4
    - **IO+combo**: Combination immunotherapy
    - **IO+chemo**: Immunotherapy plus chemotherapy
    - **IO+targeted**: Immunotherapy plus targeted therapy

### 4.3 Tissue Annotations

Use [OncoTree](http://oncotree.mskcc.org/) to map cancer types. If unmatched, perform manual review and map to standardized tissue categories.

## 5. Create SE or RangedSE 

Use:

- `SummarizedExperiment`: for expression or mutation matrices (TPM, SNV binary calls)
- `RangedSummarizedExperiment`: for genomic ranges (e.g., VCFs with genomic coordinates)

Each object should include:

- `assay`: main data matrix (features × samples)  
- `rowData`: feature metadata (e.g., gene symbol, Ensembl ID)  
- `colData`: sample-level metadata (clinical)


## 6. Build MAE

Integrate multiple assay types and clinical data into a single MAE object.

**Required Components:**

- `experiments()`: a list of `SE`/`RangedSE` objects (e.g., `expr`, `snv`, `cna`)  
- `colData()`: the clinical metadata  
- `sampleMap()`: map linking sample IDs to patients across assays

## 7. IO Example Dataset

View the dataset online at **[ICB_Van_Allen](https://www.orcestra.ca/clinical_icb/62f29ca3b89ff37208748d8b)** — available on **Orcestra**.

The following tabs are included:

- **Dataset Tab**: Contains **Gencode v19** annotations and related publication references. 

- **Pipeline Tab**:  
    - **Commit**: Key scripts are available available in this [GitHub commit](https://github.com/BHKLAB-DataProcessing/ICB_Van_Allen-snakemake/tree/c7a8e0e9e70b27c690e57312eab36d8557629c14). Below is the structure of the folder:

    ```
    📁  ICB_Van_Allen/
    ├── 📄 Snakefile                       # Snakemake workflow combining all scripts
    └── 📁 scripts
        ├── 📄 format_downloaded_data.R   # Generates CLIN, EXPR, SNV input files
        ├── 📄 Format_CLIN.R              # Cleans and annotates clinical metadata
        ├── 📄 Format_EXPR.R              # Processes and logs RNA expression data
        ├── 📄 Format_SNV.R               # Cleans SNV mutation data
        ├── 📄 Format_CNA_seg.R           # Segmented CNA profiles 
        ├── 📄 Format_CNA_gene.R          # Gene-level CNA profiles 
        └── 📄 Format_cased_sequenced.R   # Flags patients with RNA/CNA/SNV data
    ```

    - **Script**: Core functions for curating clinical and molecular data, [ICB_Common](https://github.com/BHKLAB-Pachyderm/ICB_Common/tree/9d3297b69d182e459a25596971670020473a63a5)
    - **Annotation**: Source for drug, tissue and gene annotations files, [Annotations](https://github.com/BHKLAB-Pachyderm/Annotations/tree/bd2325ad727b2351d637b66f0313d0dfb81a0917)
