# Lab Server

## Accessing the Lab Server

The lab server is accessible in a manner similar to H4H. 

Complete SSH instructions can be found **[here](https://bhklab.github.io/HPC4Health/remote_development/ssh/#ssh-password-based-authentication)**.

### TLDR: SSH without password
In your home directory, create a new key with the following command:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
Save the key in the default location `(~/.ssh/id_rsa)` by pressing Enter. Leave the passphrase empty to enable passwordless login.

To automatically add your public key to the `~/.ssh/authorized_keys` file on the container
```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub -p <PORT> <USERNAME>@<HOSTNAME>
```
Enter the password to the container when prompted.

To create an alias for the server, add the following to your `~/.ssh/config` file:
```bash
Host labserver
    HostName <HOSTNAME>
    Port <PORT>
    User <USERNAME>
    IdentityFile ~/.ssh/id_rsa
```

You should now be able to SSH into the server without a password.
```bash
ssh labserver
```

## I can't see any files in the home directory

This likely means the server was rebooted and the directory needs to be re-mounted. 

To re-mount the home directory, run the following command:

```bash
sudo mount -a
```

If you are still having issues, please contact Jermiah Joseph or the lab coordinator.