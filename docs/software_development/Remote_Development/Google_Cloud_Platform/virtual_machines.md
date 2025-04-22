# GCP Virtual Machines (VMs)

A Cloud VM is a scalable, on-demand virtual machine hosted in the cloud. It
functions like a physical computer, providing compute power, memory, storage,
and network connectivity. Cloud VMs are versatile and can be used for a variety
of tasks, from running applications and hosting websites to managing databases
and performing intensive data processing.

In summary, VMs offer flexible compute instances to run custom ML experiments,
manage pipelines, or host applications.

## Why Use Cloud VMs?

- Ideal for workloads requiring full control over the environment, OS, and
    configurations.
- Provides isolated environments for training ML models.
- Supports GPU/TPU acceleration for deep learning tasks.
- Can host containerized ML workflows using Docker.

## Setting Up and Using GCP VMs

> Ensure that you have completed [How to Use GCP](introduction.md#how-to-use-gcp)
> before starting this process.

### Creating a GPU-Enabled VM for Model Training

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

- `--image-family` must be one of the GPU-specific image types. For more
    information, see [Choosing an Image](https://cloud.google.com/deep-learning-vm/docs/images).
- `--image-project` must be `deeplearning-platform-release`.
- `--maintenance-policy` must be `TERMINATE`. For more information, see
    [GPU Restrictions](https://cloud.google.com/compute/docs/gpus#restrictions).
- `--accelerator` specifies the GPU type to use. Must be specified in the
    format `--accelerator="type=TYPE,count=COUNT"`. Supported values of
    `TYPE` are:
    - `nvidia-tesla-v100`, (`count=1` or `8`)
    - `nvidia-tesla-p100`, (`count=1`, `2`, or `4`)
    - `nvidia-tesla-p4`, (`count=1`, `2`, or `4`)
