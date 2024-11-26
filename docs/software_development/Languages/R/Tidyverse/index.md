# Tidyverse

??? abstract "TL;DR"

    The Tidyverse is a suite of R packages that mesh together with a
    goal of improving common data science pipeline steps, namely data import,
    tidying, manipulation, visualisation, and programming.

    Of the eight core packages, some notable ones include:

    * `readr`, for data import and export
    * `dplyr`, for data manipulation
    * `ggplot2`, for data visualization

    The packages also emphasize the use of the pipe, `|>` or `%>%`. When you
    pipe an object forward, it is treated as the first parameter in the
    next function. For example, the two lines below are equivalent to one
    another:

    ```
    colnames(read.csv(filename, header = TRUE))
    ```
    ```
    filename |> read.csv(header = TRUE) |> colnames()
    ```

## What is the Tidyverse?

!!! quote "From the [Tidyverse website](https://www.tidyverse.org/):"

    "The Tidyverse is an opinionated collection of R packages designed for data
    science. All packages share an underlying design philosophy, grammar, and data
    structures."

The concept of the tidyverse originated from a paper by Hadley Wickham in 2014,
titled "Tidy Data", in which he describes the aforementioned design philosophy.
(For those interested, you can read the paper here:
[10.18637/jss.v059.i10](https://doi.org/10.18637/jss.v059.i10).)

The tidyverse package itself can be thought of as a collection of several "core"
packages. When you load the package with `library(tidyverse)`, you are just
loading all of these core packages (eight of them, as of writing this) along
with their dependencies together in a single line. Alternatively, you can load
individual packages within the tidyverse, such as `library(ggplot2)`.

You can see a list of the core packages on their site
[here](https://www.tidyverse.org/packages/), and further details within their
respective documentation pages.

## Why use the Tidyverse?

As mentioned in the definition, the tidyverse is an _opinionated_ collection of
packages. This means that while the packages all cohesively follow the same
design philosophy, they may not work well with how you prefer to program or for
your specific use case. You may choose to use only certain packages from the
tidyverse, or you may choose to only use baseR and other alternatives.

The main advantages of using the tidyverse are:

-   **Consistency**: All packages in the tidyverse follow the same design
    philosophy, making it easier to learn and use multiple packages. They also
    mesh well with one another, making it easier to use multiple packages
    together.
-   **Piping**: Most of the tidyverse is designed to be used together with
    pipes. The `|>` operator from base R works well for this, or you can use the
    `magrittr` package and `%>%` pipe for more advanced piping options.
-   **Readability**: Often tidyverse code is more human-readable than more
    complex R alternatives, especially when using long pipe chains.

Some disadvantages of using the tidyverse are:

-   **Learning curve**: The tidyverse has a steep learning curve, especially if
    you are new to R or programming in general. If switching over from baseR,
    there might also a learning curve to relearn how to do things you are
    already familiar with.
-   **Stability**: The tidyverse is constantly evolving, and packages may be
    updated or deprecated. While baseR tries to emphasize stability across
    updates, the tidyverse prefers to optimize functionality. This may lead to
    breaking changes in your code across updates.
-   **Compatibility**: The tidyverse is not the only way to do things in R, and
    as well, there are countless other packages that may not play nicely with
    tidyverse-oriented data structures or tibbles. In these cases you may have
    to convert back and forth between tibbles and data frames, which can be
    cumbersome.

## Introductory Example

Let's say we have a CSV file containing a table, and we want to read into R,
perform some manipulations on the data, and then write it out to a new file.

First, let's define some common paths for input and output:

```r
infile <- "rawdata/my_df.csv"
outfile <- "procdata/my_df.csv"
```

Using these paths, let's compare the code for what this whole process might look
like.

=== "Base R"

    ```r
    # Read the CSV file
    my_df <- read.csv(infile)

    # Filter to only rows where value > 10
    my_df_filtered <- my_df[my_df$value > 10, ]

    # Select only specific columns
    my_df_selected <- my_df_filtered[, c("id", "value")]

    # Write the output out to a new CSV file
    write.csv(my_df_selected, outfile, row.names = FALSE)
    ```

    * Note: You could also overwrite the `my_df` variable each time you filter
    rows and select columns instead of creating new intermediary data frames,
    especially if you have no need to keep the original or intermediary data.

=== "Tidyverse"

    ```r
    my_df <- infile |>      # Start with the path, piping forward into the "pipeline"
      read_csv() |>         # From `readr`, reads a csv at the path into a tibble
      filter(value > 10) |> # From `dplyr`, filters to only rows that match condition
      select(id, value) |>  # From `dplyr`, selects only specified columns by name
      write_csv(outfile)    # From `readr`, writes the tibble to a csv file path
    ```

    * Note: While technically not required, setting `my_df` to the pipeline will
    save the final pipeline result to that variable name. The function
    `write_csv()` invisibly returns the same tibble piped into it, thus it is
    saved as `my_df`.

Arguably, the human-readability of the code became a bit better, even if you're
not necessarily familiar with the Tidyverse. Note that the `read.csv()` function
is different from the `read_csv()` function, as well as `write.csv()` and
`write_csv()`. Often base R uses dot notation for their variables and functions,
e.g. `as.data.frame()`, whilst Tidyverse convention is to use snakecase, e.g.
`as_tibble()`.

## Tidyverse vs. Base R

It's important to differentiate the R Tidyverse packages and design from the
base R language itself. The R programming language is developed and maintained
by the [R Foundation](https://www.r-project.org/foundation/), whilst the
Tidyverse (as well as a multitude of other R programming tools and packages) are
developed and maintained by [Posit, PBC](https://posit.co/) (formerly RStudio,
Inc) on top of the R language. Some might consider the Tidyverse to be like a
completely separate language because of its unique syntax, development style,
and separation from traditional base R and programming design in general.

If you're familiar with R, you're almost certainly familiar with the RStudio
application, the IDE developed by Posit. Hadley Wickham, the author of the Tidy
Data paper, also happens to be the Chief Scientist at Posit. It's likely that
if any package is supported/funded by Posit, it is a Tidyverse-adjacent package.
It is also likely that they adopted a modern hexagonal sticker for their logo.
Some examples are:

-   [`pak`](https://pak.r-lib.org/), a fresh approach to R package installation.
-   [`fs`](https://fs.r-lib.org/), a cross-platform interface for file system
    operations in R.
-   [`renv`](https://rstudio.github.io/renv/index.html), a package for easy
    reproducible environments in R.
-   [`styler`](https://styler.r-lib.org/), a code formatter for R, often used
    alongside `lintr` to keep your code clean.

R programmers may choose between Tidyverse packages, base R functions, or other
packages like `data.table`. There's not always a _right_ way of doing
things and you can spend some time to figure out which ways work best for you.

## Additional Resources

-   [Welcome to the Tidyverse](https://tidyverse.tidyverse.org/articles/paper.html)
    &mdash; A brief paper introducing the Tidyverse, from the package vignette.
-   [Tidyverse](https://en.wikipedia.org/wiki/tidyverse) Wikipedia page.
-   [R for Data Science](https://r4ds.hadley.nz/) Textbook &mdash; The go-to
    textbook for learning R and the Tidyverse, authored by Hadley Wickham, Mine
    Çetinkaya-Rundel, and Garrett Grolemund.
-   [Swirl](https://swirlstats.com/) &mdash; An interactive learning platform
    for R.
    -   Specifically, check out [this course](https://swirlstats.com/scn/getclean.html)
        for a quick (and interactive!) taste of working with `dplyr` and
        `tidyr`.
-   [Tidymodels](https://www.tidymodels.org) &mdash; A collection of packages
    for modeling and machine learning in R.
-   [Pharmaverse](https://pharmaverse.org/) &mdash; A connected network of
    companies and individuals working to promote collaborative development of
    curated open source R packages for clinical reporting usage in pharma.
-   [Writing performant code with tidy tools](https://www.tidyverse.org/blog/2023/04/performant-packages/)
    &mdash; An interesting read on analysing code performance and how to
    consider alternatives; especially relevant to package development.
