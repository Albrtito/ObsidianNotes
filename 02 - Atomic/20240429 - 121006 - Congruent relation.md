---
aliases:
  - Congruent relation
tags:
  - review
  - Discrete
  - incomplete
"References:": 
cssclasses:
sr-due: 2024-05-02
sr-interval: 2
sr-ease: 248
---
# Def:

The congruent relation is defined as an [[Equivalence relations]].Where two elements are related if they are congruent: 

> [!NOTE] Congruent relation
> Two elements a and b are **congruent modulo m** if m | (a-b). This relation is denoted as: 
> $$
> a \equiv b(\mod m)
> $$

+ This means that **under the division by m**, a and b have the same remainder.
$$
\begin{gather}
m | a \Rightarrow m = qa + r_1 \\
m | b \Rightarrow m = kb + r_2\\\\
\boxed{r_1 = r_2}
\end{gather}
$$
**Remarks:**
+ a is related to b: $a \equiv b (\mod m)$ **if and only if**: $a (\mod m) = b (\mod m)$. **This means** exactly the same as what is said above. Both have the same remainder under the division by m
+ **If** $a \equiv b (\mod m)$ **then**: a = b + km $k \in Z$
# Equivalent relation: 

## Proving the equivalent relation:
In order to prove that the relation is equivalent the three properties of equivalent relations mus be proved: 

1. **Reflexivity:**
3. **Symmetry:**
4. **Transitivity**

## Equiv. classes and quotient set: 
The equivalence classes (or **congruent classes**) modulo m for an equivalent congruent relation of mod m are: 
$$
[a]_m = \{b\in Z: a \equiv (\mod m)\}k = \{a + mk : k \in Z\}
$$
Because this means nothing to anyone trying to understand this let’s explain it in a friendly way: 

Every time we create a relation mod m means dividing any element in the domain of the relation (Z) by m and looking at what the remainder of that division is. For some value of m we’ll have several possible remainders based on the number we divide by m.
	f.e: The relation based on the mod 4 means dividing by 4 and looking at what the remainder is, all the possible remainders we can get when dividing by 4 are 0,1,2,3. Then we can create the equivalent classes, one for each value that the remainder can take. 

**Remarks:** There are only m equivalent classes for the congruent relation mod m defined by the **quotient set of the relation**: 
This is the notation usually used: 
$$
Z_m = \{[0]_m,[1]_m,...,[m-1]_m\}
$$
More formally: 
$$
Z_m ) \{[a]_m: 0 \leq a \leq m-1 \}
$$

# Practice cases: 
## Clock: 


