# TailwindCSS

[TailwindCSS](https://v3.tailwindcss.com/docs/installation) is a utility-first framework for styling components in React. In every new web application project within the lab Tailwind is installated and utilized for core styling.

Due to our developer team being quite small in the lab, utilizing Tailwind is crucial when developing web applications in a timely manner because it removes several steps when styling components, hence saving a signficant amount of time. Traditionally, when styling a React component you must assign it a class, create a CSS file, create a new class in the CSS file that corresponds to the class given to your component, then write in your stylings. When Tailwind is installed and configured it has a large collection of preset classes (utility classes) that can be written inline on a component classname that will apply certain stylings to it. This means that you **NEVER** need to create extra CSS files and rarely define your own classes.

Above the time saving aspect, Tailwind also ensures consistent styling (due to predefined utilities), easy to setup inline response designs utilizing media queries (this is not possible inline without Tailwind), and hover/focus, along with other state variants.

In lab projects we primarily use v3.4.17 but v4 has been recently released, so newer applications can bump to take advantage of their new simplified setup, "high performance engine", larger colour palette, and new 3D transformations.

## Tailwind Example

If you want to add a `flex` display orientation to a div element, you would simply write it inline like such:

```JavaScript
<div class="flex flex-row ...">
	.
	.
	.
</div>
```

This would apply the following classes manually without creating a css file for it

```CSS
.flex {
	display: flex;
}
.flex-row {
	flex-direction: row;
}
```

## Robust Tailwind Comparison

![tailwind-component](../../../images/tailwind-component.png)

If you want to create the above component with raw CSS, you would need to define the following.

```JavaScript
<div class="chat-notification">
	<div class="chat-notification-logo-wrapper">
		<img class="chat-notification-logo" src="/img/logo.svg" alt="ChitChat Logo">
	</div>
	<div class="chat-notification-content">
		<h4 class="chat-notification-title">ChitChat</h4>
		<p class="chat-notification-message">You have a new message!</p>
	</div>
</div>

<style>
	.chat-notification {
		display: flex;
		align-items: center;
		max-width: 24rem;
		margin: 0 auto;
		padding: 1.5rem;
		border-radius: 0.5rem;
		background-color: #fff;
		box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
	}
	.chat-notification-logo-wrapper {
		flex-shrink: 0;
	}
	.chat-notification-logo {
		height: 3rem;
		width: 3rem;
	}
	.chat-notification-content {
		margin-left: 1.5rem;
	}
	.chat-notification-title {
		color: #1a202c;
		font-size: 1.25rem;
		line-height: 1.25;
	}
	.chat-notification-message {
		color: #718096;
		font-size: 1rem;
		line-height: 1.5;
	}
</style>
```

If you utilize Tailwind you can simply write the following:

```JavaScript
<div class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg flex items-center gap-x-4">
	<div class="shrink-0">
		<img class="size-12" src="/img/logo.svg" alt="ChitChat Logo">
	</div>
	<div>
		<div class="text-xl font-medium text-black">ChitChat</div>
		<p class="text-slate-500">You have a new message!</p>
	</div>
</div>
```

As you can see, once you are comfortable utilizing Tailwind styling, it will become significantly faster to develop core components of an application.