---
aliases:
  - CIDR Notation
  - CIDR
  - Classless Interdomain Routing
tags:
  - incomplete
  - Networks
References: 
cssclasses:
---
# CIDR Notation:
> CIDR: Classles Interdomain Routing

## Intro:
When working with IP addresses we use CIDR notation to **reference groups of IP Adresses.**

If we want to reference large groups of IPs we could just say: 
> “from the 192.34.23.0 to the 192.34.23.255

Which would theoretically include all the ones with any value in the fourth and the same values for the first three ones.

However, because we study computer science and life could not make things easier for us we opt for using another notation (sure it makes some things easier), this notation is based on **the number of bits that define the group of IP addresses we are refering to.** 

> In the previous example we could say that the first 24 bits are the ones that define the group as they never change. Then we write:
> $$ 192.34.23.0/24$$

Finally 
***