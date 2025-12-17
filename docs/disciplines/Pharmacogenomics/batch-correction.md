
# Batch Correction Analysis

This page introduces the concept of batch correction in genomic data analysis, explains why it matters, and provides a practical overview of commonly used methods and tools.

---

## What is Batch Correction?

**Batch effects** are unwanted sources of variation in high-throughput experiments (e.g., RNA-seq, microarrays) caused by technical differences such as processing date, technician, reagent lot, or sequencing platform — rather than true biological differences.

These effects can obscure meaningful biological signals and lead to misleading conclusions if not properly addressed.

> **Why it matters:** Uncorrected batch effects can inflate variance, bias downstream analyses (e.g., differential expression, clustering), and reduce the reproducibility and generalizability of findings.

---

## Technical Batches in Multi-Center Studies

In multi-center or multi-institutional studies, batch effects can arise due to:
- Differences in **sample processing protocols**
- **Sequencing platforms** or vendors used at each site
- Center-specific **technical pipelines** or lab personnel

When available, **center ID** or **platform ID** can be included as a batch variable. If unknown, statistical methods like **svaseq** or **RUVSeq** can help identify latent factors related to these center-specific technical artifacts.

---

## Known vs. Unknown Batches

- **Known batch variables** (e.g., center, platform, plate) are explicitly recorded in metadata and can be modeled directly.
- **Unknown (latent) batch effects** must be inferred from the data using statistical techniques such as **SVA** or **RUV**.

---

## Common Methods for Batch Estimation and/or Correction

| Method         | Type              | Key Tool/Package         | Notes                                                                 |
|----------------|-------------------|---------------------------|-----------------------------------------------------------------------|
| **ComBat**     | Known batches     | `sva::ComBat`             | Empirical Bayes method; widely used for microarray or log-transformed RNA-seq data |
| **ComBat-seq** | Known batches     | `sva::ComBat_seq`         | Variant of ComBat for **RNA-seq count data**                      |
| **svaseq**     | Unknown batches   | `sva::svaseq`             | RNA-seq-specific extension of SVA; models logCPM or transformed counts |
| **sva**     | Unknown batches   | `sva::sva`             | widely used for microarray or log-transformed RNA-seq data |
| **RUVSeq**     | Unknown batches   | `RUVSeq::RUVg`, `RUVs`    | Designed for RNA-seq counts using control genes or replicates         |
| **Linear Model** | Known batches   | `limma::removeBatchEffect` | Simple, design-aware batch removal approach for log-scale data        |
| **PCA**        | Diagnostic tool   | `prcomp`, `PCAtools`      | Visualization tool to detect batch structure; not a correction method |
| **PCA**        | Known batches in scRNA-seq data  | `harmony:RunHarmony`   | Alters the PCA embeddings using the batch information, but doesn't change the counts matrix|
---

## General Workflow

1. **Explore batch effects**
   - Use PCA, boxplots, or sample clustering by known batch variables

2. **Choose a method**
   - **Known batch**: Use **ComBat**, **ComBat-seq**, or **limma**
   - **Unknown batch**: Use **SVAseq** or **RUVseq** for RNA-seq data

3. **Apply correction**
   - Use appropriate functions from `sva`, `limma`, or `RUVSeq` depending on your data type

4. **Re-assess the data**
   - Visualize again (e.g., PCA, clustering) to confirm batch effects are minimized and biological signals preserved

---

## Best Practices

- Always inspect the data **before and after** batch correction
- Avoid overcorrection: ensure relevant biological variation is retained
- In multi-platform or multi-center studies, consider combining batch correction with **meta-analysis** approaches

---
## Note 

The choice of batch **estimation** and **correction** methods depends on the underlying **data distribution** and the **statistical assumptions** of each method.

- For example, **ComBat** assumes normally distributed log-transformed data, while **ComBat-seq** is specifically designed for raw count data.
- **svaseq** and **RUVSeq** also make different assumptions about latent variation and require careful selection of controls or models.

> **Recommendation:** Always assess your data type (e.g., log-transformed vs. raw counts) and the assumptions of each method before applying batch correction. Where possible, review relevant studies or perform simulations to justify your approach.

---

## Example

For a step-by-step example of batch estimation and correction using real log-transformed RNA-seq data, refer to the following guide:  
-  [Batch estimation: SVA](https://drive.google.com/file/d/1pvnGrQfymj22ls6epNMwBZ4mv5cvq8p8/view?usp=sharing)  
-  [Batch correction: ComBat](https://drive.google.com/file/d/16lNLoxRF_ELS8vhYBT2gKhoM4IZOvfzM/view?usp=sharing)

---

## References

- Leek JT et al., *Bioinformatics*, 2012.  
  [The sva package for removing batch effects and other unwanted variation in high-throughput experiments](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3307112/)

- Risso D et al., *Nature Biotechnology*, 2014.  
  [Normalization of RNA-seq data using factor analysis of control genes or samples](https://pubmed.ncbi.nlm.nih.gov/25150836/)

---