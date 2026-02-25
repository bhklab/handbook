# React Hooks
React hooks are special functions that let you "hook into" React features. This includes things like state, lifecycle, and context, without writing classes. They were introduced in React 16.8 (2019)

Before hooks came along, React components were either
- Class components (with this.state, componentDidMount, etc)
- Stateless functional components (no lifecycle or state)

Hooks let you write everything as a simple function component, while still giving you:
- State (useState)
- Lifecycle effects (useEffect)
- Context (useContext)
- References (useRef)

### useState
Stores local, reactive state in a function component. Calling the setter triggers a re-render.
Ex.

```JSX
function CounterButton() {
	const [count, setCount] = useState(0);
	return (
		<button onClick={() => setCount(c => c + 1)}>
		    Clicked {count} times
	    </button>
	);
}
```

Same code functionality pre Hooks:
```JS
class CounterButton extends React.Component {
	constructor(props) {
		super(props);
		this.state = { count: 0 };
		this.increment = this.increment.bind(this);
	}

	increment() {
		this.setState(prev => ({ count: prev.count + 1 }));
	}

	render() {
		return (
			<button onClick={this.increment}>
				Clicked {this.state.count} times
			</button>
		);
	}
}
```

TO BE CONTINUED...