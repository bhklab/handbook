# Quick Start

When connecting to H4H for the first time, here are some recommended action items:

## Set up your `.bashrc` file

??? example "TLDR: Complete `.bashrc`"
    ```.vim
    # .bashrc

    # Source global definitions
    if [ -f /etc/bashrc ]; then
            . /etc/bashrc
    fi

    # User specific environment
    if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
    then
        PATH="$HOME/.local/bin:$HOME/bin:$PATH"
    fi
    export PATH

    # Uncomment the following line if you don't like systemctl's auto-paging feature:
    # export SYSTEMD_PAGER=

    # User specific aliases and functions
    if [ -d ~/.bashrc.d ]; then
            for rc in ~/.bashrc.d/*; do
                    if [ -f "$rc" ]; then
                            . "$rc"
                    fi
            done
    fi

    unset rc

    # BHKLAB additions
    # User specific aliases and functions
    alias bhklab="cd /cluster/projects/bhklab"
    alias radiomics="cd /cluster/projects/radiomics"

    # File permission setting
    # Gives rwx for user and group, r-x for other
    umask 002
    ```

The `.bashrc` file is a configuration file for the Bash shell. For a full description of this file, you can check out [this article](https://phoenixnap.com/kb/bashrc#:~:text=bashrc%20file%20is%20a%20configuration,%2C%20shortcuts%2C%20and%20visual%20tweaks.).

To view it, start in your home directory on H4H. You can open the file with your favourite text-editor. If you're unfamiliar with those, you can start with [nano](https://linuxize.com/post/how-to-use-nano-text-editor/)

```bash
$ pwd
/cluster/home/<YOUR_H4H_USERNAME>
$ nano .bashrc
```

By default, it should look something like this:

```.vim
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
        for rc in ~/.bashrc.d/*; do
                if [ -f "$rc" ]; then
                        . "$rc"
                fi
        done
fi

unset rc
```

For some convenience, we're going to add some extra settings to this file.

### Data Directory Aliases
First, to make it easy to get to the BHKLab data directories, we'll add two [aliases](https://medium.com/@jogarcia/bash-aliases-32f648e3a924):

```.vim
# User specific aliases and functions
alias bhklab="cd /cluster/projects/bhklab"
alias radiomics="cd /cluster/projects/radiomics"
```

With these aliases, you can access the `bhklab` and `radiomics` data directories easily:

```bash
$ bhklab
$ pwd
/cluster/projects/bhklab
```

??? warning "Access requirement"
    To use these aliases, you need to be connected to a data node or compute node. See [Remote Access Nodes](https://bhklab.github.io/HPC4Health/setup/02_ssh_into_h4h/#remote-access-nodes) for instructions on how to access these.

    Additionally, when you set up your H4H account with Zhibin Lu, he would have granted you access to `bhklab`, `radiomics`, or `both`. This will determine which data directories you have access to.

### Default File Permissions
Second, to make sure any files, directories, etc. you make, either interactively or using a script, is accessible by other lab members, add the following:

```.vim
# File permission setting
# Gives rwx for user and group, r-x for other
umask 002
```

??? warning "Internal or Private data"
    If you work with any internal or private datasets, you may want to adjust the file permissions setup or utilize subgroups to restrict access. Contact the lab member listed next to High Performance Computing (HPC) on H4H on the [Lab Member Expertise](../../../onboarding_offboarding/Onboarding/lab_member_expertise.md) page if you need assistance.


## Interactive Jobs - `salloc`

Familiarize yourself with `salloc` by reading our documentation on [Interactive Jobs and Debugging](https://bhklab.github.io/HPC4Health/slurm/interactive_jobs/) and the [Slurm `salloc` documentation](https://slurm.schedmd.com/salloc.html).


## Submitting Jobs - `sbatch`
Familiarize yourself with submitting jobs by reading our documentation on [Submitting Jobs on H4H](https://bhklab.github.io/HPC4Health/slurm/submitting_jobs/) and the [Slurm `sbatch` documentation](https://slurm.schedmd.com/sbatch.html).

!!! example "Slurm header example"
    ```.vim
    #!/bin/bash
    #SBATCH --job-name=my_job_name
    #SBATCH --mem=8G
    #SBATCH --time 1:0:0
    #SBATCH --cpus-per-task 2
    #SBATCH --nodes 1
    #SBATCH --mail-user=bhklab.johnsmith@gmail.com
    #SBATCH --mail-type=BEGIN,FAIL,END
    #SBATCH --output="~/slurm_logs/%A-%x.out"
    ```
    
    * This will submit a job called "my_job_name".
    * It requests 2 CPUs with 8G of memory each for 1 hour. 
    * An email will be sent to `bhklab.johnsmith@gmail.com` when the job begins, fails, and/or ends.
    * Logs will be output as a file with the format `{job number}-{job name}` in a directory called `slurm_logs` in the user's home directory.