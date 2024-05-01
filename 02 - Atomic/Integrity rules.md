---
tags:
  - FilesAndDB
---
Referential integrity rules are used to keep and maintain the [[Referential Integrity]]

This five rules state what to do when an association is going to be deleted or updated.

1. **Restrict:** (DR/UR)
	Any operations on relations with some association (child) is prevented
2. **No Action** (DNA/UNA)
	If the operation breaks referential integrity, then it is not done. 
3. **Cascade: (propagation)** (DC/UC)
	The operation is extended to all associated relations. So that they are also deleted or updated. 
4. **Set Null:** DSN/USN
	The old or not valid association values will be substituted by null. 
5. **Set Default**: DSD/USD
**REMAKR:** We'll be mainly using no action and cascade

**REMARK:** If nothing is said, the basic setup for integrity rules is: 
+ **Delete no action:** DNA
+ **Update Cascade:** UC