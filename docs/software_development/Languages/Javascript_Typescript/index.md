# JavaScript/TypeScript

## What is JavaScript

JavaScript is primarily known as a high-level (abstracted from complexity) programming language, most notably used in creating dynamic front-end web content. Due to it's versatility it has also been adopted to create APIs and run server side operations in full stack applications. 

### Why We Use JavaScript

JavaScript is the most common choice for the front-end and backend in full stack applications in the lab because of its ease of use, portability, improving performance, and how common it is in the industry. When learning web development you typically will end up using vanilla JavaScript or JavaScript libraries such as React, Vue, or Angular to start, making it a safe option for newcomers and seasoned developers.

### How to run JavaScript

For the front-end/client portions of JavaScript applications, there are no additional engines/compilers needed to execute code because browsers have built-in JavaScript engines (utilizing JIT) that will execute the code for you. However, when using JavaScript code server side (code execution by your machine) you will need a Node.js runtime environment to be installed on your computer because operating systems don't include them natively. The best way to install Node.js on your system and manage versions is using [nvm (Node Version Manager)](https://github.com/nvm-sh/nvm?tab=readme-ov-file#intro). Every project in the lab was likely developed with a different version of node, so making sure you are utilizing the ones compatible with the code/packages is important to ensure expected functionality.

## What is TypeScript

TypeScript is simply a superset language of JavaScript that provides additional functionality such as [static typing](https://www.TypeScriptlang.org/docs/handbook/2/basic-types.html#static-type-checking), [interfaces/types](https://www.TypeScriptlang.org/docs/handbook/2/objects.html), and [enums](https://www.typescriptlang.org/docs/handbook/enums.html#handbook-content) to name a few. The additional functionalities of TypeScript help you avoid errors before they happen (saves you debugging time), makes your code more predictable, and help others understand it easier. The best part about TypeScript is the fact that all JavaScript code is also valid TypeScript code (because TypeScript is a superset of JavaScript). This makes adding TypeScript to your arsenal easier for your next project and also makes incrementally adopting TypeScript into already existing JavaScript projects quite seamless.