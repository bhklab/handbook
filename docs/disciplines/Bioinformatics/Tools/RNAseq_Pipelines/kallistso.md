# Kallistso

Kallisto is a lightweight, ultra-fast RNA-seq quantification tool.
It is mainly used for estimating transcript abundances directly from RNA-seq reads without performing full read alignment.
A detailed tutorial is available [here](https://pachterlab.github.io/kallisto/starting).

## Key features
 - **Alignment-free**:
Kallisto does not align reads base-by-base to the genome.
Instead, it uses a technique called pseudoalignment to quickly determine which transcript reads are compatible with.
 - **Extremely fast**:
It is significantly faster than traditional aligners like STAR and HISAT2 because it skips full alignment.
 - **Quantification**:
Directly outputs transcript abundance estimates such as **TPM** (Transcripts Per Million).
 - **Low memory usage**:
Efficient enough to run on laptops or small servers.

## Download
Kallistso is already installed on H4H. 
If you would like to install it on your local computer, please follow [these instructions](https://pachterlab.github.io/kallisto/download). 

## Workflow:
 - **Step 1: Build a transcriptome index** (from a reference transcriptome FASTA file)
```
kallisto index -i transcriptome.idx transcripts.fa
```
 - **Step 2: Quantify RNA-seq reads** (Pseudoalignment and abundance estimation)
```
kallisto quant -i transcriptome.idx -o output_dir -b 100 reads_1.fastq reads_2.fastq
```
-b 100 specifies 100 bootstrap samples for estimating quantification uncertainty.

## Outputs
 - `abundance.tsv` — Main quantification table (TPM, estimated counts)
 - `abundance.h5` - Binary HDF5 file containing the same information as `abundance.tsv`, plus bootstrap results if bootstrapping was performed.
 - `run_info.json` — Summary of the Kallisto run (e.g., number of processed reads, parameters used).


## Usage
 - A Snakemake Kallistso pipeline is available at H4H: `/cluster/projects/bhklab/pipelines/kallisto_snakemake_pipeline`
 - Details about pipeline setup and usage are available in the pipeline's `README` file. 