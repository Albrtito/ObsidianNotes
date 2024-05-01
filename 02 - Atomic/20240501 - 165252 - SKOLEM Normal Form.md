---
aliases:
  - SKOLEM Normal form
  - SNF
tags:
  - review
  - Logic
"References:": 
cssclasses:
---
# SKOLEM Normal Form (SKN)
SKOLEM normal form is a formula structure key for several automatic proof procedures (whatever that is)

> [!NOTE] Definition
> Features: 
> + Quantifiers must be in the head of the formula
> + Only universal quantifiers are allowed
> + The matrix of the formula is a conjuction of clauses 
> 	Namely: 
> 	The matrix formula is composed by valid formulas that only contain the $\lor$ connective cunjucted between them: $(Universal)[(F_1)\land(F_2)\land…\land (F_n)]$
> 	Where: $F_i$ only contains connectives of type $\lor$
> 	

## Procedure to obtain SKOLEM NORMAL FORM (SNF)
Given any formula A, it is possible to derive the SNF using:
1. Get the [[20240501 - 161016 - PRENEX Normal form|PRENEX Normal form]] of A
2. Bind free variables, adding existencial quantifiers to **the head** of the PNF(existencial closure)
3. Transform the matrix of the resulting formula using the equivalences: 
	+ Remember that because we have already transformed into the PNF there are no $\rightarrow$ or composite $\lnot$ connectives.
$$
	\vdash A\lor(B\land C)\leftrightarrow(A\lor B)\land (A\lor C)
$$
$$
\vdash(A\land B)\lor(A\land C)\leftrightarrow A\land(B\lor C)
$$
4. Remove all existential quantifiers, to do so: 
	1. Start processing existential quantifiers from left to right
	2. If $\exists$ as no $\forall$ on the left. Replace the variables with constants: 
		$$
			\exists x \forall y \forall x(P(x,y)\lor Q(x,z)) \Rightarrow \forall y \forall z(a,y) \lor Q(a,z))
	$$
	3. If $\exists$ has any $\forall$ on the left, replace the variable with a function depending on as many arguments as $\forall$’s on the left, using those very same variables as arguments.

$$
\forall y\forall z\exists x(P(x,y)) \lor Q(x,z)) \Rightarrow \forall y \forall z (P(f(y,z), y ) \lor Q(f(y,z),z))
$$
+ See that the variable x has been substituted by the function f(y,z)
+ If there where more existential quantifiers, **use different functions.** 
