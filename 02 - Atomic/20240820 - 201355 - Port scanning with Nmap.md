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
Nmap uses by default [[20240820 - 202516 - SYN scan|SYN scan]] over the top 1000 TCP ports. However the scan needs root privileged, without it the TCP scan will be performed.

Specifying scan types: 
+ `-sS` : **SYN scan**
+ `-sT`: **TCP scan**

### SYN scan: 
If we ask for the package trace we will see that each SYN scan is composed of request and responses with the following structure: 

**REQUEST (example):**
```shell
SENT (0.0429s) TCP 10.10.14.2:63090 > 10.129.2.28:21 S ttl=56 id=57322 iplen=44  seq=1699105818 win=1024 <mss 1460>
```
+ TCP: Used protocol
+ **10.10.14.2:63090 > 10.129.2.28:21**: IPv4 addresses and their respective ports from and to which the packets are being send.
+ **S:** SYN packet is being send
+ **more:** Other TCP parameters
**RESPONSE (example): **
```shell
RCVD (0.0573s) TCP 10.129.2.28:21 > 10.10.14.2:63090 RA ttl=64 id=0 iplen=40  seq=0 win=0
```

Same as the request, however here we can see two different flags for the RST packet and ACK packet (RA).

### TCP Connect Scan
+ Using the `-sT` flag
+ Uses the three-way handshake to scan each port.
+ **stealthier than SYN**
	+ No unfinished connections → less likely to be detected
	+ More polite 
	+ Does not disturb services running on the network
+ **Slower** → Needs to wait for the target to answer
### UDP scan: 
+ Use the `-sU` flag
+ Much slower than the -sS
### Version scan: 
Scan versions, service names and details about the target. 
+ Use the `-sV` flag

## Defining ports: 
Some useful flags for port definition: 
+ **List of target ports:** `-p <portNum>, <portNum>, ...`
+ **Port range:** `-p <portNum>-<portNum>`
+ **Use top ports:**(Defined by the Nmap database) `--top-ports= <number>` 
+ **All ports:** `-p-`
+ **Fast port scan:** (top 100 ports) `-F-` 
## Filtered ports: 
Filtered ports are those that cannot be properly scanned, **nmap does not know what to do.** 
This status can be set by either two things: 
1. The packet has been **dropped**
2. The packet has been **rejected**

+ packet is dropped = **scan is longer**
+ packet is rejected = **look at the package trace for an unreachable port (ICMP error code)**
