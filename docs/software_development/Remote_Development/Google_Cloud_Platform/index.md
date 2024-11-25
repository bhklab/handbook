# Introduction to Google Cloud Platform (GCP)

## Table of Contents

1. [What is Google Cloud Platform?](#1-what-is-google-cloud-platform)
2. [Why Use GCP?](#2-why-use-gcp)
3. [How to Use GCP](#3-how-to-use-gcp)
4. [Essential and Most Used GCP Services You May Use for Your Project](#essential-and-most-used-gcp-services-you-may-use-for-your-project)
   1. [Google Cloud Storage (GCS)](#1-google-cloud-storage-gcs)
   2. [BigQuery](#2-bigquery)
   3. [Cloud SQL for MySQL, PostgreSQL, and Microsoft SQL Server](#3-cloud-sql-for-mysql-postgresql-and-microsoft-sql-server)
   4. [Google Cloud Artifact Registry](#4-google-cloud-artifact-registry)

## 1. What is Google Cloud Platform?

Google Cloud Platform is a suite of cloud computing services offered by Google, providing a wide range of infrastructure and application services that can be accessed on-demand. It enables users to build, deploy, and scale applications seamlessly while taking advantage of Google’s powerful and reliable infrastructure.

## 2. Why Use GCP?

- **Scalability**: Easily scale resources up or down based on workload.

- **Pay-as-You-Go**: Only pay for what you use.

- **Integration**: Connect seamlessly with open-source and enterprise tools.

- **Global Infrastructure**: High-speed global network for faster operations.

## 3. How to Use GCP

### Prerequisites:

- Ensure you have an active Gmail account.
- Confirm that your account has been added to the relevant GCP project.

#### To access and use Google Cloud Platform (GCP), follow these steps:

#### Accessing GCP via the Console

- Visit the [Google Cloud Console](#https://console.cloud.google.com/) .

- Explore the dashboard to view, manage, and configure services, projects, and resources.

#### Accessing GCP via Terminal

**To interact with GCP directly from your terminal:**
**Step 1**: Initialize Google Cloud SDK

- Install the Google Cloud SDK on your machine by following the official installation guide (https://cloud.google.com/sdk/docs/install).

  ```
  gcloud init
  ```

- Follow the prompts to authenticate, select your project, and configure the settings.

**Step 2:** Authenticate Your Terminal

- Run the following command to authenticate:
  ```
  gcloud auth login
  ```
- This opens a browser window asking you to log in with your Google account.
- After login, your terminal will be authenticated, and you’ll see a confirmation message.

**Step 3:** Set the Active Project

- Ensure the correct project is set as the active one.

```
gcloud config set project <PROJECT_ID>
```

- Replace <PROJECT_ID> with your GCP project ID (e.g., bhklabproject-123).
- Verify the active project:
  ```
  gcloud config list project
  ```

## Essential and Most Used GCP Services You May Use for Your Project

Below are some key Google Cloud Platform (GCP) services that can be used for your project:

### 1. [Google Cloud Storage (GCS)](#1-google-cloud-storage-gcs)

### 2. [BigQuery](#2-bigquery)

### 3. [Cloud SQL for MySQL, PostgreSQL, and Microsoft SQL Server](#3-cloud-sql-for-mysql-postgresql-and-microsoft-sql-server)

### 4. [Google Cloud Artifact Registry](#4-google-cloud-artifact-registry)

## 1. Google Cloud Storage (GCS)

**Purpose**: Scalable and secure object storage for data files, datasets, and ML-ready data.

**Use Case**:

- Centralized storage for raw and processed datasets.
- Facilitates data sharing across team members.
- Integration with other GCP services like BigQuery and AI/ML tools.

**How to Use:**

- Ensure that you have completed [How to Use GCP](#3-how-to-use-gcp) before starting this process.

- Create a GCS Bucket:
  Use the GCP console, gcloud CLI, or API to create bucket

- **_Using Console_:**
  - Follow the instructions in this [documentation](https://cloud.google.com/storage/docs/creating-buckets#console) to create buckets.
- **_Using Command Line:_**
  In your development environment, run the gcloud storage buckets create command:
  `gcloud storage buckets create gs://<BUCKET_NAME> --location=<BUCKET_LOCATION>`

  Where:

  - BUCKET*NAME* is the name you want to give your bucket, subject to naming requirement. For example, my-bucket.

  - BUCKET*LOCATION* is the location of your bucket. For example, us-east1.

  If the request is successful, the command returns the following message:
  **Creating gs://BUCKET_NAME/...**

- **_Transfer Data:_**
  _From Local to GCS:_
  ```
  gsutil cp <local_file> gs://<bucket_name>
  ```
  _From GCS to Local:_
  ```
  gsutil cp gs://<bucket_name>/<file_name> <local_destination>
  ```

## **2. BigQuery**

It is a SQL-based data warehouse that allows you to process, load, and analyze data efficiently using SQL queries.
**Purpose**: A powerful data warehouse for querying, analyzing, and preprocessing large datasets.

**Use Case**:

- Quickly preprocess and explore large datasets using SQL like query.
- Simplifies aggregation, feature extraction, and preparation for ML models.
- You can directly load data from a GCS bucket into an SQL-based data warehouse (BigQuery). It supports all types of data—structured, semi-structured, and unstructured, including tsv, csv, parquet, avro, xlsx, and many more.
- To use BigQuery with a client library, please follow this [link](#https://cloud.google.com/bigquery/docs/reference/libraries) for detailed guidance.
- **How to Use:**

* Ensure that you have completed [How to Use GCP](#3-how-to-use-gcp) before starting this process.\*

1. **Load Data into BigQuery**:  
   From GCS:
   ```
   bq load --source_format=CSV <DATASET_NAME>.<TABLE_NAME> gs://<BUCKET_NAME>/<FILE_NAME>
   ```
2. **Query Data**:  
   Use BigQuery's web interface or CLI to run SQL queries for data cleaning, feature engineering, and exploratory analysis.
   Example:
   ````
   SELECT * FROM `project_id.dataset_name.table_name` LIMIT 10;```
   ````

**Follow the instructions in this [document](#https://cloud.google.com/bigquery/docs) to learn more about BigQuery**

## 3. Cloud SQL for MySQL, PostgreSQL, and Microsoft SQL Server

Google Cloud SQL is a fully-managed relational database service for MySQL, PostgreSQL, and Microsoft SQL Server. It eliminates the need for database maintenance while offering high availability, scalability, and security. Below is a comprehensive guide to using Cloud SQL effectively for your projects.

### **Why Use Cloud SQL?**

1. **Managed Service**: Automated backups, updates, and maintenance.
2. **Scalability**: Seamless scaling for growing workloads.
3. **Security**: Built-in encryption, IAM-based access, and network security.
4. **Integration**: Works seamlessly with GCP services like Compute Engine, Kubernetes Engine, and BigQuery.
5. **Flexibility**: Supports popular relational databases: MySQL, PostgreSQL, and Microsoft SQL Server.

### **Setting Up Cloud SQL**

Ensure that you have completed [How to Use GCP](#3-how-to-use-gcp) before starting this process.\_

#### **Step 1: Enable the Cloud SQL API**

```
gcloud services enable sqladmin.googleapis.com
```

#### **Step 2: Create a Cloud SQL Instance**

**MySQL Example**:

```
gcloud sql instances create [INSTANCE_NAME] \ --database-version=MYSQL_8_0 \ --cpu=[CPU_COUNT] \ --memory=[MEMORY_SIZE] \ --region=[REGION]

```

**PostgreSQL Example**:
`gcloud sql instances create [INSTANCE_NAME] \
    --database-version=POSTGRES_14 \
    --cpu=[CPU_COUNT] \
    --memory=[MEMORY_SIZE] \
    --region=[REGION]  `

**Parameters**:

- `--cpu`: Number of vCPUs (e.g., 2).
- `--memory`: RAM allocation (e.g., 4GB).
- `--region`: Choose a region (e.g., `us-central1`).

#### Step 3: Configure Users and Databases

**Create a Database**:

```
gcloud sql databases create [DATABASE_NAME] --instance=[INSTANCE_NAME]
```

**Add a User**:

```
gcloud sql users create [USERNAME] --password=[PASSWORD] --instance=[INSTANCE_NAME]
```

**For a detailed guide on using client services, please refer to this [link](#https://cloud.google.com/sql/docs)**

### **3. Virtual Machines (VMs)**

A Cloud VM is a scalable, on-demand virtual machine hosted in the cloud. It functions like a physical computer, providing compute power, memory, storage, and network connectivity. Cloud VMs are versatile and can be used for a variety of tasks, from running applications and hosting websites to managing databases and performing intensive data processing.

**Purpose**: Flexible compute instances to run custom ML experiments, manage pipelines, or host applications.

#### How It Helps:

- Ideal for workloads requiring full control over the environment, OS, and configurations.
- Provides isolated environments for training ML models.
- Supports GPU/TPU acceleration for deep learning tasks.
- Can host containerized ML workflows using Docker.

#### How to Use:

_Ensure that you have completed [How to Use GCP](#3-how-to-use-gcp) before starting this process._

1. **Create a GPU-Enabled VM for Model Training**:

```
gcloud compute instances create $INSTANCE_NAME \  --zone=$ZONE \  --image-family=$IMAGE_FAMILY \  --image-project=deeplearning-platform-release \  --maintenance-policy=TERMINATE \  --accelerator="type=nvidia-tesla-v100,count=1" \  --metadata="install-nvidia-driver=True"
```

Parameters:

- `--image-family` must be one of the GPU-specific image types. For more information, see [Choosing an Image](https://cloud.google.com/deep-learning-vm/docs/images).
- `--image-project` must be `deeplearning-platform-release`.
- `--maintenance-policy` must be `TERMINATE`. See [GPU Restrictions](https://cloud.google.com/compute/docs/gpus#restrictions) to learn more.
- `--accelerator` specifies the GPU type to use. Must be specified in the format `--accelerator="type=TYPE,count=COUNT"`. Supported values of `TYPE` are:
  - `nvidia-tesla-v100` (`count=1` or `8`)
  - `nvidia-tesla-p100` (`count=1`, `2`, or `4`)
  - `nvidia-tesla-p4` (`count=1`, `2`, or `4`)

## 4. Google Cloud Artifact Registry

Google Cloud Artifact Registry is a fully-managed service for storing and managing container images, as well as other software artifacts like Maven, npm, and Python packages. It is designed to integrate seamlessly with GCP, providing enhanced security, authentication, and efficiency over external services like Docker Hub.

#### **Why Use Artifact Registry Instead of Docker Hub?**

---

| Feature               | Docker Hub                                                                      | Artifact Registry                                                                                          |
| --------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Security**          | Publicly accessible by default. Limited security features unless on paid tiers. | Private by default, with IAM-based fine-grained access control and integration with GCP security features. |
| **Authentication**    | Separate login credentials required.                                            | Uses GCP-managed identities (IAM roles and service accounts).                                              |
| **Network Proximity** | External to GCP, introducing latency.                                           | Hosted within GCP, reducing latency and egress costs.                                                      |
| **Cost**              | Free tier has pull limits. Paid plans for more.                                 | Pay only for what you store and access.                                                                    |
| **Integration**       | Limited GCP integration.                                                        | Full integration with GCP services like Cloud Build, Compute Engine, and Kubernetes Engine.                |

---

### **Setting Up and Using Artifact Registry**

- Ensure that you have completed [How to Use GCP](#3-how-to-use-gcp) before starting this process.

#### **Step 1: Enable Artifact Registry API**

```
gcloud services enable artifactregistry.googleapis.com
```

#### **Step 2: Create an Artifact Repository**

**Command**:

```
gcloud artifacts repositories create [REPOSITORY_NAME] \
    --repository-format=docker \
    --location=[REGION] \
    --description="Repository for storing Docker images"
```

#### **Step 3: Authenticate Docker with Artifact Registry**

Run the following command to configure Docker to authenticate with your Artifact Registry:

```
gcloud auth configure-docker [REGION]-docker.pkg.dev
```

#### **Step 4: Push Images to Artifact Registry**

1. Tag your Docker image for Artifact Registry:

```
   docker tag [IMAGE_NAME] [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/[IMAGE_NAME]:[TAG]
```

2. Push the image:

```
  docker push [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/[IMAGE_NAME]:[TAG]
```

#### **Step 5: Pull Images from Artifact Registry**

To pull an image from your repository:

```
docker pull [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/[IMAGE_NAME]:[TAG]
```
