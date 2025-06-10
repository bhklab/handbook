# Spectral Clustering

Spectral clustering is a graph-theoretic method used for clustering data points. The paper [[1]](#1). 

There are many versions of this algorithm which leverage different graph *Laplacians* derived from *similarity scores*. Thus Spectral Clustering will work on **any** collection of objects $\{x_1,\dots, x_n\}$ as long as one can compute similarity scores $s_{ij}\geq 0$ for all pairs of points. 


The basic sketch for the algorithm is:
1. Construct a weighted graph adjacency matrix $W$ from $s_{ij}$. Construct a Laplacian $L$ (normalized, regular, random walk, etc.) from $W$. 
2.  Compute first $R$ eigenvectors of $L$, call them $u_1, \dots, u_R$ 
3. Construct the $n\times R$ matrix $U=\left[u_1, u_2, \dots, u_R\right]$ 
4 . Use [K-means](./K_Means.md) or other clustering algorithms to cluster the rows and return the clusters. This requires tuning the number of clusters $k$ 


Different flavors and interpretations of the algorithms can be given, depending on the Laplacian used. 

### Rules of Thumb

The general rule of thumb is to use a $k$ nearest neighbor graph with $k$ tuned to make the graph connected. For large graphs try $k\approx \mathcal{O}(\log(n))$, else try it manually. 



#### References
- <a id="1">[1]</a> 
Von Luxburg, Ulrike. "A tutorial on spectral clustering." Statistics and computing 17 (2007): 395-416.
