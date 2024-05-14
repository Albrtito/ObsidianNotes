---
tags:
  - Discrete
  - review
DateCreated: 2024-02-05
"References:":
  - "[[Basic Set Operations]]"
aliases:
  - Elementary Combinatorics
---
# Elementary combinatorics
This is an introduction to combinatoric concepts. Combinatorics are also called counting methods. They are the main object of study of discrete mathematics. This methods are used to count possibilities. 

## Basic definitions: 

We’ll turn possibilities into sets, a set A is said to contain all the possibilities of some event happening. Then we can **count how many possibilities there are** inside that set, this count is called **cardinality**

> [!NOTE] Cardinality
> Given a set S, its cardinality |S| represents with integer value the number n of different elements inside the set S. Namely, the size of the set

**Remarks:**
+ Two sets have the same cardinality <=> There exist a bijective function between them 
	+ This means we can find a function that turns any value of A into an unique value of B and vice versa
+ A **countable** set is one with finite cardinality or cardinality = $\mathbb{N}$
	+ Zero element set: $\emptyset$ 
	+ Finite number of elements

### Sum and product principles:
Because we are defining the collection of possibilities as sets it is useful to us to define some operations that can be made between these sets and the number of possibilities each one contains. The two main operations used are **addition and multiplication** from which the **product principle** and **the sum principle** are obtained. 

> [!NOTE] Addition of cardinalities
> For two disjoint and finite sets, we can add their cardinality and obtain their union's cardinality
> **Conditions:**
> 	A and B disjoint
> 	A and B finite
> **Result:**
> 	|A U B| = |A| + |B|
> If the sets are **not disjoint**
> $|A U B| = |A| + |B| - |A\cap B|$
> 

+ This applies with  as disjoint possibilities can be summed. 

When this is generalised we get: 
![[20240515 - 010006 - Principle - Sum principle|Sum principle]]


Multiplication of cardinalities is given by the product principle: 
![[20240515 - 010522 - Principle - Product principle|Product principle]]

## Counting methods: 

## Cardinality of the power set: 

> [!NOTE] Corollary 32
> Definition of the power set as the set **contains all possible subsets of A**
> $$
> |P(A)| = 2^{|A|}
> $$
>

**Proof:** Sum all the possible subsets for each of the possible number of elements in the subset. Based on the [Newton's Binomial Theorem](Newton's%20Binomial%20Theorem.md) when x = 1 and y = 1.
## [Inclusion exclusion principle](Inclusion%20exclusion%20principle.md)
+ We'll se cases with 3 sets, a maximum of 4 in the worst case. 
## [Pigeonhole principle](Pigeonhole%20principle.md)
+ Useful for problems
## [Distributions](Distributions.md)
For a set of r distinct elements, division into r sets so that there are always those sets and elements but **the number of elements in each set varies** , compute possibilities. Applications in equations
### [Set partitions](Set%20partitions.md)
Given a set S, divide it into a certain number of partitions and compute the possible number of n partitions. The cardinality of those partitions is usually specified. 