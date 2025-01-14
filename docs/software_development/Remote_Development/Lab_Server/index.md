# Lab Server

## Accessing the Lab Server

The lab server is accessible in a manner similar to H4H. 

SSH instructions can be found [here](https://bhklab.github.io/HPC4Health/remote_development/ssh/#ssh-password-based-authentication)


## I can't see any files in the home directory

This likely means the server was rebooted and the directory needs to be re-mounted. 

To re-mount the home directory, run the following command:

```bash
sudo mount -a
```

If you are still having issues, please contact Jermiah Joseph or the lab coordinator.