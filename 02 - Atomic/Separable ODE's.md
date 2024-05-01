Date: 2024-02-08
Class: #DiffCalc 
References: [[Integration tips&tricks]]

---

# Order 1 Separable ODE's
Separable ODE's are of the form: 
$$
M(x) + N(y) \frac{dy}{dx} = 0

$$
+ M(x) is a function in x: Only x as the unknown
+ N(y) is a function in y: Only y as the unknown

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
### Examples: 
Here are some examples while writing in VIM. 