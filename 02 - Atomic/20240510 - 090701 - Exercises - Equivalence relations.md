---
aliases: 
tags:
  - review
  - Discrete
"References:":
  - "[[Discreta_Exercises_All_Solved.pdf]]"
cssclasses:
  - page-manila
---
# Exercises - Equivalence relations


## 11.4:
Let R be a relation defined on N × N, such that $(a, b)R(c, d)$ if and only if a + b = c + d. 
Show that R is an equivalence relation on N × N, and that there exists a bijection between the quotient set (N × N)/R and N.

The relation can be defined as a function f, then: 
$$
f(a,b) = a + b = c+ d = f(c,d)
$$
## 11.6: 
We define the relation R on R2 = R × (R \\ {0}) such that
$$
(a, b) \mathcal{R}(c, d) \quad \Leftrightarrow \quad a d=b c 
$$
Show that this is an equivalence relation, and obtain the quotient set $R_2/\mathbb{R}$

## 11.7: Circular relation
A relation R defined on a set A is a circular relation if it verifies the following property: 
$$
aRb \text{ and } bRc \Rightarrow cRa $$
Prove that a relation is an equivalence relation if and only if it is circular and reflexive.

+ **All equivalence relations are circular**
$$
\text{Equivalence} \Leftrightarrow \text{Circular and Reflexive}
$$
**Proof:**
1. **If** it is equivalence and aRb and bRc => (transitivity) aRc => (Symmetry) cRa **=>** **circular**
2. **If** R is circular and reflexive =>? Symmetric and transitive 
	+ 
