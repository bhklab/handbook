# Google Cloud Storage (GCS)

GCS is a scalable and secure object storage for data files, datasets, and
ML-ready data.

## Why Use GCS?

- Centralized storage for raw and processed datasets.
- Facilitates data sharing across team members.
- Integration with other GCP services like BigQuery and AI/ML tools.

## Setting Up and Using GCS

> Ensure that you have completed [How to Use GCP](introduction.md#how-to-use-gcp)
> before starting this process.

Use the GCP console, gcloud CLI, or API to create a bucket:

### Creating a GCS Bucket via Cloud Console

- Follow the instructions in this [documentation](https://cloud.google.com/storage/docs/creating-buckets#console)
    to create buckets.

### Creating a GCS Bucket via Terminal

- In your development environment, run the `gcloud storage buckets create`
    command:

    ```sh
    gcloud storage buckets create gs://<BUCKET_NAME> --location=<BUCKET_LOCATION>
    ```

    Where:
    - `<BUCKET_NAME>` is the name you want to give your bucket, subject to
        naming requirement. For example, `my-bucket`.
    - `<BUCKET_LOCATION>` is the location of your bucket. For example,
        `us-east1`.
- If the request is successful, the command returns the following
    message:

    ```console
    Creating gs://BUCKET_NAME/...
    ```

### Transferring Data Across GCS

- _From Local to GCS_:

    ```sh
    gsutil cp <local_file> gs://<bucket_name>
    ```

- _From GCS to Local_:

    ```sh
    gsutil cp gs://<bucket_name>/<file_name> <local_destination>
    ```
