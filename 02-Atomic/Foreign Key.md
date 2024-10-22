---
tags:
  - FilesAndDB
---
Foreign keys are a way of referencing an attribute or a set of attribute that belong to another relation.  This is called an **association**
Because the DB needs to maintain [Referential Integrity](Referential%20Integrity.md), the only values that can be stored in a foreign key attribute are: 
+ Existent values that there are in the referenced attribute
+ Null values


### For multi-attribute keys: 
Multi attribute keys can have a match in only some of the attributes provided, three cases are separated based on the possibilities: 
+ Complete match: all attributes are null or none are
+ Partial: non-null part must exist (one row min)
### Creating foreign keys with table creation: 
Foreign keys are defined as constrains in the table in the following way: 
```sql
constraint fk_key_name Foreign key(attribute_name) References  referenced_table(referenced_key));
```
+ On the `attribute_name` entry is the name of the current table's attribute that will be the foreign key
This is done on the [Creating and deleting Tables](Creating%20and%20deleting%20Tables.md) fase. 
