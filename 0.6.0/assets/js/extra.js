function cleanupClipboardText(targetSelector) {

  const targetElement = document.querySelector(targetSelector);

  // Function to recursively iterate over nodes and filter out excluded elements
  function processNode(node) {
    // Base case: if the node is a text node, return its text content
    if (node.nodeType === Node.TEXT_NODE) {
      return node.textContent;
    }

    // If the node has children, iterate over them
    if (node.nodeType === Node.ELEMENT_NODE) {
      // Check if the node has a class that should be excluded
      if (node.classList && (node.classList.contains("go") || node.classList.contains("gp"))) {
        return ""; // Skip this node
      }

      // Iterate over child nodes and process them
      return Array.from(node.childNodes)
        .map((childNode) => processNode(childNode)) // Recursively process child nodes
        .filter((s) => s !== "") // Filter out any empty strings
        .join(""); // Join the processed text
    }

    return "";
  }

  const clipboardText = Array.from(targetElement.childNodes)
    .map((node) => processNode(node))
    .filter((s) => s !== "")
    // Remove `>>>` and `$` from the beginning of the line
    .map((s) => s.replace(/^(\$|>>>)/g, ""));

  return clipboardText.join("").trim();
}

// Sets copy text to attributes lazily using an Intersection Observer.
function setCopyText() {
  // The `data-clipboard-text` attribute allows for customized content in the copy
  // See: https://www.npmjs.com/package/clipboard#copy-text-from-attribute
  const attr = "clipboardText";
  // all "copy" buttons whose target selector is a <code> element
  const elements = document.querySelectorAll(
    'button[data-clipboard-target$="code"]',
  );

  if (elements.length === 0) {
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      // target in the viewport that have not been patched
      if (
        entry.intersectionRatio > 0 &&
        entry.target.dataset[attr] === undefined
      ) {
        entry.target.dataset[attr] = cleanupClipboardText(
          entry.target.dataset.clipboardTarget,
        );
      }
    });
  });

  elements.forEach((elt) => {
    observer.observe(elt);
  });
}

// Using the document$ observable is particularly important if you are using instant loading since
// it will not result in a page refresh in the browser
// See `How to integrate with third-party JavaScript libraries` guideline:
// https://squidfunk.github.io/mkdocs-material/customization/?h=javascript#additional-javascript
document$.subscribe(function () {
  setCopyText();
});

// document$.subscribe(function () {
//   const copyButtons = document.querySelectorAll('.btn-clipboard');
//   copyButtons.forEach(button => {
//     button.addEventListener('click', () => {
//       const codeBlock = button.closest('pre').querySelector('code');
//       const copyText = Array.from(codeBlock.childNodes)
//         .filter(node => !node.classList.contains('gp') && !node.classList.contains('go'))
//         .map(node => node.textContent)
//         .join('');

//       navigator.clipboard.writeText(copyText).then(() => {
//         console.log('Copied without prompt/output symbols!');
//       }).catch(err => {
//         console.error('Error copying text: ', err);
//       });
//     });
//   });
// });
