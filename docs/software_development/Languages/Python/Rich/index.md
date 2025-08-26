# Rich

## Rich

??? abstract "TL;DR"

    [Rich](https://github.com/Textualize/rich) is a python package for making command-line tools look better. Rich contains a drop in replacement of python's default `print` method which adds additional funcitonality such as pretty-printing lists and dictionaries; colouring and styling text; custom progress bars; and much more.

    *Installation*
    ```
    pip install rich
    ```
    Alternatively if using Pixi:
    ```
    pixi add rich --pypi
    ```

    *Usage*
    ```python
    >>> from rich.print import print

    >>> print("[blue]Hello World!") # This will make the output blue
    ```


    

## Introduction

!!! quote "From the [Rich Documentation](https://rich.readthedocs.io/en/stable/introduction.html):"

    "Rich is a Python library for writing rich text (with color and style) to the terminal, and for displaying advanced content such as tables, markdown, and syntax highlighted code."

Rich is a python package for printing formatted text to the terminal. It offers a powerful drop-in replacement for python's default `print` function. 

## Why Use Rich?

- **Compatible**: Rich has a drop-in replacement for python's `print` function, so it can be added to any existing python project with just one import statement. Rich will automatically offer syntax highlighting and pretty-printing of lists and dictionaries without any additional user intervention.
- **Powerful**: Rich offers text styling, tables, tree printing, live displays, and much more. It's a bare-neccesity for any terminal-based python application. 
- **Intuitive**: Rich is very easy to use, and their documentation contains examples for every feature they offer. If you're trying to do something with Rich, chances are the documentation already contains a working example you can copy/paste into your project.

## Basic Usage

To use rich, import the replacement `print` method:

```python
from rich.print import print
print("This is using the rich print method.")
```

Alternatively, you can create a custom rich console by importing thr `Console` class:

```python
from rich.console import Console

console = Console()
console.print("This also uses the rich print method.")
```

### Styling text

Rich offers in-line styling by enclosing your styling tags in square brackets:

```python
from rich.print import print
print("[bold red]This text is bold and red[/bold red] but the rest of this line is normal.")

print("[blue]Since there's no closing tag, this entire line will be blue.")
```

You may also pass styling tags into the `style` parameter of the print function:
```python
from rich.print import print
print("This text is bold and red", style="bold red")
```

### Tables

Rich offers an easy solution for printing tables of data to the console. Just import the `Tables` module to get started:

```
from rich.print import print
from rich.table import Table
```

Here's an example of a table from the [Rich documentation](https://rich.readthedocs.io/en/stable/tables.html):

```python
from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)
```

## Additional Resources

**Styling Guide**:
[Rich Documentation On Styles](https://rich.readthedocs.io/en/stable/style.html)
Provides information of the available styling options and how to use them.
**Standard Colours**:
[Rich Documentation On Standard Colours](https://rich.readthedocs.io/en/stable/appendix/colors.html#appendix-colors)
Provides a list of named colors for use in styling terminal output.
**Tables**:
[Rich Documentation On Tables](https://rich.readthedocs.io/en/stable/tables.html)
In-depth guide on creating tables with examples.

## Advanced Resources

**Live Displays**:
[Rich Live Displays Page](https://rich.readthedocs.io/en/stable/live.html)
Live displays offer a great way to create persistent and animatied displays in the terminal.

**Progess Display**:
[Rich Progress Display Page](https://rich.readthedocs.io/en/stable/progress.html)
Rich includes support for custom progress bars and is useful in cases where tqdm doesn't function properly, such as when multiple nested tasks all require progress bars.




