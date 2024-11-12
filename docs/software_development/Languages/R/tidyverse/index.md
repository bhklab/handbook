# Tidyverse


## What is the Tidyverse?

From their [website](https://www.tidyverse.org/):

> "The tidyverse is an opinionated collection of R packages designed for data science. All packages share an underlying design philosophy, grammar, and data structures."

The concept of the tidyverse originated from a paper by Hadley Wickham in 2014, titled "Tidy Data". For those interested, you can read the paper here: [10.18637/jss.v059.i10](https://doi.org/10.18637/jss.v059.i10).

Some of the core packages in the tidyverse include:

- `ggplot2`: for data visualization
- `dplyr`: for data manipulation
- `tidyr`: for data tidying
- `readr`: for data import
- `purrr`: for functional programming
- `tibble`: for tibbles, a modern reimagining of data frames
- `stringr`: for strings
- `forcats`: for factors

You can see this list of packages with more in-depth descriptions [here](https://www.tidyverse.org/packages/), and also within their respective documentation pages.

## Why use the Tidyverse?

As mentioned in the definition, the tidyverse is an *opinionated* collection of packages. This means that while the packages all cohesively follow the same design philosophy, they may not work well with how you prefer to program or for your specific use case. You may choose to use all of or only certain packages from the tidyverse, or you may choose to only use other alternatives.

The main advantages of using the tidyverse are:

- **Consistency**: All packages in the tidyverse follow the same design philosophy, making it easier to learn and use multiple packages. They also mesh well with one another, making it easier to use multiple packages together.
- **Piping**: Most of the tidyverse is designed to be used together with pipes. The `|>` operator from base R works well for this, or you can use the `magrittr` package and `%>%` pipe for more advanced piping.

Some disadvantages of using the tidyverse are:

- **Learning curve**: The tidyverse has a steep learning curve, especially if you are new to R or programming in general. If switching over from baseR, there might also a learning curve to relearn how to do things you are already familiar with.
- **Stability**: The tidyverse is constantly evolving, and packages may be updated or deprecated. This can lead to breaking changes in your code if you are not careful.
- **Compatibility**: The tidyverse is not the only way to do things in R, and as well, there are countless other packages that may not play nicely with tidyverse-oriented data structures such as tibbles. In these cases you may have to convert back and forth between tibbles and data frames, which can be cumbersome.