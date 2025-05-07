# Google Cloud Artifact Registry

Google Cloud Artifact Registry is a fully-managed service for storing and
managing container images, as well as other software artifacts like Maven, npm,
and Python packages. It is designed to integrate seamlessly with GCP, providing
enhanced security, authentication, and efficiency over external services like
Docker Hub.

## Why Use Artifact Registry Instead of Docker Hub?

| Feature               | Docker Hub                                                                      | Artifact Registry                                                                                          |
| --------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Security**          | Publicly accessible by default. Limited security features unless on paid tiers. | Private by default, with IAM-based fine-grained access control and integration with GCP security features. |
| **Authentication**    | Separate login credentials required.                                            | Uses GCP-managed identities (IAM roles and service accounts).                                              |
| **Network Proximity** | External to GCP, introducing latency.                                           | Hosted within GCP, reducing latency and egress costs.                                                      |
| **Cost**              | Free tier has pull limits. Paid plans for more.                                 | Pay only for what you store and access.                                                                    |
| **Integration**       | Limited GCP integration.                                                        | Full integration with GCP services like Cloud Build, Compute Engine, and Kubernetes Engine.                |

## Setting Up and Using Artifact Registry

> Ensure that you have completed [How to Use GCP](introduction.md#how-to-use-gcp)
> before starting this process.

### Enabling the Artifact Registry API

```sh
gcloud services enable artifactregistry.googleapis.com
```

### Creating an Artifact Repository

```sh
gcloud artifacts repositories create [REPOSITORY_NAME] \
    --repository-format=docker \
    --location=[REGION] \
    --description="Repository for storing Docker images"
```

### Authenticating Docker with Artifact Registry

Run the following command to configure Docker to authenticate with your Artifact
Registry:

```sh
gcloud auth configure-docker [REGION]-docker.pkg.dev
```

### Pushing Images to Artifact Registry

1. Tag your Docker image for Artifact Registry:

    ```sh
    docker tag [IMAGE_NAME] [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/[IMAGE_NAME]:[TAG]
    ```

2. Push the image:

    ```sh
    docker push [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/[IMAGE_NAME]:[TAG]
    ```

### Pulling Images from Artifact Registry

```sh
docker pull [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/[IMAGE_NAME]:[TAG]
```
