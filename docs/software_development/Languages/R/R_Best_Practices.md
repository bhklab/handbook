# R Coding Best Practices

## Quick Start

!!! note

    There are two primary style guides for R code: the [Bioconductor Style Guide](https://contributions.bioconductor.org/r-code.html) and the [Tidyverse Style Guide](https://style.tidyverse.org/). There are differences between them, such as Tidyverse style preferring two spaces for indentation while Bioconductor prefers four spaces, or snake_case naming for functions in Tidyverse while Bioconductor prefers camelCase.

    Because the BHKLab develops packages for Bioconductor, as a general rule **we prefer to follow the Bioconductor Style Guide**.

### Naming

- All class names should use **PascalCase**.
- All function names should use **camelCase**.
- Variable names can be **lower_snake_case** or **camelCase**, but be consistent within your project.
- Private (non-exported) functions should be prepended with a dot (e.g., `.myPrivateFunction`).
- Never use dots in your function, class, or variable names (e.g., never `my.class`, `my.function`, or `my.variable`).
  - Dots have a special meaning in R and are used to define S3 methods.
  - For generic function `f` and object `x` of S3 class `A`, `f(x)` calls the method `f.A(x)`.
- Dots are discouraged but acceptable in list, column, or function parameter names.

### Formatting

- Lines of code should ideally be less than **80 characters** and never more than **120 characters**.
  - This makes it easy to read your code with multiple windows open and ensures no horizontal scrolling is necessary.
- Functions should ideally be less than **50 lines of code** and never more than **80 lines of code**.
  - If your functions are longer than this, your function is doing too many things; consider refactoring into helper methods.
- Indentation should use **four spaces**.
- It is preferable to add an extra indentation for wrapped lines if it reduces the overall indentation of the code.

### Style

- Assignment should always use `<-` and never use `=`.
- Assignment with `->` is discouraged, but acceptable when using pipes.
- When using pipes, the base R pipe `|>` is preferred over the magrittr pipe `%>%`.
- Operators should always be surrounded by spaces.
  - **Good:** `x[x > 1]` or `c("a", "b") %in% c("a", "b", "c")` or `if (x > 5 || x < 0 )` or `x <- 1`
  - **Bad:** `x[x>1]` or `c("a", "b")%in%c("a", "b", "c")` or `if (x>5||x<0)` or `x<-1`
- No spaces after function names, except in `for`, `if`, or `else` statements.
  - **Bad:** `mean (x)`
  - **Good:** `mean(x)` or `if (x){ ... }` or `for (x in 1:5) { ... }`
- Curly braces should start on the same line as a function.

```r
# Good
my_fun <- function(x) {
  ...
}
# Bad
my_fun <- function(x)
{
  ...
}
```

### Linting

- Linting is a form of static code analysis that automatically checks if code in a directory or project follows best practices for coding style and format.
- The [`lintr`](https://lintr.r-lib.org/) package provides linting for the R language and integrates into the R console and many IDEs.
  - This linter is included with the R VSCode extension and can be added to RStudio.
- By default, the linter enforces the **Tidyverse Style Guide**, which differs slightly from Bioconductor (and BHKLab) conventions.
- The [`styler`](https://github.com/r-lib/styler/releases/tag/v1.0.0) package can be used to automatically format R files to follow your `lintr` settings, but be careful as it can mangle your code. Integration is easiest with RStudio.

## References

- [Bioconductor Style Guide](https://contributions.bioconductor.org/r-code.html)
- [Tidyverse Style Guide](https://style.tidyverse.org/)
