---
aliases:
  - Madani fuzzy system
tags:
  - IA
References: 
cssclasses:
---
# Mamdani fuzzy system
1. Fuzzification
2. Rule evaluation
3. Composition 
4. Defuzzification

## 1. Fuzzification:
It turns the data either into a: 
+ **fuzzy singleton:** Data do not have noise, nice and single value
+ **fuzzy set:** Data has noise, more values

## 2. Evaluation:
1. **Match the fuzzified inputs with antecedents** #Duda Why the antecedentse? What is the antecedents?
	+ This can be done by matching the disjunction(OR) of the rule antecedents of matching the conjunction (AND) of the rule antecenteds
2. **Compute the consequent** by applying either clipping or scaling of the antecent. 

	+ **Clipping:** Most common method
$$
Q(x) = min(S, \,u)
$$
***