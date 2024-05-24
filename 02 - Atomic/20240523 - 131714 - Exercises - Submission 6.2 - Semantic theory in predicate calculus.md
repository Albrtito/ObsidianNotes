---
aliases:
  - Exercises - Submission 6.2 - Semantic theory in predicate calculus
  - Exercises - Semantic theory in predicate calculus
tags:
  - Logic
"References:": 
cssclasses:
---
# Exercises - Semantic theory in predicate calculus: 

## 2: Evaluation of a formula given **a domain and definition of the predicates**: With truth table

## 3: Given a domain D = {a,b}: With truth table
![[Screenshot 2024-05-23 at 13.53.07.png]]
The formula is true for every interpretation. **THEN:**
+ It is semantically valid in the domain. However it is only valid in **this domain**

## 4: Given a domain D = {a} with truth table
Verify the formula: 
$$
\forall x (P(x) \lor \forall x Q(x)) \rightarrow \forall x(P(x) \lor Q(x))
$$
![[Screenshot 2024-05-23 at 14.04.05.png]]
The formula is true for all interpretations. Then it is valid in domain D.

## 5. Verify formula with counterexample
$$
\forall x(P(x) \lor Q(x)) \rightarrow (\forall x P(x) \lor \forall x Q(x))
$$
In order to find a counter example (False interpretation) we look for: 
+ $\forall x(P(x) \lor Q(x))$ : true
	+ 
+ $(\forall x P(x) \lor \forall x Q(x))$ : false
	+ $\forall x P(x)$: FALSE
	+ $\forall x Q(x)$ : FALSE

We can try to find a counterexample in domain D = {a} however this counterexample is not possible: 
![[Screenshot 2024-05-23 at 14.22.58.png]]
+ See that we cannot fix P(x) ∨ Q(x)

However in a domain with two elements  D = {a,b} we can get a counterexample: 
![[Screenshot 2024-05-23 at 14.23.57.png]]

## 6: Verify the formula with counterexample: 
$$
\exists x (P(x) \land Q(x)) \rightarrow (P(y)\lor Q(y))
$$
The conditional needs to be false, then: 
$(P(y)\lor Q(y))$ is False while $\exists x (P(x) \land Q(x))$ is true meaning:  
+ P(y) is false
+ Q(y) is false

If we look in a domain D= {a} with free variable y = a we need for Q(y) to equal 0 while Q(a) equals 1. This is impossible. 
![[Screenshot 2024-05-23 at 17.36.37.png]]

However in a domain of two elements we can surely find a counterexample: 
![[Screenshot 2024-05-23 at 17.36.49.png]]

## 7: Verify the formula with counterexample
$$
\lnot \forall x A(x) \land \lnot (\exists x \lnot A (x))
$$
In order for the formula to be false we need one terms to be false. To simplify the quantifiers we do the following: 
$$
\exists x \lnot A(x) \land (\forall x  A (x))
$$
In a one element domain we get: 
D = {a}
![[Screenshot 2024-05-24 at 02.06.58.png]]
Proving a counterexample for D

## 8: Verify the formula with counterexample: 
$$
(\exists x A(x) \rightarrow \exists x B(x)) \rightarrow \forall x (A(x)\rightarrow B(x))
$$
For this formula, we prove a counterexample by proving that the conditional is false, then: 
+ $(\exists x A(x) \rightarrow \exists x B(x))$ : **TRUE**
+ $\forall x (A(x)\rightarrow B(x))$ : **FALSE**
There are no free variables, for a domain for D = {a} we have:

