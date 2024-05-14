---
aliases:
  - Counting methods
tags:
  - review
  - Discrete
"References:": 
cssclasses:
---
# Counting methods: 
When computing the possibilities of some event A happening we’ll encounter different types of restrictions for A. Based on these restrictions we can categorise different counting methods to compute the number of possibilities (or cardinality) of some A.
This event A is usually the possibilities 



> [!NOTE] Proposition 23: Ordered subsets
> Instead of just substracting one (like in permutations) and using the factorial to compute it, now there are **an specific number of spots to arrange the elements**. 
Subtract one until there are no more spots left
>
+ Formula: Compute the permutation and delete the unwanted spots
$$
n!\over (n-r)!
$$
	**r: The number of spots to arrange** 
		+ Specify where to stop


+ **Allowing repetitions**: If two elements can repeat, then no need of subtracting one each time, just multiply by the number of elements in the set the number of times equal to the spots u have. This means. 
$$
n^r
$$

> [!NOTE] Subsets
> + Using the [Binomial coefficients](Binomial%20coefficients.md)
> + **The order does not matter**
> + " From n choose r": Choose pairs of r from a set of n elements
>

$$
\binom {n}{r} = {n!\over r!(n-r)!}
$$
The [Pascal's triangle](Pascal's%20triangle.md) represents the number of possible subsets for different size's of sets. 
