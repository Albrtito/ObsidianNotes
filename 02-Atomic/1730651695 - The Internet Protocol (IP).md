---
aliases:
  - The Internet Protocol (IP)
  - IP
tags:
  - incomplete
  - Networks
References: 
cssclasses:
---
# The Internet Protocol (IP)
There are two versions of IP in use today, [[1730826735 - Protocol - IPv4 protocol|IPv4 protocol]] and **IPv6**. 

+ IP addresses are technically associated with an interface rather than with the host or router containing that interface.
+ Every internet interface **must have an IP address that is UNIQUE** 
+ We can use [[1730832772 - CIDR Notation|CIDR]] notation to reference **groups of IP addresses.**
  
  > [!ATTENTION] REMARK:
  > Really important to know about CIDR and understand what this notation means

## IPv4 vs IPv6
The IPv6 protocol has been created with  several advantages over the IPv4, however a widely accepted network protocol such as IPv4 is not easy to change. 
### Transition, tunneling:
The transition between these two protocols needs to be slow and stedy, changing all systems in a matter of days is not viable given that there are billions of system active right now. 

> [!bug] Problem: 
> The old hardware will only support IPv4, there is no way of making it use IPv6.  


> [!check] Solution
> The **solution that has been adopted is TUNELING**. 

***