---
Date: 2024-02-22
tags:
  - FilesAndDB
"References:":
---
The referencial integrity of a text is the integrity and cohesion of it's associations between relations, if a table disappears or changes, other tables that use this one as a reference need to know what to do and how to act. 
When designing the structure of the DB here are five rules. 
+ Create some [Integrity rules](Integrity%20rules.md) to structure delete and update operations

**For Delete and update**
1. **Restrict**
2. **No action**(DNA/UNA): If by the end of the operation there's any problem, rollback
3. **Cascade**
5. **Set Null**
6. **Set Default**

+ NO ACTION AND CASCADE ARE THE MAIN TWO USED