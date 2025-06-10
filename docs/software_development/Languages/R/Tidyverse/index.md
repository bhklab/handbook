# Tidyverse

??? abstract "TL;DR"

    The [Tidyverse](https://tidyverse.tidyverse.org/) is a suite of R packages
    that mesh together with a goal of improving common data science pipeline
    steps, namely data import, tidying, manipulation, visualisation, and
    programming.

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

The origins of the Tidyverse began from a paper written by Hadley Wickham in
2014, titled "Tidy Data", in which he describes the aforementioned
design philosophy. (For those interested, you can read the paper here:
[10.18637/jss.v059.i10](https://doi.org/10.18637/jss.v059.i10).) More recent
documentation of the underlying principles guiding Tidyverse packages can be
found in [the tidy tools manifesto](https://tidyverse.tidyverse.org/articles/manifesto.html)
as well as the [Tidy design principles book](https://design.tidyverse.org/).

For an introduction on the Tidyverse, take a look at their [package page](https://tidyverse.tidyverse.org/).

You can see a list of the eight core packages on their site
[here](https://www.tidyverse.org/packages/), and further details within their
respective documentation pages. For a quick visual overview of a specific
package, you can also find its respective cheatsheet on
[this page](https://posit.co/resources/cheatsheets/).

## Why use the Tidyverse?

The Tidyverse is an _opinionated_ collection of packages, meaning that while the
packages all cohesively follow the same design philosophy, they may not work
well with how you prefer to program or for your specific use case. You may
choose to use only certain packages from the Tidyverse, or you may choose to
only use base R and other alternatives.

Some advantages of using the Tidyverse are:

- **Consistency**: All packages in the Tidyverse follow the same design
    philosophy, making it easier to learn and use multiple packages. They also
    mesh well with one another, making it easier to use multiple packages
    together.
- **Piping**: Most of the Tidyverse is designed to be used together with pipes.
    The `|>` operator from base R >=4.1 works well for this, or you can use the
    `%>%` pipe from the `magrittr` package for more advanced piping options.
- **Readability**: Often Tidyverse code is more human-readable than more complex
    R alternatives, especially when using long pipe chains.

Some disadvantages of using the Tidyverse are:

- **Learning curve**: The Tidyverse has a learning curve, especially if you are
    new to R or programming in general. If switching over from base R, there
    might also be a learning curve to relearn how to do things you are already
    familiar with because of how differently things are designed.
- **Stability**: The Tidyverse is constantly evolving, and packages may be
    updated or deprecated. While base R tries to emphasize stability across
    updates, the Tidyverse packages are actively developed, and updates may
    introduce changes that improve functionality but could impact existing code.
- **Compatibility**: The Tidyverse is not the only way to do things in R, and as
    well, there are countless other packages that may not play nicely with
    Tidyverse-oriented data structures or tibbles. In these cases you may have
    to convert back and forth between tibbles and data frames, which can be
    cumbersome.

## Introductory Example

Say we have a CSV file containing a table, and we want to:

1. Read the file into R;
2. Perform some manipulations on the data; and
3. Write out the new table to a different CSV file.

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
by the R Core team and [R Foundation](https://www.r-project.org/foundation/),
whilst the Tidyverse (as well as a multitude of other R programming tools and
packages) are developed and maintained by [Posit, PBC](https://posit.co/)
(formerly RStudio, Inc) on top of the R language.

If you're familiar with R, you're almost certainly familiar with the RStudio
application, the IDE developed by Posit. Hadley Wickham, the author of the Tidy
Data paper, also happens to be the Chief Scientist at Posit. If you're a fan of
the Tidyverse, also check out Posit's other useful tools like [Positron](https://positron.posit.co/),
[Quarto](https://quarto.org/), [Shiny](https://shiny.posit.co/), and [pak](https://pak.r-lib.org/).

## Additional Resources

### Articles

- [Welcome to the Tidyverse](https://tidyverse.tidyverse.org/articles/paper.html)
    &mdash; A brief paper introducing the Tidyverse, from the package vignette.
- [Tidyverse](https://en.wikipedia.org/wiki/tidyverse) Wikipedia page.
- [Writing performant code with tidy tools](https://www.tidyverse.org/blog/2023/04/performant-packages/)
    &mdash; An interesting read on analysing code performance and how to
    consider alternatives; especially relevant to package development.

### Learning

- [R for Data Science](https://r4ds.hadley.nz/) Textbook &mdash; The go-to
    textbook for learning R and the Tidyverse, authored by Hadley Wickham, Mine
    Çetinkaya-Rundel, and Garrett Grolemund.
- [Swirl](https://swirlstats.com/) &mdash; An interactive learning platform for
    R.
    - Specifically, check out [this course](https://swirlstats.com/scn/getclean.html)
        for a quick (and interactive!) taste of working with `dplyr` and `tidyr`.
- [Tidyverse style guide](https://style.tidyverse.org/) &mdash; A guide to consistent code writing in R.

### Packages

- [Tidymodels](https://www.tidymodels.org) &mdash; A collection of packages
    for modeling and machine learning in R.
- [Pharmaverse](https://pharmaverse.org/) &mdash; A connected network of
    companies and individuals working to promote collaborative development of
    curated open source R packages for clinical reporting usage in pharma.
