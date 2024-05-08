
Date: 2024-02-05
Class: #Discrete 
References: [Basic Set Operations](Basic%20Set%20Operations.md)

---


> [!NOTE] Cardinality
> Given a set S, its cardinality |S| represents with integer value the number n of different elements inside the set S. Namely, the size of the set

+ Two sets have the same cardinality <=> There exist a bijective function between them 
	+ This means we can find a function that turns any value of A into an unique value of B and vice versa
+ A **countable** set is one with finite cardinality or cardinality = $\N$
	+ Zero element set: $\emtpyset$ 
	+ Finite number of elements
	
> [!NOTE] Proposition 14
> For two disjoint and finite sets, we can add their cardinality and obtain their union's cardinality
> **Conditions:**
> 	A and B disjoint
> 	A and B finite
> **Result:**
> 	|A U B| = |A| + |B|
> If the sets are **not disjoint**
> $|A U B| = |A| + |B| - |A\cap B|$
> 

> [!NOTE] Proposition 15: Sum principle
> With infinite disjoint sets. We can apply the **Proposition 14 as many times as we want to** (usually with not disjoint sets)
>

+ This applies with  as disjoint possibilities can be summed. 

> [!NOTE] Propositions 17 to 19: Product principle
> **Conditions:**
> + A and B are finite
> 
> **Result:**
> $|A * B| = |A| * |B|$
+ With multiple sets, this maintains. In this case $A_i$ are different sets.
 
$$
\prod^m_{k=1} |A_K|
$$
+ **Usefulness** 
	+ create unique pairs between sets. 
	+ Break down procedures into smaller ones: If a procedure can be broken down into tasks that are consecutive. Then the ways of doing the procedure are computed by multiplying the multiplicities of the tasks. 

> [!NOTE] Proposition 21,22: Permutations
> Possible arrangements, **no specific number of spots to arrange the elements**
Place one object and subtract one from the cardinality of the set that is being ordered. 
> 
> **Result:**
> + Just use the factorial for basic permutations


+ **Permutations with repetitions:** For repeated elements in a set the arrangements cannot repeat. Those repeated arrangements have to be deleted. 
  To delete the repeated arrangements divide by the number of those repeated arrangements. The number is computed as a normal permutations (with the factorial). The final formula is: 
$$
  \binom{n!}{n_1!...n_k!} = {n! \over n_1!...n_k! }
$$

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