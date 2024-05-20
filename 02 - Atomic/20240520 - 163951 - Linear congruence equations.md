---
aliases:
  - Linear congruence equations
tags:
  - review
  - Discrete
"References:": 
cssclasses:
---
# Linear congruence equations
Linear congruence equations are a way of proposing the [Linear Diophantine equations](20240429%20-%20113931%20-%20Linear%20Diophantine%20equations.md). 

For this type of equations we ask whether there is a number x such as if multiplied by a the following relation would comply.  
$$
a \cdot x \equiv b \mod m 
$$
This can be rewritten as the Diophantine equation:
$$
b = a\cdot x + m y
$$
Where for a solution to be found the gcd of a and b (denoted as d) must divide b. 
$$
gcd(a,m)| b
$$
## Formal definition:

> [!NOTE] Definition: Congruence equation
> A congruence modulo m of the form: 
> $$
> a \cdot x \equiv b \mod m
> $$
> **Where**:
> + m is a positive integer
> + a,b are integers 
> + x is a variable 
> 
> **Then:** This is called a **congruence equation**

**Remarks:**
+ Obtaining the **multiplicative inverse** of $a \mod m$ is **equal to** $a\cdot x \equiv 1 \mod{m}$ **IF:** There is an **unique solution** for that relation. 
+ **If** x is a solution of a linear congruence equation **and**:  $x'\equiv x \mod{m}$. 
	**Then:** x’ is **also a solution of that equation.**
+ The solution of a linear congruence equation are the equivalent classes classes of congruence modulo m. Elements of $\mathbb{Z}_m$

