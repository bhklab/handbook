# Prerequisites

# [Setup](#setup)

Pixi is a tool for managing conda environments and dependencies. 
To install Pixi, visit the [Pixi website](https://pixi.sh/latest/) and follow the 
instructions specific to your operating system.
The [Pixi documentation](https://pixi.sh/latest/) is an extensive resource for
learning how to use Pixi.

NOTE: `Pixi` is a new tool and is still in development. 
If you encounter any `pixi` related issues when working with the handbook,
please [open an issue](https://github.com/bhklab/handbook/issues/new) on the
handbook repository.

## Cloning the Repository

To begin, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/bhklab/handbook.git
```

## Installing Dependencies
Once you have cloned the repository, navigate to the project directory and 
install the dependencies:

```bash
pixi install
```

This will install the dependencies specified in the `pixi.toml` file.