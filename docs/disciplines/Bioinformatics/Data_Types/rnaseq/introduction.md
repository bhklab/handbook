# **RNA-seq**

---

## **What is RNA Sequencing (RNA-seq)?**

**RNA sequencing (RNA-seq)** is a high-throughput sequencing technology that allows scientists to map and quantify the transcriptome - essentially studying RNA molecules within cells. The transcriptome, or the RNA space, is comprised of messenger RNA (mRNA) and other non-coding RNAs (ncRNAs).

**Central Dogma of Molecular Biology: DNA → RNA → Protein** 

While all RNAs are transcribed from RNA, only the mRNAs are further translated into protein, hence they are oftend referred to as the "messengers" that carries instructions from DNA to create proteins, or the functional units within the cells. ncRNAs have several roles relating to the regulation of gene expression and other cellular activities. By sequencing RNA, we get a snapshot of the transcriptome, including active genes, allowing us to understand how cells function and respond to different conditions.

---

## **Purpose of RNA-seq in Bioinformatics/Transcriptomics**

**Bioinformatics** is the use of computational approaches to study biology, and **transcriptomics** focuses on studying RNA. Some purposes of RNA-seq in bioinformatic analysis include:

**1. Gene expression and activity**

Identifies the genes actively transcribed into mRNA in a given condition or cell type, giving an indication of which genes are "switched on". By quantifying the abundance of mRNA molecules, we can measure the activity levels of specific genes. RNA-Seq also allowed for examining post-transcriptional modifications such as alternative splicing, where RNA segments are rearranged or removed, influencing the diversity of proteins produced.

**2. ncRNA expression and activity**

Beyond mRNAs, several ncRNAs are of interest for cancer research. RNA-Seq also profiles the expression levels of these transcripts such that similar analyses can be performed as with mRNA.

**3. Differential RNA Expression**

Differential expression analysis can identify differences in RNA expression between different conditions (e.g. healthy vs diseased states, before and after treatment, etc). 

**4. Biomarker Analysis**

RNA transcript expression can be associted with the response to different drugs, hence are often used as input features to identify biomarkers for cancer treatment.

**5. Subtype Identification**

Patterns of RNA transcript expression can be used to identify distinct clusters or subgroups within a given population. This approach is often used to identify cancer subtypes.

**6. Functional Enrichment**

Using databases such as Gene Ontology (GO), KEGG, Reactome, mSigDB, etc, sets of RNA transcripts (e.g. from differential expression analysis) can be linked to downstream effects on biological processes, signaling pathways, and overallc cellular function. 


---

## **How is RNA-seq Data Obtained?**

Here’s a simplified process:

1. **RNA extraction**: Scientists first isolate and collect RNA from cells or tissue samples.
2. **Synthesize cDNA**: Due to the fragile nature of RNA, these transcripts are converted into complementary DNA (cDNA), which is more stable.
3. **Fragmentation**: The cDNA is broken into smaller fragments that enable them to be sequenced.
4. **Sequencing of Fragments**: Machines called sequencers read the fragments and identify the order of RNA nucleotides (A, U, G, C).
5. **Alignment**: Sequenced fragments are aligned to a reference genome or transcriptome to get position-based mapping information, such as mapping mRNA transcripts to their respective genes.
6. **Quantification**: With aligned fragments, transcript expression can be quantified.

---

## **How is RNA-seq Different from DNA Sequencing?**

| **Feature**              | **DNA Sequencing**                          | **RNA Sequencing**                        |
|--------------------------|---------------------------------------------|------------------------------------------|
| **What is studied?**     | DNA, the cell’s blueprint.                 | RNA, transcribed from DNA.            |
| **Purpose**              | Understand the structure of genes, mutations, and inheritance. | Study gene and transcript activity |
| **Stable or Changing?**  | DNA is mostly stable and the same in all cells. | RNA levels vary depending on the cell’s activity. |
| **Building Blocks**      | A, T, G, C (Adenine, Thymine, Guanine, Cytosine). | A, U, G, C (Uracil replaces Thymine in RNA). |
| **Output**               | The sequence of an organism's entire genome (WGS) or specific parts (WES). | A snapshot of all active RNA molecules. |

---


## **Summary**

RNA-seq fits into the Central Dogma by focusing on RNA, the "middle step" between DNA and proteins. It provides a dynamic snapshot of gene and transcript activity, offering crucial insights into how cells work, respond to the environment, and contribute to diseases. By analyzing RNA, scientists can better understand the processes that sustain life and develop treatments for various conditions.
