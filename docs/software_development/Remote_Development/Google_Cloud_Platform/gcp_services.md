# Commonly Used GCP Services

Below are some key Google Cloud Platform (GCP) services that can be used for
your project:

## Google Cloud Storage (GCS)

GCS is a scalable and secure object storage for data files, datasets, and
ML-ready data.

### Why Use GCS?

-   Centralized storage for raw and processed datasets.
-   Facilitates data sharing across team members.
-   Integration with other GCP services like BigQuery and AI/ML tools.

### Setting Up and Using GCS

> Ensure that you have completed [How to Use GCP](index.md#3-how-to-use-gcp)
> before starting this process.

Use the GCP console, gcloud CLI, or API to create a bucket:

#### Creating a GCS Bucket via Cloud Console

-   Follow the instructions in this [documentation](https://cloud.google.com/storage/docs/creating-buckets#console)
    to create buckets.

#### Creating a GCS Bucket via Terminal

-   In your development environment, run the `gcloud storage buckets create`
    command:
    ```sh
    gcloud storage buckets create gs://<BUCKET_NAME> --location=<BUCKET_LOCATION>
    ```
    Where:
    -   `<BUCKET_NAME>` is the name you want to give your bucket, subject to
        naming requirement. For example, `my-bucket`.
    -   `<BUCKET_LOCATION>` is the location of your bucket. For example,
        `us-east1`.
-   If the request is successful, the command returns the following
    message:
    ```console
    Creating gs://BUCKET_NAME/...
    ```

#### Transferring Data Across GCS

-   _From Local to GCS_:
    ```sh
    gsutil cp <local_file> gs://<bucket_name>
    ```
-   _From GCS to Local_:
    ```sh
    gsutil cp gs://<bucket_name>/<file_name> <local_destination>
    ```

## BigQuery

BigQuery is a powerful SQL-based data warehouse that allows you to process,
load, and analyze large datasets efficiently using SQL queries.

### Why Use BigQuery?

-   Quickly preprocess and explore large datasets using SQL-like query.
-   Simplifies aggregation, feature extraction, and preparation for ML models.
-   You can directly load data from a GCS bucket into an SQL-based data
    warehouse (BigQuery). It supports all types of data &mdash; structured,
    semi-structured, and unstructured; including tsv, csv, parquet, avro, xlsx,
    and many more.
-   To use BigQuery with a client library, please follow this [link](#https://cloud.google.com/bigquery/docs/reference/libraries)
    for detailed guide.

### Setting Up and Using BigQuery

> Ensure that you have completed [How to Use GCP](index.md#3-how-to-use-gcp)
> before starting this process.

#### Loading Data into BigQuery

-   From GCS:
    ```sh
    bq load --source_format=CSV <DATASET_NAME>.<TABLE_NAME> gs://<BUCKET_NAME>/<FILE_NAME>
    ```

#### Querying Data

-   Use BigQuery's web interface or CLI to run SQL queries for data cleaning,
    feature engineering, and exploratory analysis.
-   Example:
    ```sql
    SELECT * FROM `project_id.dataset_name.table_name` LIMIT 10;
    ```

> Follow the instructions on this [page](https://cloud.google.com/bigquery/docs)
> to learn more about BigQuery.

## Cloud SQL for MySQL, PostgreSQL, and Microsoft SQL Server

Google Cloud SQL is a fully-managed relational database service for MySQL,
PostgreSQL, and Microsoft SQL Server. It eliminates the need for database
maintenance while offering high availability, scalability, and security. Below
is a comprehensive guide to using Cloud SQL effectively for your projects.

### Why Use Cloud SQL?

-   **Managed Service**: Automated backups, updates, and maintenance.
-   **Scalability**: Seamless scaling for growing workloads.
-   **Security**: Built-in encryption, IAM-based access, and network security.
-   **Integration**: Works seamlessly with GCP services like Compute Engine,
    Kubernetes Engine, and BigQuery.
-   **Flexibility**: Supports popular relational databases: MySQL, PostgreSQL,
    and Microsoft SQL Server.

### Setting Up and Using Cloud SQL

> Ensure that you have completed [How to Use GCP](index.md#3-how-to-use-gcp)
> before starting this process.

#### Enabling the Cloud SQL API

```sh
gcloud services enable sqladmin.googleapis.com
```

#### Creating a Cloud SQL Instance

-   _Example Using MySQL_:
    ```sh
    gcloud sql instances create [INSTANCE_NAME] \
        --database-version=MYSQL_8_0 \
        --cpu=[CPU_COUNT] \
        --memory=[MEMORY_SIZE] \
        --region=[REGION]
    ```
-   _Example using PostgreSQL_:
    ```sh
    gcloud sql instances create [INSTANCE_NAME] \
        --database-version=POSTGRES_14 \
        --cpu=[CPU_COUNT] \
        --memory=[MEMORY_SIZE] \
        --region=[REGION]
    ```
-   Parameters:
    -   `--cpu`: Number of vCPUs (e.g., 2).
    -   `--memory`: RAM allocation (e.g., 4GB).
    -   `--region`: Choose a region (e.g., `us-central1`).

#### Configuring Users and Databases

Using the same `INSTANCE_NAME` as configured in the previous step:

-   Create a Database with the command below:
    ```sh
    gcloud sql databases create [DATABASE_NAME] --instance=[INSTANCE_NAME]
    ```
-   Add a User with the command below:
    ```sh
    gcloud sql users create [USERNAME] --password=[PASSWORD] --instance=[INSTANCE_NAME]
    ```

> For a detailed guide on using client services, please refer to this
> [link](https://cloud.google.com/sql/docs)

## GCP Virtual Machines (VMs)

A Cloud VM is a scalable, on-demand virtual machine hosted in the cloud. It
functions like a physical computer, providing compute power, memory, storage,
and network connectivity. Cloud VMs are versatile and can be used for a variety
of tasks, from running applications and hosting websites to managing databases
and performing intensive data processing.

In summary, VMs offer flexible compute instances to run custom ML experiments,
manage pipelines, or host applications.

### Why Use Cloud VMs?

-   Ideal for workloads requiring full control over the environment, OS, and
    configurations.
-   Provides isolated environments for training ML models.
-   Supports GPU/TPU acceleration for deep learning tasks.
-   Can host containerized ML workflows using Docker.

### Setting Up and Using GCP VMs

> Ensure that you have completed [How to Use GCP](index.md#3-how-to-use-gcp)
> before starting this process.

#### Creating a GPU-Enabled VM for Model Training

```sh
gcloud compute instances create $INSTANCE_NAME \
    --zone=$ZONE \
    --image-family=$IMAGE_FAMILY \
    --image-project=deeplearning-platform-release \
    --maintenance-policy=TERMINATE \
    --accelerator="type=nvidia-tesla-v100,count=1" \
    --metadata="install-nvidia-driver=True"
```

Parameters:

-   `--image-family` must be one of the GPU-specific image types. For more
    information, see [Choosing an Image](https://cloud.google.com/deep-learning-vm/docs/images).
-   `--image-project` must be `deeplearning-platform-release`.
-   `--maintenance-policy` must be `TERMINATE`. For more information, see
    [GPU Restrictions](https://cloud.google.com/compute/docs/gpus#restrictions).
-   `--accelerator` specifies the GPU type to use. Must be specified in the
    format `--accelerator="type=TYPE,count=COUNT"`. Supported values of
    `TYPE` are:
    -   `nvidia-tesla-v100`, (`count=1` or `8`)
    -   `nvidia-tesla-p100`, (`count=1`, `2`, or `4`)
    -   `nvidia-tesla-p4`, (`count=1`, `2`, or `4`)

## Google Cloud Artifact Registry

Google Cloud Artifact Registry is a fully-managed service for storing and
managing container images, as well as other software artifacts like Maven, npm,
and Python packages. It is designed to integrate seamlessly with GCP, providing
enhanced security, authentication, and efficiency over external services like
Docker Hub.

### Why Use Artifact Registry Instead of Docker Hub?

| Feature               | Docker Hub                                                                      | Artifact Registry                                                                                          |
| --------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Security**          | Publicly accessible by default. Limited security features unless on paid tiers. | Private by default, with IAM-based fine-grained access control and integration with GCP security features. |
| **Authentication**    | Separate login credentials required.                                            | Uses GCP-managed identities (IAM roles and service accounts).                                              |
| **Network Proximity** | External to GCP, introducing latency.                                           | Hosted within GCP, reducing latency and egress costs.                                                      |
| **Cost**              | Free tier has pull limits. Paid plans for more.                                 | Pay only for what you store and access.                                                                    |
| **Integration**       | Limited GCP integration.                                                        | Full integration with GCP services like Cloud Build, Compute Engine, and Kubernetes Engine.                |

### Setting Up and Using Artifact Registry

> Ensure that you have completed [How to Use GCP](index.md#3-how-to-use-gcp)
> before starting this process.

#### Enabling the Artifact Registry API

```sh
gcloud services enable artifactregistry.googleapis.com
```

#### Creating an Artifact Repository

```sh
gcloud artifacts repositories create [REPOSITORY_NAME] \
    --repository-format=docker \
    --location=[REGION] \
    --description="Repository for storing Docker images"
```

#### Authenticating Docker with Artifact Registry

Run the following command to configure Docker to authenticate with your Artifact
Registry:

```sh
gcloud auth configure-docker [REGION]-docker.pkg.dev
```

#### Pushing Images to Artifact Registry

1. Tag your Docker image for Artifact Registry:
    ```sh
    docker tag [IMAGE_NAME] [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/[IMAGE_NAME]:[TAG]
    ```
2. Push the image:
    ```sh
    docker push [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/[IMAGE_NAME]:[TAG]
    ```

#### Pulling Images from Artifact Registry

```sh
docker pull [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/[IMAGE_NAME]:[TAG]
```
