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
	+ Proof of symmetry: In particular, if the c in the original definition was a b, there would be symmetry:  aRb and bRb => bRa 
	+ Proof of transitivity: aRb and bRc => cRa => (by the just proved symmetry) aRc

## 11.8: Weakly transitive
A relation R on a set A is weakly transitive if, for all elements a, b, c, d ∈ A, the relations aRb, bRc, and cRd imply that aRd. Determine which one of the following two statements is true and which one is false (by proving the former, and giving a counter- example of the latter): 
1. Every symmetric and weakly transitive relation is transitive. 
2. Every reflexive, symmetric, and weakly transitive relation is an equivalence relation.

We have a definition of R such as: 
$$
aRb, bRc, cRd \Rightarrow aRd
$$
**Proof:**
1. If a relation is symmetric 