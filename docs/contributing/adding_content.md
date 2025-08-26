# [Adding Content](#adding-content)

## Introduction

> This document will guide you through the process of adding a new page to the
> handbook.

!!! tip

    The handbook is built using [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
    These tools also have extensive documentation and guides for contributing to a Mkdocs project.

    Please refer to their respective documentation **first** for any questions you might have.

## Adding Content to the Documentation

The documentation is written in Markdown and can be found in the `docs` directory.

Here are the steps to add new content to the documentation:

### 1. Select or create an issue
Navigate to the [Issues](https://github.com/bhklab/handbook/issues) section of the repo and select an existing issue or continue on from the Issue you created in the [Submitting Issues](submitting_issues.md) section. 

Assign yourself to the issue if it's not already assigned.

### 2. Create a branch for your changes

Open the issue and click on the "Create a branch" link under Development on the right side of the page.

Name your branch following the format: `<author-ID>/<purpose-of-branch>`

??? note "Note: Naming your branch"
    A branch is a way to work on a new feature or bug fix without affecting the main branch.
    The standard for this project is to use the following format:

    ```console
    $ <author-ID>/<purpose-of-branch>
    OR
    $ <author-ID>/<issue-reference>
    ```
    Where `<author-ID>` can be a GitHub username or an alias.

    `<purpose-of-branch>` is a short description of the changes you are making.
    `<issue-reference>` is the number of the issue you are working on.

    For example:

    ```console
    $ jjjermiah/adding-getting-started-page
    OR
    $ jjjermiah/13-docs-finish-tutorial-for-page-review
    ```

In your the terminal in the handbook directory, run the lines of code provided (git fetch, git checkout branchname).

You will now be on the branch associated with the issue and can beging making your changes.


### 2. Add your new content to the `docs` directory

??? question "How do I know where to create my file?"

    The command below will create an empty Markdown file called `my_new_page.md` in the `docs/onboarding_offboarding` directory.
    The relative path to the `docs` directory, will be the link to your new page. <br>
    i.e the link to your new page will be `<website-url>/handbook/onboarding_offboarding/my_new_page/`

Let's say you want to add a new page to the `Onboarding/Offboarding` section.
You would add a new file to the `docs/onboarding_offboarding` directory.

```console
$ touch docs/onboarding_offboarding/my_new_page.md
You should now see a new file at `docs/onboarding_offboarding/my_new_page.md`.
```

!!! note "You may need to add your page to the `.pages` file"

    If you are adding a new page to the handbook, you may need to add the new page to the `.pages` file
    that lives in the same directory in which your new page is located.
    This file is used to generate the navigation menu for the handbook.

    To add your new page to the `.pages` file, open the file and add the relative path to your new page.
    For example, if you added a new page to the `onboarding_offboarding` directory, you would add the following
    line (highlighted in green)
    to the `onboarding_offboarding/.pages` file:

    ```diff
    title: Onboarding / Offboarding

    nav:
        - Onboarding
        - Offboarding
    +   - onboarding_offboarding/my_new_page.md
    ```

    This will add a link to your new page in the navigation menu.

To learn more about how to actually write content, see the [Handbook MkDocs Page][mkdocs] and
[Handbook Markdown page][markdown].

### 3. Preview your changes

The following is a [`pixi task`](https://pixi.sh/latest/features/advanced_tasks/)
that will start a local server and preview the documentation at `http://localhost:8001` (aka `http://127.0.0.1:8001`).

```console
$ pixi run serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
...
INFO    -  [08:55:05] Serving on http://127.0.0.1:8001/handbook/
```

You should see your changes appear at `http://127.0.0.1:8001/handbook/onboarding/my_new_page/`

!!! tip
    You can set the handbook website to automatically open in your default
    browser by using the `-o` flag:

    ```sh
    pixi run serve -o
    ```

!!! note "About the port number"
    By default, we host the local site on port `8001` because it is more likely
    to be unused and available for the local server to use. In the case that you
    would like to manually specify a different port (e.g. if it's in use by
    something else), you can use the `-a` flag after `pixi run serve`.

    For example, to run on port `1234`:
    ```sh
    pixi run serve -a localhost:1234
    ```

### 4. Commit and push your changes to your branch

```sh
git add .
git commit -m "Add new getting started page"
git push --set-upstream origin jjjermiah/adding-getting-started-page
```

### 5. Create a PR

Create a pull request (PR) to merge your changes into the main branch.
Request a review from a maintainer.

See [the section on Reviewing a Contribution][reviewing-a-contribution] for more information.
