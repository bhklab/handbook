# [Configuring UHN VPN](#configuring-vpn)

## Quick introduction: why do we need a VPN?

A Virtual Private Network (VPN) is essential in the workplace to ensure secure and private access to the company network, especially when working remotely or on public Wi-Fi. 

A VPN encrypts internet traffic, protecting sensitive data from potential cyber threats and unauthorized access. This helps maintain confidentiality, ensures data integrity, and supports secure access to internal resources, safeguarding the organization's digital environment.

GlobalProtect is UHN's VPN service for workers. GlobalProtect provides secure, encrypted access to the corporate network, ensuring users can safely connect to company resources from any location, while maintaining data security and compliance with organizational policies.

## Steps for configuring VPN on personal devices

Most likely you will need to configure the VPN on your personal device. The person onboarding you or your supervisor will probably tell you so and either request VPN access to IT for you or help you to do it.

IT will generally accept the request quickly, and send instructions to your corporate email on the steps to follow to install and configure the VPN.

If you are a Windows or Mac user, that's it. The manual is pretty good, simple and straightforward. Follow the steps and you've got this. Easy.

If you are on Ubuntu... There's no downloading link or steps. You get stuck on the very first step. Don't worry, you don't have to open a ticket on Helpdesk and wait for them to respond... The next section will make things easier for you.

## Downloading GlobalProtect software on Ubuntu
After contacting Helpdesk a few times, I finally got an email with the downloading instructions for Ubuntu. Here I leave the email, I think it may be useful.

> Download the installation file from the [link](https://roseshare.rose-hulman.edu/portal/s/162637781701644125980.tgz) or via the curl command: 
>    
    curl https://roseshare.rose-hulman.edu/portal/s/162637781701644125980.tgz --output PanGPLinux-5.3.0-c32.tgz --ciphers 'DEFAULT:!DH'

> Unzip tar file, by running: tar -xvf PanGPLinux-5.3.0-c32.tgz

> Install the program:

> On Ubuntu/Debian, this is done through the command:
>
    sudo dpkg –i GlobalProtect_deb-5.3.0.0-32.deb

> On Redhat/CentOS, this is done through the command:
>
    sudo yum localinstall GlobalProtect_rpm-5.3.0.0-32.rpm

> To start the program, simply enter in a shell
>
    globalprotect 
    
> and then a prompt should display.

> From the prompt, run 
>
    connect -portal connect2.uhn.ca


> Login with your email address (username@uhn.ca) as your username and password.

> Type quit to exit the prompt.

## That's it - just remember connecting and disconnecting the VPN every time you neet it

Now that you have your laptop configured for the VPN, don't forget connecting every time you want to use it, running the following command:

    globalprotect

And then running in the prompt:

    connect -portal connect2.uhn.ca

When you want to disconnect from the VPN, you have to run

    globalprotect

And then in the prompt:

    disconnect