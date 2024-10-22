---
tags:
  - FilesAndDB
---
 The semantic restrictions consist in checking a conditional expression before actually giving a value to an attribute in a relation. 
 
 There are two types: 
 
 **Simple:** The **implementation is where the restriction is set**, only  applied on **one relational element**
 + With respect to [MySQL](MySQL.md) language the simple semantic restriction is applied when [Creating and deleting Tables](Creating%20and%20deleting%20Tables.md).

**Assertion:** A **general restriction** imposed in the whole DB. 
+ It concerns several relational elements.
+ Run after every actualisation 
+ **HIGH COST**
+ **ALMOST EVERY ONE IMPLEMENTS THEM**
