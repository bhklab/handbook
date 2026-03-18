# Snakemake

[Snakemake](https://snakemake.github.io) is a workflow management system that allows you to create reproducible and scalable data analysis pipelines. It is particularly useful for bioinformatics and data science projects, where complex workflows often involve multiple steps and dependencies. For more general information and tutorials, visit their [official documentation](https://snakemake.readthedocs.io/en/stable/).

## Usage in the Lab

Many of our internal data processing pipelines are built using Snakemake, such as the [RNA-seq Kallisto pipeline](../../Bioinformatics/Tools/RNAseq_Pipelines/kallisto.md#usage), and we also use it to run pipelines for the [ORCESTRA](orcestra.md) platform.

Using Snakemake with the SLURM executor plugin allows us to efficiently manage and execute workflows on high-performance computing clusters, namely H4H. This is especially helpful for large-scale data processing tasks that require significant computational resources and time.

We host many of our Snakemake workflows, such as ORCESTRA PSet processing pipelines, in our [BHKLAB_DataProcessing Github organization](https://github.com/BHKLAB-DataProcessing).

## See Also

- [BHKLAB H4H Website](https://bhklab.github.io/HPC4Health/)
