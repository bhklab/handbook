# Signature Analysis

This page provides guidelines for curating and analyzing RNA-based gene expression signatures. These signatures are typically published in peer-reviewed literature and made publicly available through trusted repositories.

---

## 🔍 What is a Signature?

A **gene signature** is a defined set of genes whose collective expression pattern is associated with a specific biological process, disease state, or response to therapy. Gene signatures are used in enrichment analysis, clustering, classification, and predictive modeling, and are increasingly applied to identify associations with drug response in both preclinical models and clinical datasets.

---

## 📦 Signature Sources

You can find gene signatures from:

- **MSigDB** (Molecular Signatures Database) – curated gene sets for enrichment analysis  
  → [https://www.gsea-msigdb.org/gsea/msigdb](https://www.gsea-msigdb.org/gsea/msigdb)

- **SignatureSets R package** – curated gene sets manually annotated and versioned  
  - Annotated with **GENCODE v40** (link to be added)
  - Uses **HUGO gene symbols** linked to **Entrez** and **Ensembl** IDs

---

## 🧮 Computing Signature Scores

Depending on the type of signature, different scoring strategies are used:

### ▸ Unweighted Signatures
- Methods: **GSVA**, **ssGSEA**
- Description: Compute enrichment scores across samples without gene-level weights

### ▸ Weighted Signatures
- Method: Weighted mean expression
- Weights: +1 (upregulated), –1 (downregulated)

### ▸ Signature-Specific Algorithms
- Some signatures require custom computation as defined in their original publication  
  → e.g., [PredictIO signature](ADD LINK TO PAPER)

---

## 📊 Signature Analysis Workflows

### 🔹 Cluster Analysis

1. Compute pairwise gene overlaps between signatures
2. Perform **PCA** on the overlap matrix (PC1 & PC2)
3. Cluster using **Affinity Propagation Clustering** (`apcluster`, v1.4.8)
4. For each cluster, aggregate genes and perform **KEGG pathway enrichment** using `enrichR` (v3.0)

### 🔹 Correlation Analysis

- Compute **Spearman correlations** between signature scores across studies
- Visualize with `corrplot` (v0.84)
- Report median correlation across datasets

### 🔹 Association Analysis

#### Clinical Associations
- **Binary outcomes** (e.g., response vs. no response): Logistic regression
- **Time-to-event data** (e.g., progression-free survival): Cox proportional hazards model

#### Preclinical Associations
- **Drug response metrics** (e.g., IC50, AUC): Spearman or Pearson correlation

> 🔍 Apply **multiple testing correction** (e.g., Benjamini-Hochberg FDR, Bonferroni) where appropriate.

---

## 📚 References

- [PREDICTIO PAPER](ADD LINK)
- SignatureSets Package (ADD LINK)
- MSigDB Resource
- [CodeOcean Tool for Signature Analysis](ADD LINK IF AVAILABLE)

---

## 🛠️ Tools and Packages

| Purpose                | Tool / Package               |
|------------------------|------------------------------|
| Signature scoring      | GSVA, ssGSEA, custom code    |
| Clustering             | `apcluster` (R)              |
| Enrichment analysis    | `enrichR` (R)                |
| Visualization          | `corrplot` (R)               |
| Association modeling   | `glm`, `coxph`               |

---

Let me know if you want me to:
- Add placeholder links for the missing references
- Turn this into a page layout in your local Markdown file
- Include example R code blocks or figures
