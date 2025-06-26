# Output


```shell
(base) jamesbannon@Jamess-MacBook-Pro-2 gdsc-treatmentresponse-snakemake % pixi run pipeline
✨ Pixi task (pipeline in snakemake): snakemake --cores all --use-apptainer --use-conda: (Run snakemake pipeline)
Assuming unrestricted shared filesystem usage.
host: Jamess-MacBook-Pro-2.local
Building DAG of jobs... /Users/jamesbannon/Desktop/pipe_test/gdsc-treatmentresponse-snakemake/.pixi/envs/snakemake/lib/python3.12/site-packages/conda/base/context.py:198: FutureWarning: Adding 'defaults' to channel list implicitly is deprecated and will be removed in 25.9. 

To remove this warning, please choose a default channel explicitly with conda's regular configuration system, e.g. by adding 'defaults' to the list of channels:

  conda config --add channels defaults

For more information see https://docs.conda.io/projects/conda/en/stable/user-guide/configuration/use-condarc.html

  deprecated.topic(
Your conda installation is not configured to use strict channel priorities. This is however important for having robust and correct environments (for details, see https://conda-forge.org/docs/user/tipsandtricks.html). Please consider to configure strict priorities by executing 'conda config --set channel_priority strict'.
Creating conda environment workflow/envs/treatmentResponse.yaml...
Downloading and installing remote packages.
CreateCondaEnvironmentException:
Could not create conda environment from /Users/jamesbannon/Desktop/pipe_test/gdsc-treatmentresponse-snakemake/workflow/envs/treatmentResponse.yaml:
Command:
conda env create --quiet --no-default-packages --file "/Users/jamesbannon/Desktop/pipe_test/gdsc-treatmentresponse-snakemake/.snakemake/conda/d7b965ffb6853289b6fb1c878b3c6504_.yaml" --prefix "/Users/jamesbannon/Desktop/pipe_test/gdsc-treatmentresponse-snakemake/.snakemake/conda/d7b965ffb6853289b6fb1c878b3c6504_"
Output:
/Users/jamesbannon/Desktop/pipe_test/gdsc-treatmentresponse-snakemake/.pixi/envs/snakemake/lib/python3.12/site-packages/conda/base/context.py:198: FutureWarning: Adding 'defaults' to channel list implicitly is deprecated and will be removed in 25.9. 

To remove this warning, please choose a default channel explicitly with conda's regular configuration system, e.g. by adding 'defaults' to the list of channels:

  conda config --add channels defaults

For more information see https://docs.conda.io/projects/conda/en/stable/user-guide/configuration/use-condarc.html

  deprecated.topic(
Retrieving notices: ...working... done
Channels:
 - conda-forge
 - bioconda
 - defaults
Platform: osx-arm64
Collecting package metadata (repodata.json): ...working... done
Solving environment: ...working... failed

LibMambaUnsatisfiableError: Encountered problems while solving:
  - unsupported request
  - nothing provides bioconductor-biocparallel >=1.36.0,<1.37.0 needed by bioconductor-coregx-2.6.0-r43hdfd78af_0
  - unsupported request
  - unsupported request
  - unsupported request
  - unsupported request

Could not solve for environment specs
The following packages are incompatible
├─ bioconductor-biocparallel =1.36.0 * does not exist (perhaps a typo or a missing channel);
├─ bioconductor-coregx =2.6.0 * is not installable because it requires
│  └─ bioconductor-biocparallel >=1.36.0,<1.37.0 *, which does not exist (perhaps a missing channel);
├─ bioconductor-genomicranges =1.54.1 * does not exist (perhaps a typo or a missing channel);
├─ bioconductor-pharmacogx =3.6.0 * does not exist (perhaps a typo or a missing channel);
├─ r-log4r =0.4.3 * does not exist (perhaps a typo or a missing channel);
└─ r-qs =0.25 * does not exist (perhaps a typo or a missing channel).

```