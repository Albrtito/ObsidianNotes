---
tags:
  - FilesAndDB
---
Creating assertions has the following syntax.
```sql
CREATE ASSERTION <name> CHECK <conditional_expression>  ;
```
#### Example: 
```sql
CREATE ASSERTION monthly_wage_DB_admin CHECK NOT EXIST (SELECT 'X' FROM EMPLOYEES A JOIN DEPARTMENT B ON (A.dep=B.cod_dep) WHERE B.position='DB Admin' and A.wage<8000);
```