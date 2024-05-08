Is based on the Bar&Stars problem. distributions give the **number of possible orders of identical r objects into n distinct groups**
+ The number of sets is set
+ The number of objects is set
In oder to solve the problem with distributions the idea is to think about positions of the symbols (bars and objects), where bars are going to limit the groups of objects. 
If we think about it this way, for r identical objects and n boxes we need n-1 bars to limit the boxes. Then there are n + r - 1 symbols. From these symbols, we can compute the possible groups of bars or objects as they would be the same due to how the [Pascal's triangle](Pascal's%20triangle.md) works.

Example: 
If we had 10 identical balls and 3 children to distribute the balls, and some children could be with no balls at all then there are: 
r = 10 identical balls (*)
n = 3 children : n-1 bars (2 bars)() | )
$$
* * * * * * * * * * 
$$
A possibility would be: 
$$
* * * *| * * * |* * * 
$$
One child gets 4, another one 3 another one 3. 
Then there are a total of 12 symbols to arrange. We can compute the number of arrangements of one of the symbol types and we'll get them all: 
$$
\binom{3+10-1}{10} = \binom {3+10-1}{2}
$$

### Generalisation: 
Then, we can conclude that for r objects and n distinct groups:
$$
\binom{n+r-1}{r} = \binom {n+r-1}{n-1}$$
### For non empty groups: 
If a group cannot be 0, then it needs for it's contents to be greater or equal to 1. Then the formula would be: 
$$
\binom{r-1}{n-1}
$$

### Applications 
#### Equations: 
$$
x_1 + x_2 + x_3+...+ x_i = n \in \N
$$
There are i variables and the sum of them all is equal to n. Then this can be transformed into a distribution problem (7 identical balls and i children) and we get the possibilities of solutions for the equation. 

**Special cases:**
+ What if any variable cannot be 0? Then use the distribution for non-empty groups 
+ What if a certain variable cannot be 0, but the rest can? Apply directly the problem and draw the bars and variables 
+ What if a variable needs to be **greater or equal than a value**? Assign those values from the start and decrease n so that that variables is already given it's part before starting to compute
+ What if the value of a variable has to be **equal to a certain value?** Then we assign those values to the variable (subtract them form n) and act as if that variable didn't exist
+ What if the variable needs to be **smaller than a value**? There are two possible things we can do here: 
	+ Compute it as the complement of the possibilities of the variables being greater than the value. (based on the S set) (S set - solutions when greater)
	+ Compute the possibilities for it to be each one of the integers below the value given and sum them.