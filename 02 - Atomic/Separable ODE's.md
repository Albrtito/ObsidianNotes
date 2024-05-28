Date: 2024-02-08
Class: #DiffCalc 
References: [Integration tips&tricks](Integration%20tips&tricks.md)

---

# Order 1 Separable ODE's

The difficult part for solving these equations is to integrate and restructure the equation so that the terms are separated. 


### Solving separable ODE's

1. Obtain $H_1(x) = \int M(x)$
2. Obtain:  $H_2(y) = \int N(y)$
3. **Fastest solution without thinking:** 
$$
C = H_1(x) + H_2(x)
$$
4. Now, if you wanna keep thinking: 
$$
\frac{d}{dx} H_1(x) + \frac{d}{dy}H_2(y) \frac{dy}{dx} = 0

$$
By the chain rule

$$
\frac{d}{dx} [H_1(x) + H_2(y) ] = 0

$$
Integrating...
$$
\int (\frac{d}{dx} [H_1(x) + H_2(y) ]) = H_1(x) + H_2(y) = 0

$$
