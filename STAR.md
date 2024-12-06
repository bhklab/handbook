# STAR Alignment Guide

## Introduction

**STAR** (Spliced Transcripts Alignment to a Reference) is a high-performance RNA-seq read aligner, widely used for mapping RNA sequencing data to reference genomes. It is optimized for speed and accuracy, especially for aligning spliced reads across exon-exon junctions.

This guide explains how to set up and use STAR for RNA-seq read alignment.

## Installation and Setup

### Loading STAR on the H4H Cluster

To use STAR on the H4H cluster, load the module:

```bash
module load STAR
```
### Verifying Installation

After loading STAR, check the version to ensure compatibility with your pipeline:

```bash
STAR --version
```
The output should display the version number, for example:
```
STAR\2.7.9a
```
# Preparing for STAR Alignment

Before using STAR, ensure you have the following files:

### Reference Genome FASTA File
- Contains the DNA sequences of your reference genome.
- **Example for GRCh38:**
  - Here: https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/405/GCF_000001405.40_GRCh38.p14/
  `GCF_000001405.40_GRCh38.p14_genomic.fna.gz`

### Gene Annotation File (GTF)
- Includes gene structure (exons, introns, splice junctions).
- **Example for GRCh38:**
  - Here: https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/405/GCF_000001405.40_GRCh38.p14/
  `GCF_000001405.40_GRCh38.p14_genomic.gtf.gz`

### RNA-seq FASTQ Files
- Paired-end or single-end sequencing data.

## Index

## 2. Generating a Genome Index

STAR requires a genome index to efficiently align reads. Submit the following command in your SLURM script to generate it:

```bash
module load STAR/<version_number>
# Replace <version_number> with the desired version, e.g., module load STAR/2.7.9a

STAR --runThreadN 8 \
     --runMode genomeGenerate \
     --genomeDir /path/to/genomeDir \
     --genomeFastaFiles genome.fa \
     --sjdbGTFfile annotations.gtf \
     --sjdbOverhang 100
``` 

### Explanation of Parameters

- **`--runThreadN`**: Number of threads (adjust to available cores for faster processing).
- **`--genomeDir`**: Directory where the genome indices will be stored.
- **`--genomeFastaFiles`**: Path to the reference genome FASTA file(s). For multiple FASTA files, list them separated by spaces.
- **`--sjdbGTFfile`**: Path to the GTF annotation file for splice junction information.
- **`--sjdbOverhang`**: Read length minus 1 (e.g., for 101 bp reads, use 100).

## 3. Aligning RNA-seq Reads

After generating the genome index, you can align RNA-seq reads using STAR.

### Single-End Reads Example:

```bash
module load STAR/<version_number>
# Replace <version_number> with the desired version, e.g., module load STAR/2.7.9a

STAR --runThreadN 8 \
     --genomeDir /path/to/genomeDir \
     --readFilesCommand gunzip \
     --readFilesIn sample_R1.fastq \
     --outFileNamePrefix sample \
     --quantMode GeneCounts \
     --outReadsUnmapped Fastx \
     --chimSegmentMin 10 \
     --outSAMtype BAM SortedByCoordinate
```
### Paired-End Reads Example:

```bash
module load STAR/version_number 

STAR --runThreadN 8 \
     --genomeDir /path/to/genomeDir \
     --readFilesCommand gunzip \
     --readFilesIn sample_R1.fastq sample_R2.fastq \
     --outFileNamePrefix sample \
     --quantMode GeneCounts \
     --outReadsUnmapped Fastx \
     --chimSegmentMin 10 \
     --outSAMtype BAM SortedByCoordinate
```

### Explanation of Parameters

- **----readFilesIn**: 
Input FASTQ files (single or paired-end).

- **--outFileNamePrefix**: 
Prefix for output files.

- **--outSAMtype**: 
Specifies output format (e.g., sorted BAM file).

- **--runThreadN:**
Number of CPU threads to use. Adjust this based on the computational resources available on your cluster. Using more threads speeds up the process but requires more cores.

- **--genomeDir:**
Path to the directory containing the pre-generated STAR genome index. This directory is created using the --runMode genomeGenerate command (see the section on generating the genome index).

- **--readFilesCommand:**
Command used to preprocess the input FASTQ files. In this example, gunzip is specified, indicating that the input FASTQ files are compressed (.gz). For uncompressed files, this parameter is not needed.

- **--readFilesIn:**
Specifies the input FASTQ file(s) for alignment. For single-end reads, provide one file; for paired-end reads, provide both files separated by a space (e.g., sample_R1.fastq sample_R2.fastq).

- **--outFileNamePrefix:**
Specifies the prefix for all output files. STAR will append specific suffixes to this prefix to generate different output files (e.g., BAM files, logs).

- **--quantMode:**
Enables quantification of reads at the gene level. Using GeneCounts generates a file (ReadsPerGene.out.tab) that provides read counts for each gene, useful for downstream expression analysis.
   - Output includes three columns for each gene:
   - Uniquely mapped reads.
   - Reads mapped to both strands.
   - Reads mapped to the opposite strand.

- **--outSAMtype:**
Specifies the format of the output alignment file: 
   - **BAM Unsorted:** Produces an unsorted BAM file.
   - **BAM SortedByCoordinate:** 
      - Produces a sorted BAM file based on genomic coordinates, which is typically required for downstream tools like featureCounts or visualization in genome browsers.

- **--outReadsUnmapped:**
Specify whether to output unmapped reads. Options include Fastx to write unmapped reads in FASTQ format, which can be useful for troubleshooting or further analysis.

- **chimSegmentMin:**
Minimum length of chimeric alignments (e.g., for detecting fusion transcripts). Defaults to 0, but setting a value like 10 can help identify chimeric reads.

## STAR Output

STAR generates several output files. Key files include:

### Log Files
- **`Log.out`**: General log with alignment summary.
- **`Log.final.out`**: Detailed alignment statistics.
- **`Log.progress.out`**: Progress of the alignment process, including percentage completion.

### Alignment Files
- **`Aligned.sortedByCoord.out.bam`**: BAM file containing reads aligned to the reference genome, sorted by genomic coordinates.
- **`Aligned.out.bam`**: BAM file containing reads aligned to the reference genome (unsorted).

### Gene Counts
- **`ReadsPerGene.out.tab`**: File containing gene-level read counts, with three columns for each gene:
  - Uniquely mapped reads.
  - Reads mapped to both strands.
  - Reads mapped to the opposite strand.

### Unmapped Reads
- **`Unmapped.out.mate1`**: FASTQ file containing unmapped reads from the first mate (if specified).
- **`Unmapped.out.mate2`**: FASTQ file containing unmapped reads from the second mate (if specified).

### Splice Junctions
- **`SJ.out.tab`**: File listing detected splice junctions, including information about their genomic coordinates and supporting read counts.

### Chimeric Reads
- **`Chimeric.out.sam`**: SAM file containing chimeric (fusion) alignments, useful for identifying fusion transcripts.

**Several of these parameters are optional, for more details see:**
- https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf 

## Running STAR Alignments in Parallel Using `sbatch --array`

When processing multiple RNA-seq samples, you can use SLURM's `--array` option to run jobs in parallel. This approach is efficient for handling batch alignment tasks.

### 1. Preparing Input Files

Create a text file listing all your sample FASTQ file pairs, with one sample per line. For paired-end data, include both files separated by a space, like this:

**`samples.txt`:**


### 2. Writing the `sbatch` Script

Here's an example `sbatch` script to run STAR for each sample in the list using an array job:

**`run_star.sh`:**
```bash
#!/bin/bash
#SBATCH --job-name=STAR_array
#SBATCH --array=0-2                 # Set the range of job indices (adjust based on the number of samples)
#SBATCH --ntasks=1                  # Number of tasks per job
#SBATCH --cpus-per-task=8           # Number of CPUs per task
#SBATCH --mem=61440M                # Memory allocation per job
#SBATCH --p himem                   # Partition
#SBATCH -t 07:00:00                 # Max runtime 
#SBATCH --output=logs/star_%A_%a.log # Log file for each task

# Load STAR module
module load STAR

# Read the samples file to get the corresponding FASTQ files for this array task
SAMPLES_FILE="samples.txt"
LINE=$(sed -n "${SLURM_ARRAY_TASK_ID}p" $SAMPLES_FILE)
FASTQ1=$(echo $LINE | cut -d ' ' -f 1)
FASTQ2=$(echo $LINE | cut -d ' ' -f 2)

# Specify the genome directory and output directory
GENOME_DIR="/path/to/genomeDir"
OUTPUT_DIR="/path/to/output"

# Run STAR
STAR --runThreadN 8 \
     --genomeDir $GENOME_DIR \
     --readFilesCommand gunzip \
     --readFilesIn $FASTQ1 $FASTQ2 \
     --outFileNamePrefix $OUTPUT_DIR/sample_${SLURM_ARRAY_TASK_ID}_ \
     --outSAMtype BAM SortedByCoordinate
```
### 2. Submitting the Job

Submit the job array with the following command:

```bash
sbatch run_star.sh
```

### Explanation of Parameters

- **`--array=0-2`**: Specifies the range of indices for the job array. Adjust based on the number of lines in `samples.txt`. For example, if you have 10 samples, use `--array=0-9`.
- **`SLURM_ARRAY_TASK_ID`**: A unique identifier for each array task, corresponding to the line in `samples.txt`.
- **`sed -n "${SLURM_ARRAY_TASK_ID}p"`**: Extracts the line from `samples.txt` corresponding to the current array task.

### 4. Logs and Output
- **Logs**: Logs for each task will be saved in the `logs/` directory with filenames like `star_JOBID_TASKID.log`.
- **Output**: Aligned BAM files and other outputs will be saved in the specified `OUTPUT_DIR`.

