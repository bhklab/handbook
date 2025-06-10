# K-Means Clustering

The idea behind k-means clustering is to choose a number of clusters, $k$, and centroids for the clusters, and then iteratively refine the cluster assignments and centroids until a number of iterations is reached or the cluster assignments don't change. Detailed mathematical developments can be found in [[1]](#1). 


Specifically given a dataset of points $\mathcal{D}= \{x_1, \dots, x_n\}$ where $x_i\in\mathbb{R}^n$ and an integer parameter $k\geq2$ we pick $k$ random vectors $c_1, \dots, c_k\in \mathbb{R}^d$ which serve as *candidate centroids* and iteratively perform the following steps:

- **E Step** This step updates the cluster assignments.
- **M Step** This step updates the centroids. 


Adopting the convention that $d(x_j, c_k) = ||x_j-c_k||_2^2$ and letting $C(j)\in\{1,\dots, k\}$  denote the cluster assignment of data point $x_j$, adding up over all of the clusters we penalize a given assignment $C$ via the following objective function:

$$
J = \sum_{k}\sum_{j:C(k)=k} = \sum_{j=1}^N\sum_{\ell=1}^k||x_j-c_\ell||A_{j\ell}
$$ 

where $A_{j\ell}$ is an indicator (0/1 variable) indicating if observation $j$ assigned to cluster $l$. Concretely $A_{j\ell} = 1$ if $C(j)=\ell$ and is 0 otherwise. 

Looking at the objective function we can see that it separates over clusters, thus for **fixed** clusters we can minimize $J$ by assigning each $x_j$ to its closest centroid. Using this insight the algorithm fixes clusters and penalizes them, and then updates the centroids by computing the means. 

Thus the algorithm to minimize $J$ proceeds in two rounds:

1) **E step** This step is done first and assigns clusters according to which closest 
$$
C(j)=\underset{r=1,\dots, k}{\text{argmin }} d(x_j,c_r)^2
$$

2) **M step** We update the centroids by computing the average of points in each cluster:
$$
c_\ell =\frac{\sum_{j=1}^n A_{jl}x_j}{N_\ell}
$$
where $N_\ell = \sum_{j=1}^nA_{j\ell}$, that is, the number of points in the $\ell$'th cluster. 


The $M$ step is derived by taken the gradient of $J$ with respect to each centroid,  $\nabla_{c_k}J$,  and setting it to zero. According to [[1]](#1) the algorithm is guaranteed to converge but not to a global minimum. 

$K$-means works as long as the metric $d$ is differentiable with respect to $c_k$.  That is if we replace $||x_j-c_\ell||^2$ with *any* differentiable $d(x_j, c_\ell)$ we can still use $k$ means. Of particular interest is the case where the metric as an inner-product norm derived from a positive definite matrix $M$, that is:
$$
d(x_j,c_\ell) = (x_j-c_\ell)^TM(x_j-c_\ell)
$$ as in the case of metric learning (see [[2]](#2) for inner product norms and [[3]](#3) for metric learning). 



#### References
- <a id="1">[1]</a>
Bishop, Christopher M. Pattern recognition and machine learning. Vol. 4. No. 4. New York: springer, 2006.

- <a id="2">[2]</a>
Lax, Peter D. Linear Algebra and Its Applications, 2nd Edition

- <a id="3">[3]</a>
Bellet, Aurélien, Amaury Habrard, and Marc Sebban. Metric learning. Morgan & Claypool Publishers, 2015.

