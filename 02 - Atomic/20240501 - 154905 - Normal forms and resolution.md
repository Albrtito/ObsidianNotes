---
aliases:
  - Normal forms and resolution
tags:
  - review
  - Logic
"References:": 
cssclasses:
---
# Normal forms and resolutions: 
## Intro and definitions: 

The objective of normalising formulas is to reduce the complexity required to deal with formulas in First-Order logic. In oder to follow we need to define two concepts: 

**Literal formulas:** Any formula that is: 
+ An atomic formula (Positive literal)
+ A negation of an atomic formula (Negative literal)
**Clause**: Any disjunction of one or more literal symbols. f.e: the formula $L_1 \lor L_2…\lor L_n$ 
	where: 
+ Each L is a literal
+ If n = 0. This is called empty clause and denoted as $\lambda$
+ Clauses with zero or one positive literal are called **Horn clauses**
## The equivalence theorem: 
![[20240501 - 155450 - Theorem - Equivalence theorem|The equivalence theorem]]
## PRENEX Normal Form: 
![[20240501 - 161016 - PRENEX Normal form|PRENEX Normal form]]
## SKOLEM Normal form: 
![[20240501 - 165252 - SKOLEM Normal Form|SKOLEM Normal form]]

## Resolution: 
![[20240501 - 171518 - Proof method Resolution|Resolution proof method]]
