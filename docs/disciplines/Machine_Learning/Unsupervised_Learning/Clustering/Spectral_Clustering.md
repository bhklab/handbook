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

### Worked Example

This code snippet gives an example of how to run spectral clustering in python. We begin by importing the needed libraries:

```python
from sklearn.cluster import SpectralClustering
from scipy.stats import nbinom
import numpy as np

```

The next step involves simulating some data. We generate 10 samples each from 2 separate [negative binomial](https://en.wikipedia.org/wiki/Negative_binomial_distribution) distributions. The choice of negative binomial distribution is due to its [common use](https://bioconductor.org/packages/devel/bioc/vignettes/DESeq2/inst/doc/DESeq2.html) in modeling the raw counts of bulk RNA-seq. 

```python
seed = 1234 # seed to get reproducible behavior
n1, p1 = 10, 0.3
n2, p2 = 15, 0.5

g1 = nbinom.rvs(n1, p1, size = 50,random_state = seed).reshape(10,5) # simulated expression for distribution 1
g2 = nbinom.rvs(n2, p2, size = 50,random_state = seed).reshape(10,5) # simulated expression for distribution 2

```

Next we stack this data into a matrix and perform a pointwise $\log_2(x+0.001)$ transformation like those done on [ORCESTRA](https://orcestra.ca). We also follow the rule of thumb above and pick the number of neighbors as the natural log of the number of observations. Lastly, we write down the labels.

```python
X = np.log2(np.vstack((g1,g2))+0.001)
n_nbrs = int(np.ceil(np.log(X.shape[0])))+1 # add an offset to make the graph slightly more dense
true_labels = 10*[0]+10*[1]
```

```python
clustering_algo = SpectralClustering(n_clusters = 2,affinity = 'nearest_neighbors',n_neighbors=n_nbrs)
clustering_algo.fit(X)
```

After fitting we can access the predicted labels and compare them to the ground truth using the following:
```python
print(clustering_algo.labels_)
print(true_labels)
```
#### References
- <a id="1">[1]</a> 
Von Luxburg, Ulrike. "A tutorial on spectral clustering." Statistics and computing 17 (2007): 395-416.
