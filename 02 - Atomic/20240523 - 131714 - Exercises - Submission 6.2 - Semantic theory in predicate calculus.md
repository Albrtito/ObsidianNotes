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

## 2: Evaluation of a formula given **a domain and definition of the predicates**: 

| x   | y   | P(x,y) | Q(x) | Q(y) | P(x,y)→Q(y) | ∃y(P(x,y)→Q(y)) | $\forall x \exists y$ (P(x,y) → Q(y)) |
| --- | --- | ------ | ---- | ---- | ----------- | --------------- | ------------------------------------- |
| a   | a   | 1      | 1    | 1    | 1           | 1               | 1                                     |
| a   | b   | 1      | 1    | 0    | 0           | 1               | 1                                     |
| b   | a   | 0      | 0    | 1    | 1           | 1               | 1                                     |
| b   | b   | 1      | 0    | 0    | 0           | 1               | 1                                     |

## 3: Given a domain D = {a,b}:
![[Screenshot 2024-05-23 at 13.53.07.png]]
The formula is true for every interpretation. **THEN:**
+ It is semantically valid in the domain. However it is only valid in **this domain**

## 4: Given a domain D = {a}
Verify the formula: 
$$
\forall x (P(x) \lor \forall x Q(x)) \rightarrow \forall x(P(x) \lor Q(x))
$$
