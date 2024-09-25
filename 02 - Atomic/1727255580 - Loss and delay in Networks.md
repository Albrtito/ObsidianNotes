---
aliases:
  - Loss and delay in Networks
tags:
  - review
  - Networks
References: 
cssclasses:
---
# Loss and delay in Networks

Each router has a queue:
+ Loss happens when the queue is full.

## Sources of packet delay: 
1. **Processing:**
2. **Queueing:**
3. **Transmission:**
4. **Propagation:** RTT. Time to do a round trip. 

## Nodal delay:
$$
d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}
$$
The whole delay is based on the delay genreated by the four types of delay:
+ **Queueing delay:** 
  R : Link bandwitdth (bps)
  L: Packet length (bits)
  a : average packet arrival rate (pck/s)
  $$ \text{traffic intensity } = {La\over R}$$
  Traffic intensity gives the measure of how intense the trafic is. 
  + La → bits comming in
  + R → bits going out
  Traffic intensity can be either: 
  + Near to zero: If there is a ton of bandwith and little packages
  + Near to 1: Same bandwith and packets sent. (lots of delay)
  + Greater than one: Infinite delay. We cannot do anything with this.
## Packet loss:
If the buffer is full, the packet will be dropped. 

## Throughput:
Rate at which bits are transfered. 
+ Instantaneous: A one specific momento
+ Average: Self explanatory.

***