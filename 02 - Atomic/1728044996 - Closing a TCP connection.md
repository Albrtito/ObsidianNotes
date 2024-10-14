---
aliases:
  - Closing a TCP connection
  - Closing TCP
tags:
  - review
  - Networks
References: 
cssclasses:
sr-due: 2024-10-27
sr-interval: 13
sr-ease: 230
---
# Closing a TCP connection

To close a TCP connection the **FIN** flag is used: 

1. One host sends a FIN flag
2. The other host ACKs the FIN flag + Send it’s own FIN flag
3. ACK the last FIN flag

**Remarks:**
+ Cases such as **simultaneously FIN flags** can be handled
***
