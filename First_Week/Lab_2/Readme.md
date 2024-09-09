# Lab2_Task

## Overview
In this project, I created a modern web page using HTML, CSS, and JavaScript. The page includes a responsive layout with sections for a header, main content, and footer. Additionally, I added a button that dynamically changes the content of a specific section when clicked.

## Technologies Used
- **HTML**: Structured the content of the web page.
- **CSS**: Styled the elements to create a modern, responsive design.
- **JavaScript**: Added interactivity to change content dynamically.

## Key Learnings

### `getElementById`
I learned how to use the `document.getElementById()` method to target specific elements in the DOM by their `id` attribute. This method is essential for manipulating HTML elements using JavaScript.

Example:
```javascript const textContentDiv = document.getElementById("text-content");```

In this example, I targeted the div element with the id of text-content.

I also learned how to use the textContent property to update the text inside an HTML element. This is useful for dynamically changing the content of a web page without reloading it.

```javascript textContentDiv.textContent = "This content has been updated using JavaScript!";```

This line of code replaces the existing content inside the targeted div with new text.