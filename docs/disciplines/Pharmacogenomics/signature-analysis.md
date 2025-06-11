# Signature Analysis

This page provides guidelines for curating and analyzing RNA-based gene expression signatures. These signatures are typically published in peer-reviewed literature and made publicly available through trusted repositories.

---

## What is a Signature?

A **gene signature** is a defined set of genes whose collective expression pattern is associated with a specific biological process, disease state, or response to therapy. Gene signatures are used in enrichment analysis, clustering, classification, and predictive modeling, and are increasingly applied to identify associations with drug response in both preclinical models and clinical datasets.

---

## Signature Sources

You can find gene signatures from:

- **MSigDB** (Molecular Signatures Database) – curated gene sets for enrichment analysis  
  → [https://www.gsea-msigdb.org/gsea/msigdb](https://www.gsea-msigdb.org/gsea/msigdb)

- **SignatureSets R package** – curated gene sets manually annotated and versioned  
  - Annotated with **GENCODE v40** [bhklab/SignatureSets](https://github.com/bhklab/SignatureSets)
  - Uses **HUGO gene symbols** linked to **Entrez** and **Ensembl** IDs

---

## Computing Signature Scores

Depending on the type of signature, different scoring strategies are used:

### ▸ Unweighted Signatures
- Methods: **GSVA**, **ssGSEA**
- Description: Compute enrichment scores across samples without gene-level weights

### ▸ Weighted Signatures
- Method: Weighted mean expression
- Weights: +1 (upregulated), –1 (downregulated)

### ▸ Signature-Specific Algorithms
- Some signatures require custom computation as defined in their original publication  
  → e.g., [bhklab/PredictioR](https://github.com/bhklab/PredictioR)

---

## Signature Analysis Workflows

### 🔹 Cluster Analysis

1. Compute pairwise gene overlaps between signatures
2. Perform **PCA** on the overlap matrix
3. Cluster using **Affinity Propagation Clustering** (`apcluster`)
4. For each cluster, aggregate genes and perform pathway enrichment analysis (e.g., **KEGG**, **Reactome**, or **GO Biological Process**) using tools like `enrichR`, `clusterProfiler`, or `gprofiler2`
  

### 🔹 Correlation Analysis

To assess similarity or redundancy between gene signatures:

- **Compute Spearman and/or Pearson correlation coefficients** between signature scores across samples.
  - *Spearman* is rank-based, captures monotonic relationships, and is robust to outliers and non-linear patterns.
  - *Pearson* assumes linear relationships and is sensitive to the scale and magnitude of values.
- Use the `cor()` function in R with `method = "spearman"` or `"pearson"` as appropriate.

- - **Visualize** the correlation matrix using the `corrplot` R package or a heatmap (e.g., `pheatmap` or `ComplexHeatmap`) to identify clusters or patterns among signatures.

### 🔹 Association Analysis

#### Clinical Associations
- **Binary outcomes** (e.g., response vs. no response): Logistic regression
- **Time-to-event data** (e.g., progression-free survival): Cox proportional hazards model

#### Preclinical Associations
- **Drug response metrics** (e.g., IC50, AUC): Spearman or Pearson correlation

> Apply **multiple testing correction** (e.g., Benjamini-Hochberg FDR, Bonferroni) where appropriate.

---

## Additional Tools and Packages

| Purpose                | Tool / Package                                      |
|------------------------|-----------------------------------------------------|
| Signature scoring      | GSVA, ssGSEA, custom code                           |
| Clustering             | `apcluster`, `hclust`                               |
| Enrichment analysis    | `enrichR`, `clusterProfiler`, `fgsea`               |
| Visualization          | `corrplot`, `ComplexHeatmap`, `pheatmap`, `ggplot2` |
| Association modeling   | `glm`, `survival` (includes `coxph`), `caret`       |

> **Note:** The choice of packages or pipelines may vary based on the specific research question and analysis goals.

---

## Example

CO link will be added. 