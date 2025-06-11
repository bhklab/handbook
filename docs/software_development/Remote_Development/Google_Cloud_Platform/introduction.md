# Introduction to Google Cloud Platform (GCP)

## What is Google Cloud Platform?

Google Cloud Platform is a suite of cloud computing services offered by Google,
providing a wide range of infrastructure and application services that can be
accessed on-demand. It enables users to build, deploy, and scale applications
seamlessly while taking advantage of Google’s powerful and reliable
infrastructure.

## Why Use GCP?

- **Scalability**: Easily scale resources up or down based on workload.
- **Pay-as-You-Go**: Only pay for what you use.
- **Integration**: Connect seamlessly with open-source and enterprise tools.
- **Global Infrastructure**: High-speed global network for faster operations.

## How to Use GCP

> Prerequisites:
>
> - Ensure you have an active Google account.
> - Confirm that your account has been added to the relevant GCP project.

To access and use Google Cloud Platform (GCP), follow these steps:

### Accessing GCP via the Cloud Console

- Visit the [Google Cloud Console](https://console.cloud.google.com/).
- Explore the dashboard to view, manage, and configure services, projects, and
    resources.

### Accessing GCP via Terminal

To interact with GCP directly from your terminal:

1. **Initialize Google Cloud SDK**
    - Install the Google Cloud SDK on your machine by following the official
      [installation guide](https://cloud.google.com/sdk/docs/install), then use
      the following command:

        ```sh
        gcloud init
        ```

    - Follow the prompts to authenticate, select your project, and configure the
      settings.

2. **Authenticate Your Terminal**
    - Run the following command to authenticate:

        ```sh
        gcloud auth login
        ```

    - This opens a browser window asking you to log in with your Google account.
    - After login, your terminal will be authenticated, and you’ll see a
      confirmation message.

3. **Set the Active Project**
    - Ensure the correct project is set as the active one.

        ```sh
        gcloud config set project <PROJECT_ID>
        ```

    - Replace `<PROJECT_ID>` with your GCP project ID (e.g., `bhklabproject-123`).
    - Verify the active project:

        ```sh
        gcloud config list project
        ```

## Commonly Used GCP Services

Below are some key Google Cloud Platform (GCP) services that can be used for
your project:

- [Google Cloud Storage (GCS)](gcs.md) - Scalable and secure object storage for data files, datasets, and ML-ready data
- [BigQuery](bigquery.md) - SQL-based data warehouse for processing and analyzing large datasets
- [Cloud SQL](cloud_sql.md) - Fully-managed relational database service for MySQL, PostgreSQL, and Microsoft SQL Server
- [Virtual Machines (VMs)](virtual_machines.md) - Scalable, on-demand virtual machines for running custom ML experiments
- [Artifact Registry](artifact_registry.md) - Fully-managed service for storing and managing container images and software artifacts

Each service page provides detailed information about why to use the service and step-by-step setup instructions.
