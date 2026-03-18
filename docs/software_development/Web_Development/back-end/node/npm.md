# npm (Node Package Manager)

npm is the default package manager bundled with Node when installing directly from [NodeJS](https://nodejs.org/) or via a [Node Version Manager (NVM)](./node.md#installation-maclinux-and-windows). npm consists of a CLI tool (primarily used for installing packages and executing code/tests) and it also has access to the largest online software registry (containing millions of different packages).

Similarlily to Pixi, npm focuses on localized package management rather than global. Each project contains it's own package.json file which includes the following belonging to the respective project:

- A list of packages and their versions
- Scripts
- Licenses
- Authors
- Project description 
- ...

The localized packages ensure the runtime Node environment has access **ONLY** to the packages needed for the current execution. This avoids environment managemenet and cross project dependency issues commonly faced using pip or conda for Python projects.

By default the npm CLI has a baked in "install" command that will install all packages within the current working directory. For the project you are currently inside of, simply run `npm install`. This will search for a package.json file in the local directory and install the package versions listed there inside of a folder called `node_modules`.

# Scripts
For any project there are usually several scripts (often referred to as tasks in other package managers) preconfigured for repeated processes. This usually includes building (build), start/dev (live executing the application), or test (live testing the application). These scripts live within your package.json and will look like each of the code blocks below.

### Back-end

#### Standard execution for ExpressJS
Any of these commands can be invoked by writing `npm`, then following with the script/task name Ex. `npm start`.


```JSON
"scripts": {
	"start": "node app.js",
	"devstart": "nodemon app.js",
	"test": "mocha --exit"
},
```

#### Standard execution for NestJS
Any of these commands can be invoked by writing `npm` or `npm run`, then following with the script/task name Ex. `npm run start`.


```JSON
"scripts": {
    "build": "nest build",
    "format": "prettier --write \"src/**/*.ts\" \"test/**/*.ts\"",
    "start": "nest start",
    "start:dev": "nest start --watch",
    "start:debug": "nest start --debug --watch",
    "start:prod": "node dist/main",
    "lint": "eslint \"{src,apps,libs,test}/**/*.ts\" --fix",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:cov": "jest --coverage",
    "test:debug": "node --inspect-brk -r tsconfig-paths/register -r ts-node/register node_modules/.bin/jest --runInBand",
    "test:e2e": "jest --config ./test/jest-e2e.json"
}
```


### Front-end
#### Standard execution for [CRA (Create React App)](https://create-react-app.dev/)

Any of these commands can be invoked by writing `npm`, then following with the script/task name Ex. `npm start`.

```JSON
"scripts": {
    "start": "react-scripts start", # Runs the project locally (typically executed for development)
    "build": "react-scripts build", # Builds the project into a lightweight deployable format
    "test": "react-scripts test", # Tests the app using integrated Jest test runner (not configured for most projects in the lab)
},
```

#### Standard execution for [Vite](https://vite.dev/)

Any of these commands can be invoked by writing `npm run`, then following with the script/task name Ex. `npm run dev`.

```JSON
"scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview"
}
```
