# Lab Handbook

<!--intro-start-->
## Draft Structure:
<iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVKwSe31w=/?moveToViewport=-3635,688,2780,1134&embedId=279072143427" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>


Edit this diagram using drawio or vscode drawio extension:  `docs/diagrams/handbook_overview.drawio.png`

Insipiration:

  - [Koesterlab Handbook](https://koesterlab.github.io/data-science-for-bioinfo/)
  - [Candice Morey Lab Handbook](https://ccmorey.github.io/labHandbook/)
  - [Baby Lab Handbook](https://mcmaster-baby-lab.github.io/handbook/)
  - [Lowe Power Lab Handbook](https://github.com/lowepowerlab/lab_handbook)
  - [Vortex Lab Handbook](https://github.com/uw-vortex/VORTEX-handbook)

## Table of Contents
- [Lab Handbook](#lab-handbook)
  - [Draft Structure:](#draft-structure)
  - [Table of Contents](#table-of-contents)
  - [Development Documentation](#development-documentation)
  - [Development (for now)](#development-for-now)
    - [Installing Pixi](#installing-pixi)
    - [Cloning the repository](#cloning-the-repository)
    - [Installing dependencies](#installing-dependencies)
    - [Building the documentation](#building-the-documentation)
    - [Previewing the documentation](#previewing-the-documentation)
    - [Adding Content to the Documentation](#adding-content-to-the-documentation)

## Development Documentation

See [Contributing to the Lab Handbook][contributing-to-the-lab-handbook] for more information.


## Development (for now)

TODO::Add this stuff to the proper section under `Contributing`

### Installing Pixi

Pixi is a tool for managing conda environments and managing dependencies.

To install pixi, visit the [pixi website](https://pixi.sh/) and follow the instructions for your operating system.

### Cloning the repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/bhklab/handbook.git
```

### Installing dependencies

To install the dependencies for the handbook, run the following command:

```bash
pixi install
```

This will install the dependencies specified in the `pixi.toml` file.

### Building the documentation

To build the documentation, run the following command:

```bash
pixi run build
```

This will build the documentation and output it to the `site` directory.

### Previewing the documentation

To preview the documentation, run the following command:

```bash
pixi run serve
```

This will start a local server and preview the documentation at `http://localhost:8000`.

### Adding Content to the Documentation

The documentation is written in Markdown and can be found in the `docs` directory.

Here are the steps to add new content to the documentation:

1. Create a branch for your changes.
  ```bash
  git checkout -b <branch-name>
  # i.e git checkout -b adding-getting-started-page
  ```

2. Add your new content to the `docs` directory.
  ```bash
  touch docs/onboarding/getting_started.md
  ```

3. Add your new content to the `mkdocs.yml` file.
  ```yaml
  nav:
    - Home:
        - Welcome: index.md
    - Onboarding:
        - Introduction: onboarding/introduction.md
        - Getting Started: onboarding/getting_started.md
  ```

4. Preview your changes.
   ```bash
   pixi run serve
   ```

5. Commit and push your changes to your branch.
  ```bash
  git add .
  git commit -m "Add new getting started page"
  git push origin adding-getting-started-page
  ```

6. Create a pull request to merge your changes into the main branch.

  - Request a review from a maintainer.
