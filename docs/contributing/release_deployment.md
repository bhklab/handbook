# Release and Deployment

## Introduction

The handbook website is hosted on [GitHub Pages](https://pages.github.com/).
This document provides a detailed overview of how the deployment and release
processes work, ensuring a smooth and automated workflow.

## GitHub Pages

GitHub Pages is a service that allows you to host static websites directly
from your GitHub repository.

### How It Works

Whenever changes are pushed to the `main` branch, a
[GitHub Action](https://github.com/features/actions) is triggered to
automatically build and deploy the website.

You can view the build and deployment action at
[this link](https://github.com/bhklab/handbook/actions/workflows/main.yaml).

The automated workflow includes the following steps:

1. **Check Out the Repository**: The GitHub Action checks out the latest code
   from the `main` branch.
2. **Install Dependencies**: Dependencies specified in the `pixi.toml` file
   are installed.
3. **Build the Documentation**: The action builds the site using MkDocs and
   the configurations defined in your project.
4. **Deploy to GitHub Pages**: The compiled site is deployed to the `gh-pages`
   branch.

Once the `gh-pages` branch is updated, GitHub Pages will automatically publish
the latest version of the website.

## Releases

Even though this project primarily uses MkDocs, we leverage
[release-please](https://github.com/googleapis/release-please) to automate the
release process, making it easier to maintain version control and changelogs.

### How It Works

When a pull request is merged into the `main` branch, a
[GitHub Action](https://github.com/features/actions) triggers the release
process.

You can view the release automation action at
[this link](https://github.com/bhklab/handbook/actions/workflows/release-please.yaml).

Key benefits of using `release-please` include:

- **Automated Release Creation**: The tool automatically generates a release
  with changelogs and updates the version number based on the changes merged
  into `main`.
- **Dynamic Pull Request Updates**: If additional changes are pushed to the
  `main` branch after a pull request is created, the release PR will update to
  include those changes, ensuring that the release captures all intended
  updates.
- **Controlled Release Process**: Maintainers can merge changes into the
  release PR only when they are ready to publish a new version, giving them
  full control over the timing of each release.

This automated approach ensures consistency and reduces the manual effort
required to manage releases.