# Quick Git Tips

## 1. Switch Branches Without Losing Changes

**Problem:** Switching branches with uncommitted changes.  
**Solution:** Stash the changes and reapply them later:

```sh
git stash
git stash apply
```

For more information on stashing, see [git's documentation on stashing](https://git-scm.com/docs/git-stash).

## 2. View Commit History Across Branches

**Problem:** Viewing a detailed log of commits and branches.  
**Solution:** Git's `log` command comes with many options to visualize commit history in a pretty way:

```sh
git log --oneline --graph --decorate --all
```

In the handbook, we have a dedicated branch that handles the deployment of the website called `gh-pages`.
To avoid seeing this branch in your git log, you can use the following command:

```sh
git log --exclude="*/gh-pages" --graph --oneline --all
```

For more information on the `log` command, see [git's documentation on log](https://git-scm.com/docs/git-log).

## 3. Edit the Last Commit

**Problem:** You committed changes but realize you forgot something.  
**Solution:** Amend the last commit with:

```sh
git commit --amend
```

[This doc by Atlassian](https://www.atlassian.com/git/tutorials/rewriting-history) does a great job explaining different ways to rewrite history in git.

For more information on git commits and their options, see [git's documentation commits](https://git-scm.com/docs/git-commit).

## 4. Check for Merge Conflicts

**Problem:** Identifying conflicts before merging branches.  
**Solution:** Use a dry-run merge to check for conflicts:

```sh
git merge --no-commit --no-ff <branch>
```

## 5. Simplify Commands with Aliases

**Problem:** Repeatedly typing long Git commands.  
**Solution:** Create shortcuts for common commands:

```sh
git config --global alias.co checkout
git config --global alias.st status
```

This allows you to shorten commands like `git checkout` to `git co`.

```sh
git co <branch> 
```

You can even add common options to your aliases.
For example, to always use the `-m` flag when committing, you can set up an alias like this:

```sh
git config --global alias.cm 'commit -m'
```

Now to write a commit message, you can use:

```sh
git cm "Your commit message here"
```

You can see all the aliases you have set up by running:

```sh
git config --global --get-regexp alias
```

## 7. Remove local branches that have been deleted remotely

**Problem:** You or another lab member have deleted a branch on the
remote repository, but it still shows up in your local repository.  
**Solution:** Use the following command to remove local branches that have been deleted remotely:

```sh
git fetch --prune
```

This command will remove all local branches that have been deleted on the remote repository.
