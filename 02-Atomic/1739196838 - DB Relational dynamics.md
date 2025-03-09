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
+ **Bin. Compatible:** Applied to two relations but output 1
Unary operators of relational Algebra: 
1. **Selection:**
$$
\sigma_{\text{predicate}} = \text{<value>} \text{(Relation)}
$$
Selects all values of the selected relation where the given predicate takes the value chosen. 

 1. **Projection:** 
$$
\pi_{atrib1,atrib2...} (Relation)
$$
Creates a subRelation w
***