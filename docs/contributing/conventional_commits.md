# [Conventional Commits](#conventional-commits)

We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification for commit messages. This helps us automate our release process and keep our commit history clean. 

This style is mandatory for [merging pull requests][modify-the-commit-message-as-needed] on the handbook, but are recommended for all commits.

The main points are summarized below, but you can read the full spec [here](https://www.conventionalcommits.org/en/v1.0.0/).

## Commit Message Format

Each commit message consists of a **header**, a **body** and a **footer**. The header has a special format that includes a `<type>`, a `<scope>` and a `<summary>`:

```
<type>[optional scope]: <short summary in present tense>

[optional body: explains motivation for the change]

[optional footer(s): note BREAKING CHANGES here, and issues to be closed]
```

The `<scope>` of the header is optional and provides context for where the change was made. It can be anything relevant to your package or development workflow (e.g., it could be the module or function - name affected by the change).

`<type>` refers to the kind of change made and is usually one of:

- `feat`: A new feature.
- `fix`: A bug fix.
- `docs`: Documentation changes.
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc).
- `refactor`: A code change that neither fixes a bug nor adds a feature.
- `perf`: A code change that improves performance.
- `test`: Changes to the test framework.
- `build`: Changes to the build process or tools.
- `ci`: Changes to CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs).
- `chore`: Other changes that don't modify src or test files.

Other types may be defined per project, but these are the most common.


## Sources

1. [Angular Commit Format Reference Sheet - Brian Clements](https://gist.github.com/brianclements/841ea7bffdb01346392c)
2. [Origin of Angular Commit Style - AngularJS Git Commit Guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits)
3. [Py-Pkgs tutorial - Automatic version bumping using Angular Commit Style](https://py-pkgs.org/en/latest/development/commit-guidelines.html)