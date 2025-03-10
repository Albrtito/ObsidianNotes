---
aliases:
  - File structures
tags:
  - FilesAndDB
References: 
cssclasses:
---
# File structures


> [!example] Dictionary: 
> + **Expanded record:** When the logical record is larger than one block
> + **Blocking:** When the block is larger than the record. 
>   > One block may have several records
> + **Blocking factor:** How many logical records fit in a row. 
>

> [!NOTE] Title
> Files are **block sequences**, which are byte sequences. 
> When an user whants to operate on a byte the FMS looks for the block that contains that byte and then performs that operation in the required byte. 
> * This means that we allways need the block to operate. 

## Saving records: 
THe blocking factor is obtained by:
$$
f_b = \frac{S_{bk}}{Sr}
$$
+ $S_{bk}$: Size of the block
+ $S_r$ : Size of the record 

Based on this factor organization can be of two types: 
+ **Consecutive organization:** Every logical record sarts **inmmediately after the previous one**. 
+ **Non-Consecutive:** Every block starts at the beggining with a logical record. There can be some space at the end of the block. 
	+ Non consecutive organization can be done for different number of block groups. So the logical records are aligned to the beginning of each n blocks. This n blocks are called a bucket.
	+ It is advantageous to have buckets of $2^n$ blocks. Being n the 
***