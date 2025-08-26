# zoxide

[zoxide](https://github.com/ajeetdsouza/zoxide) is a fast, smarter alternative to `cd`. It keeps track of your most-used directories and lets you jump to them instantly with short commands and fuzzy matching. zoxide works across shells (Bash, Zsh, Fish, PowerShell) and is designed to speed up navigation in the terminal.

Find the installation instructions [here](https://github.com/ajeetdsouza/zoxide#installation).

## Usage

```bash
z foo              # cd into highest ranked directory matching foo
z foo bar          # cd into highest ranked directory matching foo and bar
z foo /            # cd into a subdirectory starting with foo

z ~/foo            # z also works like a regular cd command
z foo/             # cd into relative path
z ..               # cd one level up
z -                # cd into previous directory

zi foo             # cd with interactive selection (using fzf)

z foo<SPACE><TAB>  # show interactive completions (zoxide v0.8.0+, bash 4.4+/fish/zsh only)
```