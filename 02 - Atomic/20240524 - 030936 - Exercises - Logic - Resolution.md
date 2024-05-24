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
\forall x \exists y P(x,y) \land \forall y \exists x \lnot P(x,y)
$$

**TAKE OUT THE QUANTIFIERS:**
$$
\forall x \exists y \forall v\exists u(  P(x,y) \land  \lnot P(u,v))
$$

3. Get the SKOLEM equiv: 

**ONLY UNIVERSAL QUANTIFIERS:**
+ y → f(x)
+ u → g(v, x)

$$
\forall x  \forall v(  P(x,f(x)) \land  \lnot P(g(v,x),v))
$$
**OBTAIN A CLAUSE FORM:**
Or connectives together, divided by and connectives. 

Already in a clause form: 

C1: $P(x,f(x))$
C2: $\lnot P(g(v,x),v)$

No substitutions would lead to an empty clause. The **deduction is not correct.**

## 2. Verify correct deduction using resolution:
The premises are given one after the other, remember that the resolution method says: 
$$
p_1 \land p_2 \land ...\land p_n \land \lnot q
$$
**Then**: 

Premises:
$$
\begin{gather}
& \exists x \forall y(A(x, y) \rightarrow B(y, x) \vee C(y)) \\
& \forall x \forall y(D(x, y) \rightarrow \sim C(x)) \\
& D(a, b) \wedge \forall x \forall y A(x, y)
\end{gather}\\ 
$$
Conclusion:
$$
\exists x B(a, x)
$$
1. Formula into resolution form: 
$$
\begin{gather}
\exists x \forall y(A(x, y) \rightarrow B(y, x) \vee C(y)) \\
 \land \\
 \forall x \forall y(D(x, y) \rightarrow \sim C(x))
 \\ \land \\
 D(a, b) \wedge \forall x \forall y A(x, y)
 \\ \land \\
 \lnot [\exists x B(a, x)]
\end{gather}
$$
2. Transform into PRENEX: 

**DELETE COMPOUND NEGATIONS AND CONDITIONALS**
+ Use interdefinitions for the first two premises.
+ Same for conclusion 
$$
\begin{gather}
\exists x \forall y( \lnot A(x, y) \lor (B(y, x) \lor C(y))) \\
 \land \\
 \forall x \forall y(\lnot D(x, y) \lor \sim C(x))
 \\ \land \\
 D(a, b) \wedge \forall x \forall y A(x, y)
 \\ \land \\
 [\forall x  \lnot B(a, x)]
\end{gather}
$$
**TAKE OUT ALL QUANTIFIERS:**
+ Every duplicated quantifier is given a new variable. 
$$
\begin{gather}
\exists x \forall y( \lnot A(x, y) \lor (B(y, x) \lor C(y))) \\
 \land \\
 \forall u \forall v(\lnot D(u, v) \lor \sim C(u))
 \\ \land \\
 D(a, b) \wedge \forall x \forall y A(x, y)
 \\ \land \\
 [\forall x  \lnot B(a, x)]
\end{gather}
$$
