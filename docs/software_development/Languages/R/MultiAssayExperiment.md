
## MultiAssayExperiment
It is a package in R used to harmonize data management of multiple experimental assays performed on an overlapping set of specimens. It is designed to manage and integrate multiple types of omics or experimental data (e.g., RNA-seq, mutation data, methylation, proteomics) into a single, structured object.  The object stores different data modalities (assays) together, keep track of which samples have which data types, with a goal to facilitate joint analysis, visualization, and subsetting across multiple experiments.


> "It provides a familiar Bioconductor user experience by extending concepts from SummarizedExperiment,
> supporting an open-ended mix of standard data classes for individual assays,
> and allowing subsetting by genomic ranges or rownames. 
> Facilities are provided for reshaping data into wide and long
> formats for adaptability to graphing and downstream analysis."

Citation

> Ramos M, Schiffer L, Re A, Azhar R, Basunia A, Rodriguez Cabrera C, Chan T, Chapman P, Davis S, Gomez-Cabrero D, Culhane A, Haibe-Kains B, Hansen K, Kodali H, Louis M, Mer A, Reister M, Morgan M, Carey V, Waldron L (2017). “Software For The Integration Of Multi-Omics Experiments In Bioconductor.” Cancer Research, 77(21), e39-42. doi:10.1158/0008-5472.CAN-17-0344, https://cancerres.aacrjournals.org/content/77/21/e39. 


### Structure of a MultiAssayExperiment Object

- **`ExperimentList`**: A list of assays (SummarizedExperiment, matrix, or other compatible objects).
- **`colData`**: Metadata about the primary samples (patients/cell lines), such as age, treatment, outcome.
- **`sampleMap`**: A table mapping how each assay's sample IDs relate to the primary colData sample IDs (handles cases where IDs differ across experiments).

        MultiAssayExperiment
        |-- ExperimentList
                |-- RNA-seq matrix
                |-- Mutation calls (binary matrix)
                |-- Proteomics data
        |-- colData (patient-level metadata)
        |-- sampleMap (which patient → which sample in each assay)

## When to MultiAssayExperiment
You can create a MultiAssayExperiment object if you have a multiomics dataset (RNA, DNA mutation data, proteomics) for the same or overlapping sets of samples, and if you want to apply multi-omics integration methods, ML models, or visualizations that require synchronized datasets.


## Installation requirement
R with version > 4.5

        if (!require("BiocManager", quietly = TRUE))
            install.packages("BiocManager")

        BiocManager::install("MultiAssayExperiment")

        

## Make a MultiAssayExperiment Object

```r
library(MultiAssayExperiment)

# Suppose you have rna, mutation data and patient information
rna <- SummarizedExperiment(assays = list(counts = matrix(rnorm(1000), ncol = 10)))
snv <- matrix(sample(0:1, 100, replace = TRUE), ncol = 10)
patient_info <- as.data.frame(
  PatientID = paste0("Patient", 1:10),
  Age = sample(40:80, 10)
)

# Create the MultiAssayExperiment object with function
mae <- MultiAssayExperiment(
  experiments = ExperimentList(rna = rna, mutations = mutations),
  colData = patient_info
)

## How to view and work with a MultiAssayExperiment 
We will give an example Using Immune Checkpoint Blockade Dataset. Suppose you have downloaded a Immune Checkpoint Blockade Dataset from [ORCESTRA](https://www.orcestra.ca/)
    
    library(MultiAssayExperiment)
    # Load dataset
    icb_mae <- readRDS(icb_file)

    # Extract clinical data (patient information, treatment, disease etc.)
    clinical_data <- colData(icb_mae) %>% as.data.frame()
  
    # view RNA
    rna_se <- experiments(icb_mae)[["expr"]]
    rna_sample <- colnames(rna_se) # Sample names inside RNA assay
    rna_expr <- assay(rna_se) # save the rna expression with sample to a matrix 
  
    # view mutation data
    snv_se <- experiments(icb_mae)[["snv"]]
    snv_matrix <- assay(snv_se)

    # Mapping between assays and primary samples
    sample_map <- sampleMap(icb_mae)

    # View metadata if available, this include any extra information about the experiment (i.e. batch info, project details)
    meta_data <- metadata(icb_mae)

## Additional References 

Bioconductor [MultiAssayExperiment](https://www.bioconductor.org/packages/release/bioc/html/MultiAssayExperiment.html)

User reference manual [PDF](https://www.bioconductor.org/packages/release/bioc/manuals/MultiAssayExperiment/man/MultiAssayExperiment.pdf)





