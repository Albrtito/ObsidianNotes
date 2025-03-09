---
aliases:
  - DB Relational dynamics
tags:
  - FilesAndDB
References: 
cssclasses:
---
# DB Relational dynamics

> [!NOTE] Intro: 
>  The relational dynamics of a model are responsible of **changing the state of the set of relations that create the database.**
>  + Changes are done in some time
>  + In order to perform the changes a language in required
>  + Operators can either inspect or change.

## Relational languages: 
Relational languages are: 
+ Domain spacific
+ Declarative
+ Of specification type

Two types of languages are described based on their approach to obtain results. 
1. **Relational algebra:** Describes the changes to be done.
2. **Relational calculus:** Describes the goal to achieve.
### Relational Algebra:

Operators are classified into unary and binary. 
+ **Unary operators**: Only applied to one relation 
+ **Binary operators:** Applied to two relation 
+ **Bin. Compatible:** Applied to two relations but:
	+ Must have the same degree
	+ Must have the same data nature (two by two). We call this being compatible.
Unary operators of relational Algebra: 
1. **Selection:**
$$
\sigma_{\text{predicate}} = \text{<value>} \text{(Relation)}
$$
Selects all values of the selected relation where the given predicate takes the value chosen. 

 2. **Projection:** 
$$
\pi_{atrib1,atrib2...} (Relation)
$$
Creates a subRelation that contains only the selected attributes from the original relation. 


This algebra lets any chain of operators (expresions) be assigned into a symbol, this is called **renaming**.
$$
\rho_\text{symbol} (Expression)
$$
$$
S \equiv Expression
$$

Bin. compatible operatores of relational Algebra: Set operators.
1. **Union:** Obtain all non-repeated tuples from both tables. 
   + Both tables must be compatible
$$
	\cup
$$
2. **Intersection:** Obtain all repeated tuples (both relations have them) from both tables.
	+ Both tables must be compatible
$$
	\cap
$$

3. **Difference:** Obtain that appear on the first relation but are not present on the second one.
$$
-
$$

Binary operators or Join operators. Require two tables but those tables must not be compatible or meet any criteria. 

1. **Cartesian product:** Obtain every combination of tuples of both relations. 
	$$
	   X
	$$
2. **Join:** Subset of the cartesian product where a condition is met. 
$$
   \leq | \geq | =
$$
	1. **Natural join:** A particular case of the join operator, where the applied condition is the equality. 
	   $$
	   $$
	   
