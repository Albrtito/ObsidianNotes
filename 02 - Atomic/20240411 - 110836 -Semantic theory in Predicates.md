---
aliases:
  - Semantic theory in Predicates
tags:
  - incomplete
"References:": 
cssclasses: 
sr-due: 2024-04-19
sr-interval: 4
sr-ease: 270
---
# Semantic theory in predicates: 

It is similar to the semantic theory in propositional calculus, however there is higher complexity on the interpretation required. 

## Evaluation of formulas:

**Remember:** In propositional calculus we have: 
+ Constants: Specific elements of the domain 
+ Variables: Assign to any element of the domain 
	+ Free variables
	+ Quantified variables
+ Functions: Assigns to specific applications, transformations between the elements of the domain. 

For each predicate an specific relation (n-ary) in the domain of reference is assigned. Predicates can not be true or false like propositions so the case **needs to tell us the values of the predicates for each element (or group of elements) in the domain.** 

f.e: 
	 For a domain D = {a,b} and the predicates P(x) and Q(x) the following table needs to be given.
	 ![[Screenshot 2024-05-08 at 12.39.50.png]]

If we start adding all the possible elements there are in predicate calculus we see that each and every one of them needs a given truth table. All of them: Functions,Prepositions, free variables and constants. This makes truth tables HUGE. As we need to think that these truth tables represent all possible combinations (without giving an specific truth table for each predicate but computing all possible truth tables that could be given)

f.e: 
	For the domain D = {a,b,c} and the formula: 
	$$
		\mathbf{P}(\mathbf{x}) \wedge(\forall \mathbf{x}(\mathbf{R}(\mathbf{f}(\mathbf{x})) \wedge \mathbf{P}(\mathbf{y})) \rightarrow \exists \mathbf{x}(\mathbf{x})) \vee \mathbf{p}
	$$
	We get the following truth table: 
	![[Screenshot 2024-05-08 at 12.44.50.png]]
	Where that one line marked would be equal to: 
	![[Screenshot 2024-05-08 at 12.43.42.png]]

Let’s see if there is any way of making this computation easier and faster.

### Evaluation of Quantifiers: 


When evaluating quantifiers the is is just evaluating whether the condition given by the quantifier holds: 
+ Universal quantifier: Holds if for all elements in the domain P(x) is true
+ Existential quantifier: Holds if for P(x) at least with one element in the domain is true.



