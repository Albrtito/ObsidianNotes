---
aliases:
  - White box testing
  - Structural testing
tags:
  - review
  - SoftwareDev
"References:": 
cssclasses:
sr-due: 2024-05-05
sr-interval: 4
sr-ease: 277
---
# White box testing: 
## Intro:
Structural or white box testing focuses on the **internal structure of methods.** 
+ Test **all paths**

We care about whatever is in the box.
![[Pasted image 20240501124251.png]]

There are different techniques: 
+ **Control flow** : Look at the execution paths and create test for each of them. 
+ **Data flow**: Focus on the definition, usage and deletion of variables
All these techniques are **applied during unit-testing**
---

## Advantages: 
+ All code paths can be verified as tested or not. There is a countable number of them
## Disadvantages: 
+ Number of paths can be to large for testing
+ Difficult to detect **data sensitivity errors** (p = q/r) #Duda  Why so difficult?
+ **Assumes control flow is correct** (the implementation (it works), now we test if it works well or not) 
+ Need of programming skills 
 

## Types of white box testing: 
+ [[20240501 - 143420 - Control flow testing|Control flow testing]]