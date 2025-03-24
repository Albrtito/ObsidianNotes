---
aliases:
  - DB Relational Statics
tags:
  - FilesAndDB
References: 
cssclasses:
---
# DB Relational Statics

> [!NOTE] Intro: 
> The static part of the Relational Model creates the tables, relations between them, what to do when something related changes and static constraints. 

This note will define the concepts and rules needed to create a **theoretical model**.


> [!example] Naming convention: 
> + **attribute:** A set of the relation
> 	+ **key:** Same thing as an attribute
> + **domain:** All possible values that an attribute can take
> + **relation:** The cartesian product of n attributes 
> + **relation degree:** The number of attributes it has
> + **relation cardinality:** Number of unique tuples in the relation
> + **individual:** An specific tuple of the relation
>

## Relation:
The relations are based on [[Binary Relations]], with the following characteristics:

+ Each related element has a **domain**
+ A relation is the **cartesian product of n domains**
+ Each related element is called an **attribute**
+ Each set of related elements is called a **tuple**

> f.e: Given the DNIs and Names sets: 
> + DNIs: Have a domain given by the properties they must follow.
> + Names: Have a domain given by their type (CHAR)
> A relation between the two of them would be: 
> $$DNI x NAME$$
> And encloses all possible tuples with some valid DNI and name in the domain: 
> $$ (DNI_i, NAME_j) $$
> 

+ Relations can be swown implicitly(**intensive**), with a graph that defines the general form of it. Or explicitly(**extensive**) with all tuples that it contains. 

> [!NOTE] Relation degree: 
> Number of columns


> [!NOTE] Relation cardinality: 
> Number or rows / elements 

### Inherent restrictions:
These are restrictions that **come with the relational nature of this theoretical model.**
1. The order of attributes does not matter
2. The order of tuples does not matter
3. There are **no two identical tuples**
4. Individuals(tuples) are of the same nature.
	* They share the same attribute number (arity)
   + Attributes are single-value and atomic
	   + Single-value: One domain
	   + Atomic: Non-divisible for their aim. #Duda: An example of this and why it is a defined property?

We can also define those **restrictions required for the integrity of the model**:
1. **Integrity of entity:** Each row is unique
	1. No attribute from primary key can take null value
2. **Referential Integrity:** Anything referenced allways exists. So all Foreign Keys mus reference something that exists. 
	1. If it’s null. The reference check is skipped. 
	2. For several attributes. The check can be done in one of the following ways.
	   + **COMPLETE:** All attributes work as one
	   + **PARTIAL:** No check for null part
	   + **WEAK:** If there is a null value, no check. #Duda Does this also mean that if an attribute is not there it is seen as null?
	

### Relation to a relation:

> [!NOTE] Intro: 
> An attribute of a relation can be the same attribute of another relation. Instead of having them separately, a conection between the relations can be created:

> $R_1$ : VxU 
> $R_2$ : VxW → V is related to $R_1$ 

However, in order to create this relations the shared attribute must be **unique** in one of the two tables. That table pasa a ser la tabla “padre” mientras que la otra será la tabla “hija”


### Naming special keys:
+ Attributes that **can take null** → Use *
+ **Foreign keys** → <u>Underlined</u> and with an arrow to the referenced key
	+ Same number of keys as the PK of the referenced relation, see referential integrity with [[#Inherent restrictions]] in order to see how this is checked.




---
## Tables: 
The tables that are specified in the model must have a name and some attributes of the table. 
+ **The table name must be in singular**: f.e. The table containing all the courses will be called course
### The identifying keys. 
+ **key:** Set of attributes with a given function 
+ **superkey:** key able of identifying univocally each tuple ( so that at most is one tuple per key)
+ **candidate key**: Minimal superkey
+ **primary key**: Privileged candidate key. (underlined)
+ **secondary key**: (or alternative), the other candidate keys, could be privileged or not. (underlined discontinuously)
### Association: 
Linking keys is the way of logically pointing what tuples reference each other. For it we use the primary and foreign keys. The  key(any key) is the one that needs to be referenced. This way foreign keys reference primary keys. 
The representation of this associations is stated below. 
#### Taxonomy of links: 
Ask for both of the relations. How many of class1 can take class2? This gives the answer to whether the link is: 
+ 1 to 1
+ 1 to n: One is the parent of the other one
+ n to n: This can't really happen as both would be child classes. We need an intermediary that has a 1 to n relation with both of them and both primary keys in the middle. 
	+ Try to avoid these
	+ create a junction table or [bridging table](bridging%20table.md) to solve this issue
	


### Representation: 
+ The primary key is underlined
+ Optional attributes are marked with an asterisk (*)
+ Candidate keys are underlined.
+ If two attributes are underlined it could means things such as: 
	+ Both need to have the same value 
	+ 
**Associations:**
Associations are represented with a directed arrow departing from the foreign key and pointing to the referenced key: This way the parent would be the referenced key and the child the foreign key. (This is where [Referential Integrity](Referential%20Integrity.md) appears so that if the referenced key is deleted what do we do?)
+ If the referenced key is the primary one: The arrow can be pointing at the whole relation. 
#### Semantic coverage: 
This part is really the worst part of computer science, the client. The way to go with this is to **SEPARE ALL THE STATEMENT IN IMPLICIT AND EXPLICIT CONSTRAINTS FROM THE START**
This is really important as it really explains you what is a possible thing to do and what is just not realistically.

**Explicit semantic assumption:**
The directly derived information from the client

**Implicit semantics are those that can be derived from the model**
(the semantics u had in mind but where not told during the statement)
+ Attributes added that where not explicitly mentioned in the text are required to appear here
+ Anything that does not directly appear in the text goes here

**Non-Observed Explicit semantics are those that need to be explained to be understood as a feature and not an error**
(they told you to do something but it could not be done)


+ Writing why the creation of some tables if it wasn't explicitly specified
+ Writing what does it mean things that could be misunderstood
+ Why is something optional or why could it be null? 
+ Constrains that must be checked.

***