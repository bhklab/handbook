DESeq2 is a popular R package used for analyzing RNA count data - transcriptomics. It is widely used for differentially expressed analysis (DE) between different conditions (e.g. WT vs. mutant). The package also integrates many powerful data processing and analysis tools.
Features:
Normalization: DESeq2 normalizes the count data to account for differences in sequencing depth and RNA composition.
Statistical Modeling: It uses a negative binomial distribution to model the count data, which is appropriate for overdispersed count data.
Differential Expression Analysis: DESeq2 provides statistical tests to identify genes that are differentially expressed between conditions.
Visualization: The package includes functions for visualizing results, such as MA plots and heatmaps.

One may follow the workflow template from below (data preprocessing and further analysis are needed, and they vary between different analyses):
# Create DESeqDataSet object
dds <- DESeqDataSetFromMatrix(countData = countData, ## your raw count
                              colData = colData, ## your column metadata (i.e. sample/cell data)
                              design = ~ condition) ## specifies the experimental design (e.g. conditions, treatments, etc.)

# Run the DESeq2 pipeline
dds <- DESeq(dds)
DEresults = results(dds)
DEresults <- DEresults[order(DEresults$padj),]

# Extract results
res <- results(dds)

## MA plot to check how well normalization works
plotMA(dds)

One can perform QC through PCA plot:
rld <- rlog(dds)
DESeq2::plotPCA(rld, ntop = 500, intgroup = 'group') +
  ylim(-50, 50) + theme_bw()

## Visually DE result with volcano plot
dds <- DESeq(dds)
DEresults = results(dds)
library(EnhancedVolcano)
# DEseq object is S4 object - we need to convert it to a data frame (S3)
DEresults <- as.data.frame(DEresults)

EnhancedVolcano(DEresults,
                lab = row.names(DEresults),
                x = 'log2FoldChange',
                y = 'padj',
                pCutoff = 5e-2,
                FCcutoff = 1,
                labSize = 2.5,
                legendLabels=c('Not sig.',expression(paste('Log'[2],'FC')),'padj', expression(paste('padj & Log'[2],'FC'))),
                ylab = "padj")

