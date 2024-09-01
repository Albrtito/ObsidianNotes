---
aliases: 
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

// Prompt the user to enter a custom alias
let customAlias = userTitle;
if (customAlias) {
    // Get the current aliases from the frontmatter (if any)
    let aliases = tp.frontmatter['aliases'] || [];

    // Add the new alias to the aliases array
    aliases.push(customAlias);

    await tp.frontmatter.update("aliases", aliases);
    } else {
        // Optional: Handle the case where no alias was provided
        new Notice("No alias was provided. The alias will not be updated.");
    }
%>

# <% tp.file.title %>


