<%* 
// Prompt the user for a title to append
let userTitle = await tp.system.prompt("Enter title");
// Get the current file title
let currentTitle = tp.file.title;
// Append the user's input to the current title
let newTitle = userTitle ? `${currentTitle} ${userTitle}` : `${currentTitle} - Untitled Suffix`;
// Rename the file
await tp.file.rename(newTitle);
// Prompt the user for tags, separated by commas
let tagsInput = await tp.system.prompt("Enter tags (comma-separated)"); 
// Process the tags 
let tagsArray = tagsInput ? tagsInput.split(',').map(tag => tag.trim()) : [];
-%>
---
aliases:
  - <% userTitle %>
tags:
  - review
  - <% tagsArray.join('\n - ') %>
"References":
cssclasses:
---
# <% userTitle %>
<% tp.file.cursor(10) %>

