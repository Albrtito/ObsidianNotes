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
+ The maximals and minimals are

**Remember:**
**Maximals**: Those nodes that have no edges from them to another node. (No outgoing edges). (remember than with Hasse graphs, even if the arrows are not drawn the edges are directed)

**Minimals:** Those nodes with **no incoming edges** 

**Maximum:** A node such as it **is a maximal** and no other node is also a maximal
**Minimum:** A node such as it **is a minimal** and no other node is a minimal.