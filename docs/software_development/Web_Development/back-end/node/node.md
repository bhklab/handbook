# NodeJS

[NodeJS](https://nodejs.org) is a runtime environment that allows you to run JavaScript code outside of a browser. By default all browsers have compilers that can interpret and execute JavaScript code, hence they can render web applications that are using React, Vue, Angular, or plain JS seamlessly. However, when running JavaScript code outside of a browser compiler, you will need to have NodeJS installed.

Many different projects in the lab use different versions of Node so using a tool such as a NVM (Node Version Manager) is a must. A NVM allows you to install and toggle between different versions of Node which is important since different projects utilize different library/package versions only compatible with specific node versions.

Most legacy projects in the lab use Node version 14-16. This includes projects like PharmacoDB, SynergxDB, ToxicoDB, KulGaP, XevaDB, PredictIO, cclid, and ORCESTRA. More recent projects like the Pmatch web-app, Science Portal, CoBE, lab website, and the new ORCESTRA rework fall into Node versions 18-22. If new applications are to be created in the lab it is recommended to adopt newer node versions (as of writing this that's 22) so we can ensure the Node versions and packages installed for them will be updated and maintained for many years to come and will not require manual package updates as frequently.

## Installation (Mac/Linux and Windows)

For Mac/Linux users you can install an NVM [here](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script)

For window users you will need to install a differerent NVM [here](https://github.com/coreybutler/nvm-windows)

Both NVMs work very similarly and provide almost identical functionality for installing and toggling between Node versions.

### Listing current versions:
``` Bash
nvm list
       v16.20.1
       v16.20.2
       v18.16.0
->     v18.19.1
       v20.17.0
       v22.21.1
       v24.12.0
```

### Installing New Versions

``` Bash
nvm install 21
Downloading and installing node v21.7.3...
Downloading https://nodejs.org/dist/v21.7.3/node-v21.7.3-darwin-arm64.tar.xz...
########################################################### 100.0%
Computing checksum with shasum -a 256
Checksums matched!
Now using node v21.7.3 (npm v10.5.0)
```

### Toggling New Versions

``` Bash
nvm use 21.7.3
Now using node v21.7.3 (npm v10.5.0)
```