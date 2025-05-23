# Pixi Package Manager

??? abstract "TL;DR"

    [Pixi](https://pixi.sh/latest/) is a modern, performant package manager designed as an alternative to Conda, Mamba, and even PyPI. It simplifies dependency management across operating systems, making project reproducibility easier across systems.

## What is Pixi?

Pixi is a package manager built to improve upon and provide an alternative to Conda and Mamba (or environments in general). Specifically, Pixi aids projects that require managing complex dependencies and ensuring reproducibility across different operating systems.

Pixi excels in ease of use, speed, and robustness, positioning itself as a compelling replacement for Conda when managing project-level dependencies, especially in multi-language (e.g., Python and R) data science projects.

!!! note "Python-only projects"

    For projects focused exclusively on Python, you might also consider using [`uv`](https://github.com/astral-sh/uv) instead, a modern alternative to `pip` and/or `pyenv`.

For extra context on why the developers built Pixi in the first place, see their [Vision](https://pixi.sh/latest/misc/vision/) page.

## Why Consider Pixi?

### Reproducibility and Cross-platform Compatibility

Pixi excels in dependency management and reproducibility, particularly across different operating systems. With Pixi, sharing your environment setup and ensuring your project runs identically on other machines is straightforward:

- Simply include a `pixi.toml` file in your project repository.
- Another user runs `pixi install` and instantly replicates your environment.

## Tasks

Instead of describing ways to run pipelines or commands to do repeated actions, you can define tasks in the `pixi.toml` file. This way, instead of running long commands with convoluted arguments and flags, you can alias it with a simple name. You can find more details on tasks on their [task documentation](https://pixi.sh/latest/workspace/advanced_tasks/).

### Enhanced Performance and Usability

Pixi enhances the performance and usability experience compared to traditional tools like Conda or Anaconda, providing:

- Faster dependency resolution
- Simplified, intuitive command-line interface (CLI)
- Robust management of dependencies for multiple languages within a single environment

## Getting Started

Installation instructions can be found directly on the [Pixi installation guide](https://pixi.sh/latest/advanced/installation/).

Once installed, a great starting point and introduction can be found on their dedicated [Getting Started page](https://pixi.sh/latest/getting_started/).

Here's a cheatsheet on how you might use Pixi for basic project management:

| Command          | Description                                     |
| ---------------- | ----------------------------------------------- |
| `pixi init`      | Start a pixi project in the current working dir |
| `pixi install`   | Install all dependencies from `pixi.toml`       |
| `pixi add <pkg>` | Add a new dependency and update environment     |
| `pixi run <cmd>` | Run a command (or task) within Pixi environment |
| `pixi shell`     | Activate a shell with Pixi-managed environment  |

## Example Usage

### Working in Python with Pixi

Instead of pip installing Python packages globally, or using a Conda environment, you can define per-project dependencies like so:

```bash
pixi add python@3.10 # specify an exact package version!
pixi add pandas

# or add multiple at once:
pixi add python@3.10 pandas
```

### Working in R with Pixi

Because Pixi utilizes the Conda package ecosystem, packages you can install with Conda are also available in Pixi. This includes R packages, which can be installed easily:

```bash
pixi add r-base
pixi add r-ggplot2
pixi add bioconductor-limma -c bioconda
```

!!! tip "Installing R and Bioconductor Packages"

    R packages are often prepended with `r-` in the package name, and depend on the base R installation `r-base`. Bioconductor packages are also available if you add `bioconda` as a channel, and are often prepended with `bioconductor-`.

## VS Code Integration

You can install the VS Code extension to help manage Pixi environments within the IDE. You can find it on the VS Code Marketplace:

- [Pixi VS Code Extension](https://marketplace.visualstudio.com/items?itemName=jjjermiah.pixi-vscode)

## Additional Resources

- [Pixi Documentation](https://pixi.sh/latest/)
- [GitHub Repository](https://github.com/prefix-dev/pixi)
