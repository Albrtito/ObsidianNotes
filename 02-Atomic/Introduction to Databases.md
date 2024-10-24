---
Date: 2024-02-25
tags:
  - FilesAndDB
"References:":
---
**Properties of storage:** 
+ Perdurability: For how long can be stored
+ Capacity: how much can be stored
+ speed: How fast can be accessed
+ range: From how far can be accessed
+ access type: ??
**Storage types, properties:**
 + Structured, non-structured, semi-structured
 **Scopes:**
 + **Logical or external**: Search, edit, add, retrieve, erase. **need effectiveness** : The first part of the course will focus on this logical scope (60%)
 + **Physical or internal scope**: read, write, locate **need efficiency**: The second part of the course will focus on this other part. 40%
	+ The key is to have some organisation so that the locate operation is not so costly:
		+ (binary search with a log n complexity)
		+ Hash organisation, direct key to where the element is (a dictionary) : But wastes a lot of space
		+ Indexed organisation: Pointed elements
### ANSI/SPARC Architecture:
Division of the architecture framing the databases structures through three levels. 
**Internal level:** Internal schema is what describes it, it's the physically stored part of the data. **data-devices** : for administrators
**Conceptual level:** Global view of the data structures, **conceptual schema**. **data - data** : for designers
**External level:** focused on users, view of the database. **External schema**. **data - users** : for users.

### Data model: 
Creation of the data model is what describes the associations and structure of the data. This is what translates into the [Relational Model](Relational%20Model.md)
in the relational databases. 
Data models have the static model: **Objects, associations and restrictions** 
And the dynamic model: **Things that change over time**
Aside from the data model type there are always **restrictions, constrains** that ensure that the data has the correct values. This constrains can be: 
+ **Inherent** when created on the model structure
+ **Semantic:** imposed on the data 
## OLTP (On-Line Transaction Processing)
Based on interactivity and on-line batching, this online processing and connection to a database called **transactions** needs to have some characteristics. 
+ **Atomicity** any operation must be or completed or not done
+ **Consistence** the integrity is a really important part in a DB. When speaking about it in relational databases we talk about the [Referential Integrity](Referential%20Integrity.md)
+ **Isolation** operations must be independent
+ **Durability** once committed , the transaction effect is permanent.
## OLAP: (On-Line Analytic Processing)
The next thing that appears is big data and managing efficiently the searches ,etc. This creates the analytic processing. 
There are types of analytic processing: **ROLAP, MOLAP, HOLAP, WOLAP...** during this course we'll be talking and looking at [ROLAP](ROLAP)
databases (relational databases) and MOLAP databases. 



---
### Summary
Highlight ==what’s important!==
