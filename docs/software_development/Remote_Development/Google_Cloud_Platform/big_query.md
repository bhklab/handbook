# BigQuery

BigQuery is a powerful SQL-based data warehouse that allows you to process,
load, and analyze large datasets efficiently using SQL queries.

## Why Use BigQuery?

- Quickly preprocess and explore large datasets using SQL-like query.
- Simplifies aggregation, feature extraction, and preparation for ML models.
- You can directly load data from a GCS bucket into an SQL-based data
    warehouse (BigQuery). It supports all types of data &mdash; structured,
    semi-structured, and unstructured; including tsv, csv, parquet, avro, xlsx,
    and many more.
- To use BigQuery with a client library, please follow this [link](https://cloud.google.com/bigquery/docs/reference/libraries)
    for detailed guide.

## Setting Up and Using BigQuery

> Ensure that you have completed [How to Use GCP](introduction.md#how-to-use-gcp)
> before starting this process.

### Loading Data into BigQuery

- From GCS:

    ```sh
    bq load --source_format=CSV <DATASET_NAME>.<TABLE_NAME> gs://<BUCKET_NAME>/<FILE_NAME>
    ```

### Querying Data

- Use BigQuery's web interface or CLI to run SQL queries for data cleaning,
    feature engineering, and exploratory analysis.
- Example:

    ```sql
    SELECT * FROM `project_id.dataset_name.table_name` LIMIT 10;
    ```

> Follow the instructions on this [page](https://cloud.google.com/bigquery/docs)
> to learn more about BigQuery.
