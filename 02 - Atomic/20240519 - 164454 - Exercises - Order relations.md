---
aliases:
  - Exercises - Order relations
tags:
  - review
  - Discrete
"References:":
  - "[[Discreta_Exercises_All_Solved.pdf]]"
  - "[[20240519 - 165004 - Order Relation|Order relations]]"
cssclasses:
  - page-manila
---
# Exercises - Order relations

## 13.1: 
+ **Obtain the Dom and Image:** Because it is reflexive the image and domain are equal to A.
+ **Obtain the Hasse diagram:** Apply the algorithm
+ **Obtain a total order compatible with R**: We can directly obtain $1\preceq 2 \preceq 3 \preceq 4 \preceq 5$
## 13.2: 
Let A the set A = {0, 1, 2} × {2, 5, 8}, and let us define the order relation R on A such that (a, b)R(c, d) ⇔ (a + b) | (c + d). Find the maximal, minimal, maximum, and minimum elements of the poset (A, R)

First we transform the relation into a more comprehensible form by obtaining the value of the sum of the coordinates at each point.
After doing so we can create the Hasse graph with those values and see that: 
+ There is no maximum or minimum
+ The maximals and minimals are directly obtained following the rules:
**Remember:**
**Maximals**: Those nodes that have no edges from them to another node. (No outgoing edges). (remember than with Hasse graphs, even if the arrows are not drawn the edges are directed)

**Minimals:** Those nodes with **no incoming edges** 

**Maximum:** A node such as it **is a maximal** and no other node is also a maximal
**Minimum:** A node such as it **is a minimal** and no other node is a minimal.

## 13.3: 
Let us consider the relation R on R2 given by $$(a, b)R(c, d) ⇔ a ≤ c \text{ and } b ≤ d $$ Find the maximal and minimal elements of the set $$C ⊆ R_2: C = {(x, y) ∈ R_2 : x^2 + y^2 = 1} $$Find sup(C) and inf(C) by considering C as a subset of R2.

Set C is defining all the points that exist in the **unit sphere of radius 1**. 
For all of those values, we obtain that all the maximals (those for which no value relates with **them**) are the points where x and y are both positive. 
All the minimals (points that relate with no one) are the ones when x and y are both negative. 

**maximals:** $\{(x,y) \in C / x, y \geq 0\}$
**minimals:**$\{(x,y) \in C / x, y \leq 0\}$

The supremum and minimum is found by deducing that for any point of A to be greater than any point of C, then this point has (x,y) both greater or equal to 1. Then the minimum of these points is (1,1)

The infimum is obtained in a similar way, however this time the point must have (x,y) smaller or equal to -1. Then the **infimum is (-1,-1)**

## 13.4: 
Let A be the set A = {n ∈ Z : 2 ≤ n ≤ 12}, and let us define on A the order relation R given by: n R m ⇔ n | m, or n is prime and n ≤ m . 

Tell the maximal, minimal, maximum, and minimum elements of the poset (A, R)

**Just painting the Hasse graph, solution with exercises**

## 13.5: 
Consider the two binary relations on set N:
$$
\begin{aligned}
& a \mathcal{R}_1 b \Leftrightarrow \exists n \in \mathbb{N} \text { such that } a=b^n, \\
& a \mathcal{R}_2 b \Leftrightarrow \exists n \in \mathbb{N} \cup\{0\} \quad \text { such that } a=b^n .
\end{aligned}
$$
1. Show that $\mathcal{R}_1$ is an order relation. Is $\mathcal{R}_2$ also an order relation? Is $\mathcal{R}_1$ a total order?

In order to show that it is an order relation we need to show that the three properties of order relations comply: 
+ **Transitivity:** 
+ **Anti-symmetry**
+ **Reflexivity:**

We conclude.
+ The R1 relation is an order relation.
+ The R2 relation is also an order relation as the 0 does not affect the three properties. 
+ R1 is not an total order: Total orders need for all the elements to be related to another one(besides itself). Based on the definition, prime numbers won’t be able to relate to any other number. 

2. Find the Hasse diagram of both relations on the set
$$
A=\{n \in \mathbb{N}: 1 \leq n \leq 9\}
$$
3. Find for $\mathcal{R}_1$ and $\mathcal{R}_2$ the maximal, minimal, maximum, and minimum elements on $A$. Find also the supremum and infimum of $A$ as a subset of $\mathbb{N}$

Minimal and maximal elements are directly obtained from the Hasse diagram. Only for the R2 relation is there any 