# React

React is a JavaScript library for building UIs. It follows a component-based architecture that allows for easy manipulation of the web browsers [virtual DOM](../../dom.md) for dynamic and interactive applications.

React is the most crucial library used in the lab for front-end development. This library remains consistent across all web applications and will continue to be the case, versions do vary though. 

For the most part React applications are built as single-page applications, meaning a singular HTML page exists as a base that has it's contents translated to the DOM, which can be constantly manipulated using a mixture of JavaScript/React.

For syntax sake, i like to think of React as a combination between JavaScript and HTML into a singular application workflow. React removes many complexities needed for JavaScript manipulation of the DOM and uses HTML(ish) syntax.

### Ex: Pressing a button in JavaScript
In JavaScript you must add a listener to fetch the element in DOM. Then manipulate the DOM yourself.
```JS
<button id="btn">Click me</button>
<script>
	const btn = document.getElementById('btn');
	let count = 0;
	btn.addEventListener('click', () => {
		count++;
		btn.textContent = `Clicked ${count} times`;
	});
</script>
```

### Ex: Pressing a button in React
In React you don't need to add listeners or even intentionally interact with the DOM. By simply talking React language, it'll work with the DOM for you.

```JSX
function CounterButton() {
	const [count, setCount] = useState(0);
	return (
		<button onClick={() => setCount(count => count + 1)}>
		    Clicked {count} times
	    </button>
	);
}
```

**Note:** In the example above useState stores the current value of ***count*** and a function (***setCount***) to update it. Whenever the update function (***setCount***) is called, an automatic re-render is triggered so the UI can reflect the change. This completely removes the heavy lifting of needing to get the element by Id, add a click event listener, then manually update the text content when the count value changes.

### Key Characteristics
- Reusability: Components/elements are designed to be used multiple times across multiple parts of an application.
- Modularity: Each component encapsulates it's own logic and styling. Making the code easier to manage, test, and debug.
- Encapsulation: Components tend to manage their own state and behavior, which avoids unintended behaviors in other parts of the app.

