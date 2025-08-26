# Containerization on H4H

Containerization is especially useful for H4H projects because it allows us to not have to build our enviromnents on H4H. 

## Apptainer

`Apptainer` is a simple easy to use container platform that is can be used on H4H. You can find the documentation [here](https://apptainer.org/docs/user/latest/).

### Installation

To install Apptainer on H4H, it is **important** to use the instructions [here](https://apptainer.org/docs/admin/main/installation.html#install-unprivileged-from-pre-built-binaries).

### Suggested Workflow

1. Create a Dockerfile for your project on your local machine. To learn how to create a Dockerfile, you can refer to the [Dockerfile](https://docs.docker.com/build/concepts/dockerfile/) section of the Docker documentation.
2. Build the container with Docker and push it to Docker Hub on your local machine.
3. Pull the container from Docker Hub using `apptainer pull` on H4H.
4. Run the container using `apptainer run` on H4H.




