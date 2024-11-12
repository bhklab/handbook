# Tabbed Code/Content Blocks

The `tabbed` extension allows you to create tabbed code/content blocks.

!!! note

    This extension is already enabled, you just have to format your markdown
    to use it.

See reference [here](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/).

=== "Tabbed Code Blocks"

    Click on either `C` or `C++` to view the code specific to that language.

    === "C"

        ``` c
        #include <stdio.h>

        int main(void) {
          printf("Hello world!\n");
          return 0;
        }
        ```

    === "C++"

        ``` c++
        #include <iostream>

        int main(void) {
          std::cout << "Hello world!" << std::endl;
          return 0;
        }
        ```

    The markdown for the above code blocks:
    ```
    === "C"

        ``` c
        #include <stdio.h>

        int main(void) {
          printf("Hello world!\n");
          return 0;
        }
        ```

    === "C++"

        ``` c++
        #include <iostream>

        int main(void) {
          std::cout << "Hello world!" << std::endl;
          return 0;
        }
        ```
    ```

=== "Tabbed Content"

    Click on either `Unordered list` or `Ordered list` to view the content
    specific to that list type.

    === "Unordered list"

        * Sed sagittis eleifend rutrum
        * Donec vitae suscipit est
        * Nulla tempor lobortis orci

    === "Ordered list"

        1. Sed sagittis eleifend rutrum
        2. Donec vitae suscipit est
        3. Nulla tempor lobortis orci

    The markdown for the above content blocks:

    ```
    === "Unordered list"

        * Sed sagittis eleifend rutrum
        * Donec vitae suscipit est
        * Nulla tempor lobortis orci

    === "Ordered list"

        1. Sed sagittis eleifend rutrum
        2. Donec vitae suscipit est
        3. Nulla tempor lobortis orci
    ```
