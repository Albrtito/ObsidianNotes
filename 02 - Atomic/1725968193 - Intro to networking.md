---
aliases:
  - Intro to networking
tags:
  - review
  - Networks
References: "[[Net_Biblio_Kurose.pdf#page=28]]"
cssclasses:
sr-due: 2024-09-14
sr-interval: 3
sr-ease: 250
---
# Intro to networking
## What is a/the net?
When we talk about the internet we are just describing a net of connected devices, nothing more. To have a connection we only need two **devices**, a data **transmission method** and a **medium** to do it in. 

**The telephone net:** A basic example is the telephone network where there each phone(device) is connected through a copper wire (medium) and sends electric signals to other phones (transmission method)
### A service description: 
As developers we won’t care about the whole structure and technicalities associated with it. We’ll actually work with the services that work because of the web. 
The web is **an infrastructure providing services to apps**. 
We differentiate between two types of apps: 
+ **Distributed apps:** Those that need the internet to work 
+ **Local apps:** Those that can run without the web
	+ f.e: The calculator

When developing an app we’ll have to choose the internet service that best suits us. (More about this on Internet service note)
## Fisionomía of the internet 

> [!NOTE] Host 
>We call **host or end system** to any device that is hooked to a net.  

+ Nowadays most of these end systems are portable devices while the initial host of the internet where traditional desktop workstations. 

In order to **connect all the host** to the network we use: 
+ [[1726049178 - Definition - Communication links|Communication links]] (the medium part of the net) 
+ [[1726049339 - Definition - Packet switches|Packet switches]] (More about this later)

When a computer sends any data, it **splits it into smaller parts (packets) and adds an explanatory header to each of them**, then this packets are send to the nearest switcher.

### Communication between nodes: 
**Remark:** There is a bijection between a net and a graph. Therefore we can use notation such as nodes to refer the host or switches and edges to refer the communication links
Computers communicate between them using [[1726049888 - Net protocols|Net protocols]]. These protocols give an **standard way of establishing a communication between two nodes**. 
Anyone can create a protocol, though most protocols used are public.
