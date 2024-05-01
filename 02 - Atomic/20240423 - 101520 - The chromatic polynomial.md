---
aliases:
  - The chromatic polynomial
tags:
  - review
  - Discrete
"References:": 
cssclasses:
sr-due: 2024-05-25
sr-interval: 30
sr-ease: 273
---
If we wanted to properly color a graph with n colours, for each number of colours I choose it may be possible or not. And it may also be possible in different ways. In order to compute this different ways of coloring a graph with some number of colours n we use the chromatic polynomial.

> [!NOTE] The chromatic polynomial: 
> Given some graph G =(V,E) be a **simple graph** and let q≥ 2 be a natural number. 
> **THEN:**
> The chromatic polynomial $P_G$ is a polynomial such that $P_g(q)$ gives the number of distinct proper colorings of G with q $\in$ N colors. 
> 
> + q≥ 2 means we always use 2 or more colours. (importante because if we use 1 colour there is no problem). Of course it is a natural number because colours cannot be other than natural. 

**Remarks:**
+ This works if G is simple 

**Chromatic number**
Given some chromatic polynomial, we can define a minimum number of colours(q) needed such as P(q) $\not =$ 0. This number of colours (q) is called chromatic number and it’s represented as: 
$$
X^{(G)}
$$

## Theorems and methods: 
There are several methods to obtain the chromatic polynomial: 
+ sf
+ **Contraction-Deletion theorem**
	![[20240423 - 104039 - Theorem - Contraction-Deletion theorem|Contration Deletion theorem]]
### Theorems: 


> [!NOTE] Disconnected graphs
> If G is a disconnected graph with k ≥ 1 connected components. Naming each component $G_j$. We get: 
> $$
> P_G(q) = \prod^{k}_{j=1}P_{G_j}(q)
> $$
> 
> **Namely:** The chromatic polynomial is computed as the product of all disjoint components. 


> [!NOTE] Split a graph in two 
> **If** the graph G can be split into two parts G1 and G2 such that the intersection between those graphs is a complete graph: ($G_1 \cap G_2 = K_n)$ for some n ≥ 1
> **Then:** 
> $$
> P_G(q) = {P_{G_1}(q) \times P_{G_2}(q)\over P_{K_n}(q)}
> $$
> 

The polynomial will be computed as the quotient between the product of the polynomial of both parts divided by the polynomial of the complete graph, this one is easily computed as: 

![[20240423 - 105604 - Chromatic poly of a complete graph|Chromatic polynomial of a complete graph]]

**REMARKS:**
When computing the chromatic polynomial, the first idea is to use the product principle. If one vertex has q possible colours, then the one adjacent will have q-1. And so on. However when problems with this method appear it’s when we start applying any other method (almost always there will be problems)
## Polys of some known graphs: 
### Tree graph:
![[20240423 - 105748 - Chromatic poly of a tree graph|Chromatic poly of a tree graph]]

### Cycle graph: 
![[20240423 - 121056 - Chromatic poly of a cycle graph.#^7039f1]]

### Wheel graph: 
![[20240423 - 131817 - Chromatic poly of a wheel graph#^FinalSol]]
## Solved problems: 
