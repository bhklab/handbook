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

From their [website](https://www.tidyverse.org/):

> "The tidyverse is an opinionated collection of R packages designed for data
> science. All packages share an underlying design philosophy, grammar, and data
> structures."

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

## Tidyverse vs. BaseR

## See also

-   [R for Data Science](https://r4ds.hadley.nz/) Textbook - The go-to textbook
    for learning R and the Tidyverse, authored by Hadley Wickham, Mine
    Çetinkaya-Rundel, and Garrett Grolemund.
-   [Tidymodels](https://www.tidymodels.org) - A collection of packages for
    modeling and machine learning in R.
-   [Swirl](https://swirlstats.com/) - An interactive learning platform for R.
    -   Specifically, check out
        [this course](https://swirlstats.com/scn/getclean.html) for a quick
        taste of working with `dplyr` and `tidyr`.
-   [Writing perfomant code with tidy tools](https://www.tidyverse.org/blog/2023/04/performant-packages/) -
    An interesting read on analysing code performance and how to consider
    alternatives; especially relevant to package development.
