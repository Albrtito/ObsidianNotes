---
Syntax: "{{comand} | {{command}}"
Definition: A pipe redirects the STDOUT of a command to the STDIN of the next one
---
+ Use pies to filter the result of a command: [grep](grep.md)
		Ex: `ls | grep .txt` only the results containing .txt of the ls output will be shown. 

+ Redirections work as many times as needed. 
		Ex: `find /etc/ -name *.conf 2>/dev/null | grep systemd | wc -l
		The find command output is given to the grep command, the grep command filters, then the output is used by the [wc](wc.md) command that counts the number of files there are. 
