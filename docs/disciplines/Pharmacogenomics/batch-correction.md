# Batch Correction Analysis

This page introduces the concept of batch correction in genomic data analysis, why it's important, and provides guidance on commonly used methods and tools.

---

## What is Batch Correction?

**Batch effects** are unwanted sources of variation in high-throughput data (e.g., RNA-seq, microarray) caused by differences in experimental conditions such as processing date, technician, reagent lot, or sequencing platform rather than true biological differences.

These effects can obscure biological signals and lead to false conclusions if not properly addressed.

> **Why it matters:** Uncorrected batch effects can inflate variance, bias downstream analysis (e.g., differential expression, clustering), and reduce the reproducibility and generalizability of results.

---

## Known vs. Unknown Batches

- **Known batch variables** (e.g., platform, date, plate) are recorded in metadata and can be directly modeled.
- **Unknown (latent) batch effects** need to be estimated from the data using statistical methods such as **SVA**.

---

## Common Methods for Batch Correction

| Method       | Type           | Key Tool/Package       | Notes |
|--------------|----------------|------------------------|-------|
| **ComBat**   | Known batches  | `sva::ComBat`          | Empirical Bayes; works well for microarray and log-transformed RNA-seq |
| **ComBat-seq** | Known batches | `sva::ComBat_seq`      | Designed for raw RNA-seq counts |
| **SVA**      | Unknown batches| `sva::sva`             | Surrogate Variable Analysis estimates hidden sources of variation |
| **RUV**      | Unknown batches| `RUVSeq`, `RUVnormalize` | Uses control genes or replicate samples |
| **Linear model** | Known batches | `limma::removeBatchEffect` | Simple and effective for design-aware modeling |
| **PCA**      | Diagnostic     | `prcomp`, `PCAtools`   | Not a correction method, but helpful for visualizing batch effects |

---

## General Workflow

1. **Explore batch effects**
   - PCA, boxplots, clustering by batch variables

2. **Choose method**
   - Known batch: try **ComBat** or **limma** 
   - Unknown batch: try **SVA** or **RUV**

3. **Apply correction**
   - Use relevant R functions from `sva`, `limma`, or `RUVSeq`

4. **Re-assess**
   - Re-run PCA or clustering to verify that batch effect is reduced without removing biological signal

---

## Note

- Always inspect data **before and after** correction.
- Don’t over-correct: ensure biological variation remains.
- For multi-center or multi-platform studies, combine batch correction with **meta-analysis** strategies.

---

**Key references:**
- Leek et al., *Bioinformatics*, 2010: [The sva package for removing batch effects and other unwanted variation in high-throughput experiments](https://pmc.ncbi.nlm.nih.gov/articles/PMC3307112/)
- Risso et al., *Nat Biotechnol*, 2016: [Normalization of RNA-seq data using factor analysis of control genes or samples](https://pubmed.ncbi.nlm.nih.gov/25150836/)

```