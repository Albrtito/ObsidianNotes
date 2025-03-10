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

Bucket Extend:
Same as blocking factor but for buckets
$$
\mathrm{BE}=\left\lfloor\frac{\mathrm{BS}}{\mathrm{~S}_{\mathrm{r}}}\right\rfloor
$$


+ **Consecutive organization:** Every logical record sarts **inmmediately after the previous one**. 
	+ The size of a file is given in blocks
	+ For this type of organization, the blocking factor is used. 
+ **Non-Consecutive:** Every block starts at the beggining with a logical record. There can be some space at the end of the block. 
	+ Non consecutive organization can be done for different number of block groups. So the logical records are aligned to the beginning of each n blocks. This n blocks are called a bucket.
	+ It is advantageous to have buckets of $2^n$ blocks.
	+ The size of a file in a non-consecutive organization is of n buckets.
	+ For this type of organization the bucket extend is used.
	+ The size of a bucket is given by blocks, bytes, something like that
> **Oracle:** Only lets us have buckets of $2^1$ to $2^4$ blocks. 

## Buckets and extensions:
Buckets dont only have aviable and occupied space but also some data used for control and other operations. Because of this we’ll adapt the BE formula to include the other sections. 
$$
\mathbf{B E}=\left\lfloor\frac{\left(\mathbf{B S}-\mathbf{S}_{\mathrm{ctrl} \mathrm{inf}}\right) \cdot(1-d f s)}{\mathbf{S}_{\mathrm{rec}}}\right\rfloor
$$

Buckets also have some other parameters such as: 
+ **Maximum Occupation | extend:** Limit so that no record can be inserted
+ **Minimunm Occupation | space:** Threshold below which it’s reused for inserting. No data in it, we can put new data in. 

## Physical Design of the Logical record:

***