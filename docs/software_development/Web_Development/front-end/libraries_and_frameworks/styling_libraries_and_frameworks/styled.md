# Styled-components

[Styled-components](https://styled-components.com/) is another JavaScript library utilized for styling web applications components. It's frequently used in many of the legacy applications such as PharmacoDB, SynergxDB, ToxicoDB, KulGaP, XevaDB, PredictIO, cclid, ORCESTRA, and the lab website. So, for maintaing sake, it is good to have a good grasp on how styled-components works and how it differs from defining raw CSS or utilizing traditional utility-first styling (like [TailwindCSS](./tailwindcss.md)).

When using styled-components, you don't directly create a classes, instead you create a new instance of a component, with the option of adding embedded classes afterwards.

In the example below as you can see we define a new div component called "Wrapper" with it's own unique stylings. Within the "Wrapper" div component we also define a local classname called "title" which only exists in the scope of the component it is defined within. This does help significantly to keep styling local and not have too many spill over issues that occur when editing styling classes and having many cascading effects in the rest of your application where they are used.

```JavaScript
const Wrapper = styled.div`
	padding: 4em;
	background-color: white;
	.title {
		font-size: 1.5em;
		text-align: center;
		color: #BF4F74;
	}
`;

return (
  <Wrapper>
		<h2 classname="title">
			Hello World!
		</h2>
  </Wrapper>
);
```