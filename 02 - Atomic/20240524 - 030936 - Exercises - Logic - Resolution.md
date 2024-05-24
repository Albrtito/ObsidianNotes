---
aliases:
  - Exercises - Logic - Resolution
  - Logic - Submission - 7.2
tags:
  - review
"References:": 
cssclasses:
---
# Exercises - Logic - Resolution: 

## 1. Verify correct deduction by resolution: 

$$
\forall x  \exists y P(x,y) \Rightarrow  \exists y \forall x P(x,y)
$$
1. Turn the formula into resolution form:
$$
\forall x  \exists y P(x,y) \land \lnot[  \exists y \forall x P(x,y)]
$$
2. Get the PRENEX equiv: 

**DELETE COMPOUND NEGATIONS:**
$$
\forall x \exists y P(x,y) \land \exists x \forall y \lnot P(x,y)
$$

**TAKE OUT THE QUANTIFIERS:**
$$
\forall x \exists u( \exists y P(x,y) \land \forall y \lnot P(u,y))
$$