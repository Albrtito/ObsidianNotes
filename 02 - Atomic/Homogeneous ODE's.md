## Order 1 Homogeneous ODE's

The homogeneous equations we'll work with are: 
+ First order: The highest derivative for y is the first derivative
The form of the homogeneous equations is of type: 
$$
M(x,y) + N(x,y){dy\over dx} = 0
$$
### Conditions: 
For an ODE to be homogeneous it has to comply with:
$$
M(tx,ty) = t^\alpha M(x,y); N(tx,ty) = t^\alpha N(x,y)
$$

Or it has to be able to be rewritten as a factor of x/y or y/x.
$$
{dy\over dx} = F(x/y) | {dy\over dx} = F(y/x)
$$

### Solving: 
Once checked that the ODE is homogeneous we apply the following: 
1. Obtain F() where the function only depends on x/y or y/x and equals to the derivative of y wrt x. 
2. Apply [[u-substitution]] where u = x/y or y/x depending on what F() depends of. 
3. Based on the u-substitution there will be a value for y based on u: 
	1. For y/x: $y/x = u : y = ux$
	2. For x/y: $x/y = u : y = x/u$
4. Then there will also be a value for the derivative of y based on u. 
	1. $y/x = u : y = ux \Rightarrow {dy\over dx} = u + x{du\over dx}$
	2. $x/y = u : y = u/x \Rightarrow {dy\over dx} ={u - x{du\over dx} \over x^2}$
5. This new ODE we obtain based on u has to be [[Separable ODE's]] after we simplify. Then we can solve it as such
6. Finally just undo the u-substitution
