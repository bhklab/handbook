# GitHub Access

In order to use GitHub on the lab server, you will need to use an SSH key set up in your GitHub account.

First check that you [have an SSH key set up](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys) on your local machine for your GitHub account. If you don't, follow the guide on [generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

You can then follow GitHub Docs' guide on [using SSH agent forwarding](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/using-ssh-agent-forwarding) to forward your SSH key to the lab server.

- On step 2 under "Setting up SSH agent forwarding", add the `ForwardAgent yes` line under the lab server alias you set up in your `~/.ssh/config` file.

## Mac Specific Step for SSH Agent Forwarding
If you are setting up SSH agent forwarding on a Mac, there is an extra step that you need to take for your local `ssh-agent` to "remember" the key.

After you've set up your SSH key, import the SSH keys into Keychanin using this command:
```bash
ssh-add --apple-use-keychain YOUR-KEY
```

This will add the key to your local `ssh-agent` and allow you to use it for SSH agent forwarding.

[Read more](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/using-ssh-agent-forwarding#your-key-must-be-available-to-ssh-agent)