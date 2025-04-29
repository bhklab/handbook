# ORCESTRA Version Controlling

ORCESTRA is a project bound to the principles of reproducibility and transparency. This is because ORCESTRA is a dataset repository that provides key metadata for the pipelines, raw data, and tools needed to create the standardized datasets published to the platform. This ensures users of the datasets on our platform can be confident in the work we produce and even validate them. The transparency and reproducibility also ensures that platform users can take our metadata and create their own versions of our datasets by adding or omitting fields that we can include in our final datasets.

## What We Version Control

ORCESTRA is setup to version control several key components:

1. The Github repository to create the dataset + commitID used
2. The raw data sources and their versions
3. Tools and key packages used in the pipeline + their versions
4. The final data object DOI from Zenodo

Ensuring users have access to the above resources for each dataset on ORCESTRA we can be confident that users will be able to clearly understand how the dataset was created, what it's comprised of, and how one could recreate it.

## Where Does ORCESTRA Source Metadata

ORCESTRA sources the majority of the metadata for the web-app from the config.yaml file that is required in the pipeline Github repository. Upon the dataset being processed the fields for the raw data and tools are extracted directly from the .yaml file, the Github commitID is sourced from the pipeline repository, and the Zenodo DOI is sourced once the API uploads the processed dataset to the lab Zenodo account.