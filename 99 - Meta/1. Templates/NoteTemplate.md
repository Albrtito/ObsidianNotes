---
aliases:
  - 
tags:
  - review
"References:": 
cssclasses:
---
<%* 
let userTitle = await tp.system.prompt("Enter title");
// Prompt the user for a title to append
// Get the current file title
let currentTitle = tp.file.title;

// Append the user's input to the current title
if (userTitle) {
    let newTitle = currentTitle + " " + userTitle;
    await tp.file.rename(newTitle);
} else {
    await tp.file.rename(currentTitle + " - Untitled Suffix");
}
let frontmatterTitle = userTitle || "Untitled";

let frontmatter = 
`
--- 
aliases: 
	- ${frontmatterTitle} 
tags: 
	- review 
"References:": 
cssclasses: --- `;
%>
# <% userTitle %>

