# DOM

!!! note
    This isn't necessary information for software development in lab but it provides better rounded knowledge of web development.

The DOM is the data representation of the objects that comprise the structure and contents of a document on the web.

### What is a web document?

A web document is simply a file you access through a web browser. This is typically written at it's core in HTML (HyperText Markup Language). It defines the structure and content of a web page.

### What is the DOM

In short, the DOM is a programming interface for all web documents. It represents the page so that programs can change the document structure, style, and content. The DOM is built using multiple APIs that work together.

In most cases the DOM serves as a programmatic representation of an HTML document. It's how browsers internally structure your page in memory so that code such as JavaScript can interact with it. JavaScript will interact with the DOM to change things in memory to adjust the web document.

### Why can't JavaScript directly interact with HTML instead of the DOM?

JavaScript can't directly interact with raw HTML text because once a browser has loaded a page, that HTML text is no longer "alive". Once a browser page has loaded it has been parsed into a structured model (the DOM) that JavaScript can work with in memory to change the rendered page.

To clarify this further, HTML lives on the server hosting a web page, whereas JavaScript lives in the browser, therefore allowing for constant manipulation of the web page by working with DOM in memory.

If you make changes to an HTML document, you must reload the page to view the changes. If you manipulate the DOM, you can see those changes real-time, due to it living in memory.

### Do browsers create their own DOM?

Yes, all browsers build their own DOM from HTML. However, each browser uses the same specifications given by [W3C](https://www.w3.org/TR/WD-DOM/introduction.html) / [WHATWG](https://dom.spec.whatwg.org/) to ensure the JavaScript used to manipulate the DOM will act consistently across all.

### HTML --> DOM --> JavaScript interactions simplified

#### HTML

Defines the structure and content of a web page. It is made up of just plane text. **Often thought of as the recipe or blueprint.**

###### *Example*
```HTML
<h1>Hello</h1>
<p>This is a paragraph</p>
```

#### DOM

Turns the plain text into a tree of objects in memory. **Often thought of as the ingredients or materials**

###### *Example*

	Document
	 └── html
	      └── body
	           ├── h1
	           └── p

#### JavaScript

Manipulates the in memory tree of objects. **Often thought of as the chef/laborer who works with the ingredients/materials**

###### *Example*

	`document.querySelector("h1").textContent = "Goodbye";`