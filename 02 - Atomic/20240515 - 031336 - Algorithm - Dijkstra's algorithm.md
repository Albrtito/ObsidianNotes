---
aliases:
  - Algorithm - Dijkstra's algorithm
  - Dijkstra's algorithm
tags:
  - Discrete
  - incomplete
"References:": 
cssclasses:
---
# Dijkstra’s algorithm
Dijkstra’s algorithm is used to **find the shortest path that joins an initial vertex s to a final vertex t** given the following conditions: 
+ The graph must be simple
+ The graph must be connected and weighted such as **all weights are positive**
$$
G = (V,E,w): (w_e >0 , \forall e\in E)
$$
The basic idea is to assign to each vertex j two labels that might be temporary or permanent, these labels are $\left(\delta_j, P_j\right)$
+ $\delta_j$ : Estimate of the length of the path from initial vertex($v_o$) to j
+ $P_j$ : Is an estimate of the **predecesor** of the vertex j along the above path. (the previous vertex we’re coming from to reach j)

## Algorithm
Get the initial and final vertex
1. Mark the origin(initial vertex) with the permanent label (0,s)
	All other vertices are marked with one of two possible labels: 
	+ If the vertex is adjacent to the initial vertex it gets the label: $(w_{s,j},s)$ , where $w_{s,j}$ is the weight of the edge joining the vertices. 
	+ If the vertex is not adjacent then it just gets an infinity label.
2. Let $v \in V$ be the last vertex that has become permanent. For each temporary vertex j we compare the temporary label $\delta_j$ to the new value $\delta_v + w_{v,j}$
3. …


