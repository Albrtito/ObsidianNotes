---
Date: 2024-03-19
tags:
  - review
  - CalcI
"References:":
  - "[[Calc_Theory_Limits.pdf]]"
sr-due: 2024-06-20
sr-interval: 56
sr-ease: 252
---
# Limit: 
This note tries to explain the proper (formal) definition of limit, even if I cannot even begin to comprehend it. #Duda 


> [!NOTE] Definition:
> **We say that the function f TENDS TO THE LIMIT l** IF when x approaches $x_0$ f approaches l. 
This is written: 
>$$
\lim_{x\rightarrow x_0}f(x) = l
>$$
>
>**Formally** this is written as:
>
**The function f tends to the limit l if:**
>+ $\forall \epsilon > 0$ 
>+ $\exists \sigma > 0$
>+ $|f(x) - l| < \epsilon$
>
>
>**Satisfying**: 
>  + $0< |x-x_0| < \sigma$
>  
>  
>  
> **On the oder hand: The function f does NOT tend to the limit l if:**
> 
>+ $\exists \epsilon > 0$ 
>+ $\forall \sigma > 0$
>+ $|f(x) - l| > \epsilon$
>  
>**Satisfying**: 
>  + $0< |x-x_0| < \sigma$
> 

**Remarks:**
 In order to show how to use this last part to prove that a limit is computed correctly we give an example: 
 
 f.e: 
	Example: 2.1. $\quad \lim _{x \rightarrow 4}(3 x-7)=5$ since $|3 x-7-5|=3|x-4|<\varepsilon$ is obtained if we take $\delta=\varepsilon / 3$.

This means that we **do not care** about the values of f far from x = $x_0$ , only the ones close to it. 

+ The definition of limit is based on points inside a [[20240603 - 102925 - Definition - Neighbourhoods|Neighbourhoods]]

## Properties: 

> [!NOTE] Uniqueness of the limit:
> If a limit exists, it is unique. If l and m both satisfy as the limits of f in $x_0$, then l must be equal to m: l = m


