---
aliases:
  - PRENEX Normal form
  - PNF
tags:
  - review
  - Logic
"References:": 
cssclasses:
---
# PRENEX Normal Form (PNF)
PRENEX normal form is a formula structure. For the logic course it is mainly used to obtain the SKOLEM Normal Form.
The PRENEX formula can **always** be obtained.

> [!NOTE] Definition
> A PRENEX normal form must: 
> + Only have connectives of type $\lnot, \land$
> + All negations must be atomic (no compound negations)
> 	This is an atomic negation: 
> 	$$
> 	\lnot A
> 	$$
> 	This is a compound negation:
> 	$$
> 	\lnot (A \land B)
> 	$$
> + All quantifiers must be at the beginning of the formula
> 

## Method to obtain PRENEX NORMAL FORM (PNF):
Given a formula A, we derive the PNF with the following steps:
1. Eliminate connectives different to $\land, \lnot, \lor$
	+ This is done using 