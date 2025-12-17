# SummarizedExperiment and Ranged

When working with lab datasets in R, you’ll often see **SummarizedExperiment (SE)** and **RangedSummarizedExperiment (RSE)** objects.
These are standard **Bioconductor containers** for storing assay data together with metadata.
They form the foundation for more advanced containers like **MultiAssayExperiment (MAE)**.


### 1. SummarizedExperiment (SE)

🔹 **What it is**

A table-like container with:

* Rows = *features* (genes, proteins, probes)
* Columns = *samples* (patients, cell lines)
* Plus two metadata tables:

  * `rowData`: feature info (gene ID, annotation)
  * `colData`: sample info (patient, treatment, outcome)

🔹 **Why it matters**

Instead of managing separate expression and metadata files, SE bundles them together so analyses stay consistent.

```r
library(SummarizedExperiment)

counts <- matrix(rpois(100, 10), ncol = 5)
se <- SummarizedExperiment(
  assays = list(counts = counts),
  rowData = DataFrame(Gene = paste0("Gene", 1:20)),
  colData = DataFrame(Sample = paste0("S", 1:5), Treatment = c("A","A","B","B","B"))
)

se
```
For detailed explanations and examples, refer to the Bioconductor documentation:  [SummarizedExperiment vignette](https://www.bioconductor.org/packages/devel/bioc/vignettes/SummarizedExperiment/inst/doc/SummarizedExperiment.html)*


### 2. RangedSummarizedExperiment (RSE)

🔹 **What it is**

A specialized SE where each row corresponds to a **genomic range** (chromosome, start, end), stored as a `GRanges` object.

🔹 **Why it matters**

Many assays (RNA-seq, ChIP-seq, variant calls) produce data tied to coordinates. RSE makes it easy to query or subset by genomic location.

```r
library(GenomicRanges)

rowRanges <- GRanges(seqnames = "chr1", ranges = IRanges(start = 1:20, width = 100))
rse <- SummarizedExperiment(
  assays = list(counts = matrix(rpois(100, 10), ncol = 5)),
  rowRanges = rowRanges,
  colData = DataFrame(Sample = paste0("S", 1:5))
)

rse
```

For detailed explanations and examples, refer to the Bioconductor documentation:  [VariantExperiment vignette (RSE use case)](https://bioconductor.org/packages/devel/bioc/vignettes/VariantExperiment/inst/doc/VariantExperiment-class.html)


## 3. How They Connect to MultiAssayExperiment (MAE)

* **SE** is the base object for assays.
* **RSE** extends SE with genomic ranges.
* **MAE** (see separate page) collects multiple SE/RSE objects together for **multi-omics integration**.

```
MultiAssayExperiment
|-- ExperimentList
|     |-- SummarizedExperiment (e.g., RNA-seq)
|     |-- RangedSummarizedExperiment (e.g., mutations)
|     |-- SummarizedExperiment (e.g., proteomics)
|-- colData (patient metadata)
|-- sampleMap (patient ↔ assay IDs)
```

[MultiAssayExperiment page in this handbook](https://bhklab.github.io/handbook/dev/software_development/Languages/R/MultiAssayExperiment/)

## Quick Comparison

| Object  | Rows                           | Columns | Best for                |
| ------- | ------------------------------ | ------- | ----------------------- |
| **SE**  | Features (genes, proteins)     | Samples | Expression + metadata   |
| **RSE** | Genomic ranges (chr/start/end) | Samples | Range-based assays      |
| **MAE** | Multiple SE/RSE objects        | Samples | Multi-omics integration |

