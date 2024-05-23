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
