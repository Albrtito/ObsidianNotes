---
aliases:
  - Saving Nmap scan results
tags:
  - Cyber
"References:": 
cssclasses:
---
# Saving scan (Nmap) results: 

Nmap saves the results in 3 different formats: 
+ `.nmap` extension: flag `-oN`
+ `.gnmap` extension (grepable output): flag `-oG`
+ `.xml` extension: flag `-oX`

The **xml** can be converted to html for better readability using the `xsltproc` tool: 
```shell
xsltproc target.xml -o target.html
```

