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

### 1. Create a branch for your changes

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

To **create a new branch and switch to it**, run the following command:

```console
git checkout -b <branch-name>
$ git checkout -b jjjermiah/adding-getting-started-page
```

If you already have a named branch, you can switch to it with the following command:

```console
git switch <branch-name>
$ git switch jjjermiah/adding-getting-started-page
```

### 2. Add your new content to the `docs` directory

??? question "How do I know where to create my file?"

    The command below will create an empty Markdown file called `my_new_page.md` in the `docs/onboarding` directory.
    The relative path to the `docs` directory, will be the link to your new page. <br>
    i.e the link to your new page will be `<website-url>/handbook/onboarding/my_new_page/`

Let's say you want to add a new page to the `Onboarding` section.
You would add a new file to the `docs/onboarding` directory.

```console
$ touch docs/onboarding/my_new_page.md
You should now see a new file at `docs/onboarding/my_new_page.md`.
```

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
