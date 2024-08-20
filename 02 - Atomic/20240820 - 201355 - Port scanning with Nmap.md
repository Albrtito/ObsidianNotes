---
aliases:
  - Port scanning with Nmap
tags:
  - Cyber
"References:": 
cssclasses:
---
# Port scanning with Nmap:
When scanning the target ports we wanna find the following information.

**Objectives:**
+ Find open ports and its services
+ Service versions
+ Information that the services provide
+ Operating system

As explained in the basic Nmap page, when Nmap scans a port it filters it as one of the following 6 states: 
1. **open**: Some app is listening
2. **filtered**: Something is blocking, cannot tell
3. **closed**: No app listening
4. **unfiltered**: Responsive port, however cannot tell if open or closed
5. **open|filtered** or **closed|filtered**: Cannot determine between the two states
## Scan types:
Nmap uses by default **SYN scan** over the top 100 TCP ports. 