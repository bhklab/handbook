# Merging Pull Requests

!!! note "For Maintainers"
    Only a subset of members of the BHK Lab organization can merge pull requests.
    If you are a maintainer, you can merge a pull request by following the steps below.

## Squash Merge

We will be using the squash merge strategy for merging pull requests.

> Squash merges are a way to combine multiple commits into a single commit.
> Instead of seeing all the author's individual commits in the main branch's
> commit history, you can see a single commit summarizing all the changes.

<figure markdown="span">
  ![squash-merge](./images/squash-merge.png)
  <figcaption>Squash merge example</figcaption>
</figure>

More information on squash merges can be found in the [GitHub Docs on Squash Merges](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges#squash-and-merge-your-pull-request-commits)

This has a few benefits:

1. It keeps the commit history clean and organized.
2. It reduces the number of commits in the main branch, making it easier to manage.
3. Avoids the `Merge branch 'main' into main` commit that is created when merging
   a pull request in favor of using the `PR` title as the commit message.

## Merging a Pull Request

To merge a pull request, follow these steps:

1. Click on the "Merge pull request" button.
