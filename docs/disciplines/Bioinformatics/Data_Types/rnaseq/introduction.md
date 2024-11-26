# **RNA-seq**

---

## **What is RNA Sequencing (RNA-seq)?**

**RNA sequencing (RNA-seq)** is a method scientists use to study RNA molecules inside cells. 

**Central Dogma of Molecular Biology: DNA → RNA → Protein** 

RNA acts as the "messenger" that carries instructions from DNA (the cell’s blueprint) to make proteins, which do the actual work in the body. By sequencing RNA, we get a snapshot of the genes that are active at a specific moment, allowing us to understand how cells function and respond to different conditions.

---

## **Purpose of RNA-seq in Bioinformatics/Transcriptomics**

**Bioinformatics** is the use of computers to study biology, and **transcriptomics** focuses on studying RNA. RNA-seq is used to understand:

**1. Which genes are "switched on"?**

Identifies the genes actively transcribed into RNA in a given condition or cell type.

**2. How active is each gene?**

Quantifies the abundance of RNA molecules to measure the activity levels of specific genes.

**3. What changes occur in gene activity?**

Detects differences in gene expression between conditions, such as healthy vs. diseased states (e.g., cancer) or before and after treatment.

**4. How do RNA changes impact health?**

Links changes in RNA levels or structures to downstream effects on proteins, signaling pathways, and overall cellular function.

**5. How is RNA processed?**

Examines post-transcriptional modifications such as alternative splicing, where RNA segments are rearranged or removed, influencing the diversity of proteins produced.

---

## **How is RNA-seq Data Obtained?**

Here’s a simplified process:

1. **Extract RNA**: Scientists first collect RNA from cells or tissues.
2. **Make cDNA**: RNA is fragile, so it is converted into complementary DNA (cDNA), which is more stable.
3. **Cut into Pieces**: The cDNA is broken into smaller fragments.
4. **Sequence the Pieces**: Machines called sequencers read the fragments and identify the order of their building blocks (A, T, G, C).
5. **Assemble the Puzzle**: Bioinformatics tools put the fragments back together and measure how much RNA was in the original sample.

---

## **How is RNA-seq Different from DNA Sequencing?**

| **Feature**              | **DNA Sequencing**                          | **RNA Sequencing**                        |
|--------------------------|---------------------------------------------|------------------------------------------|
| **What is studied?**     | DNA, the cell’s blueprint.                 | RNA, the messengers from DNA.            |
| **Purpose**              | Understand the structure of genes, mutations, and inheritance. | Study gene activity and which genes are "on." |
| **Stable or Changing?**  | DNA is mostly stable and the same in all cells. | RNA levels vary depending on the cell’s activity. |
| **Building Blocks**      | A, T, G, C (Adenine, Thymine, Guanine, Cytosine). | A, U, G, C (Uracil replaces Thymine in RNA). |
| **Output**               | The sequence of an organism's entire genome or specific parts. | A snapshot of all active RNA molecules. |

---


## **Summary**

RNA-seq fits into the Central Dogma by focusing on RNA, the "middle step" between DNA and proteins. It provides a dynamic snapshot of gene activity, offering crucial insights into how cells work, respond to the environment, and contribute to diseases. By analyzing RNA, scientists can better understand the processes that sustain life and develop treatments for various conditions.
