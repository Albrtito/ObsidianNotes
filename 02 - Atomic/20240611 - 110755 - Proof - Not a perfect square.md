---
aliases:
  - Not a perfect square
tags:
  - review
  - CalcI
"References:": 
cssclasses:
sr-due: 2024-06-14
sr-interval: 3
sr-ease: 250
---
# Proof - Not a perfect square: 

> [!NOTE] Proof
> 
Given $n \in N$ **not a perfect square**, prove that: 
>$$
\sqrt{n} \not \in \mathbb{Q}
>$$
>**Hint:**  Write n as $n = z^2r$ where: 
>+ r is a number with no squares

1. Take p and q both integer numbers such as: 
$$
\gcd (p,q) = 1
$$
and: #Duda Why do we start like this?
$$
{p^2\over q^2} = n
$$
2. Taken this definition we now have that: 
$$
p^2 = n \cdot q^2 = z^2q^2r
$$
Then: #Duda: How is it that we arrive her if the r cannot be taken out with the square? If we just take it with the square root no problem. Same for step 3.
$$
p = r \cdot k 
$$
3. Redefine p: 
$$
r^2k^2 = z^2q^2r
$$
We can simplify to obtain: 
$$
q^2 = {k^2 \over z^2} r
$$
This means that: 
$$
q = r \cdot m
$$
4. We have obtained a contradiction because of the multiplicity of r in both p and q. This means that our initial assumption is not correct. 
The contradiction: 
$$
gcd(p,q) \geq r
$$
