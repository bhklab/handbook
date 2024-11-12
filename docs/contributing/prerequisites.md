# [Prerequisites](#prerequisites)

## [Installing Pixi](#installing-pixi)

Pixi is a tool for managing conda environments and dependencies.
To install Pixi, visit the [Pixi website](https://pixi.sh/latest/) and follow the
instructions specific to your operating system.
The [Pixi documentation](https://pixi.sh/latest/) is an extensive resource for
learning how to use Pixi.

Running the following command in your terminal should verify installation.

```console
$pixi --version
pixi 0.34.0
```

## [Cloning the Repository](#cloning-the-repository)

To begin, clone the repository to your local machine using the following command:

```console
$ git clone https://github.com/bhklab/handbook.git
Cloning into 'handbook'...
....
....
....
...
$ cd handbook
```

## Installing Dependencies

Once you have cloned the repository, navigate to the project directory and
install the dependencies:

```console
$ pixi install
✔ The default environment has been installed.
```

This will install the dependencies specified in the `pixi.toml` file.

To add content to the handbook, see the [Adding Content][adding-content] section.
