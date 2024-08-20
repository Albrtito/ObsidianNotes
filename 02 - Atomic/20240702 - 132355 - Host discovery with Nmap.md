---
aliases:
  - Host discovery with Nmap
tags:
  - Cyber
"References:":
  - "[[20240701 - 181920 - Nmap|Nmap]]"
cssclasses:
---
# Host discovery with nmap: 
Host discovery is the act of searching for online targets we can work with.

## Scan types: 
**By default Nmap uses the ICMP echo request** to search for active host. 

Most of these scans disable the port scanning (-sn) this is because we don’t really care about the state of each port, only if the machine is online. 
## Scanning the network range:
Used to see which hosts are active inside a network.
```shell
sudo nmap <IP-range> -sn -oA <fileName> | grep for | cut -d" " -f5
```
+ The grep and cut commands are used to simplify the output. 
+ If the target firewalls don’t allow the scan it wont work
### Scanning multiple addresses: 
+ Use the `-iL <filePath>` flag to input a list of target hosts.
