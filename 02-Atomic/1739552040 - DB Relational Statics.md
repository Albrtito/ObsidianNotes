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

# Relation:
The relations are based on [[Binary Relations]], with the following characteristics:

+ Each related element has a **domain**
+ A relation is the **cartesian product of n domains**

> f.e: Given the DNIs and Names sets: 
> + DNIs: Have a domain given by the properties they must follow.
> + Names: Have a domain given by their type (CHAR)
> A relation between the two of them would be: 
> $$DNI x NAME$$
> And encloses all possible tuples with some valid DNI and name in the domain: 
> $$ (DNI_i, NAME_j) $$
> 

+ Each of the elements/sets of the relation is called an attribute. 

> [!attention] Remark: 
> + All tuples must be unique. → Every row must be identifiable somehow


+ Relations can be swown implicitly(**intensive**), with a graph that defines the general foirm of it. Or explicitly(**extensive**) with all tuples that it contains. 

> [!NOTE] Relation degree: 
> Number of columns


> [!NOTE] Relation cardinality: 
> Number or rows / elements 








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


**Implicit semantics are those that can be derived form the model**
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