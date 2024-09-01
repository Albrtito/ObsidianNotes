---
aliases: [<%+ let userTitle = await tp.system.prompt("Enter the text to append to the current title:");%>]
tags:
  - review
"References:": 
cssclasses:
---
<%* 
// Prompt the user for a title to append
let userTitle = await tp.system.prompt("Enter the text to append to the current title:");

// Get the current file title
let currentTitle = tp.file.title;

// Append the user's input to the current title
if (userTitle) {
    let newTitle = currentTitle + " " + userTitle;
    await tp.file.rename(newTitle);
} else {
    await tp.file.rename(currentTitle + " - Untitled Suffix");
}
%>
# <% userTitle %>

