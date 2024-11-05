<%* 
// Prompt the user for a title to append
let userTitle = await tp.system.prompt("Enter title");
// Get the current file title
let currentTitle = tp.file.title;
// Append the user's input to the current title
let newTitle = userTitle ? `${currentTitle} ${userTitle}` : `${currentTitle} - Untitled Suffix`;
// Rename the file
await tp.file.rename(newTitle);

// Get a list of all folders in the vault
let allFolders = app.vault.getfolders().map(f => f.path);

// Prompt the user to select a folder
let selectedFolder = await tp.system.suggester(allFolders, allFolders, "Select a folder");

// Move the file to the selected folder
await tp.file.move(`${selectedFolder}/${tp.file.name}`);
-%>
---
aliases:
  - <%userTitle%>
tags:
  - incomplete
References:
cssclasses:
folder: <%selectedFolder%>
---
# <% userTitle %>
<% tp.file.cursor(10) %>