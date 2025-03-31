# Cloud SQL for MySQL, PostgreSQL, and Microsoft SQL Server

Google Cloud SQL is a fully-managed relational database service for MySQL,
PostgreSQL, and Microsoft SQL Server. It eliminates the need for database
maintenance while offering high availability, scalability, and security. Below
is a comprehensive guide to using Cloud SQL effectively for your projects.

## Why Use Cloud SQL?

- **Managed Service**: Automated backups, updates, and maintenance.
- **Scalability**: Seamless scaling for growing workloads.
- **Security**: Built-in encryption, IAM-based access, and network security.
- **Integration**: Works seamlessly with GCP services like Compute Engine,
    Kubernetes Engine, and BigQuery.
- **Flexibility**: Supports popular relational databases: MySQL, PostgreSQL,
    and Microsoft SQL Server.

## Setting Up and Using Cloud SQL

> Ensure that you have completed [How to Use GCP](introduction.md#how-to-use-gcp)
> before starting this process.

### Enabling the Cloud SQL API

```sh
gcloud services enable sqladmin.googleapis.com
```

### Creating a Cloud SQL Instance

- _Example Using MySQL_:

    ```sh
    gcloud sql instances create [INSTANCE_NAME] \
        --database-version=MYSQL_8_0 \
        --cpu=[CPU_COUNT] \
        --memory=[MEMORY_SIZE] \
        --region=[REGION]
    ```

- _Example using PostgreSQL_:

    ```sh
    gcloud sql instances create [INSTANCE_NAME] \
        --database-version=POSTGRES_14 \
        --cpu=[CPU_COUNT] \
        --memory=[MEMORY_SIZE] \
        --region=[REGION]
    ```

- Parameters:
    - `--cpu`: Number of vCPUs (e.g., 2).
    - `--memory`: RAM allocation (e.g., 4GB).
    - `--region`: Choose a region (e.g., `us-central1`).

### Configuring Users and Databases

Using the same `INSTANCE_NAME` as configured in the previous step:

- Create a Database with the command below:

    ```sh
    gcloud sql databases create [DATABASE_NAME] --instance=[INSTANCE_NAME]
    ```

- Add a User with the command below:

    ```sh
    gcloud sql users create [USERNAME] --password=[PASSWORD] --instance=[INSTANCE_NAME]
    ```

> For a detailed guide on using client services, please refer to this
> [link](https://cloud.google.com/sql/docs)
