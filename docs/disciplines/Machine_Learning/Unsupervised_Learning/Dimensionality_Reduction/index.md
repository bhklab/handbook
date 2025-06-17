# Introduction

In general we assume we have a dataset $X$ which consists of $n$ observations in $\mathbb{R}^d$. The dimensionality of the dataset is $d$. 


Dimensionality reduction is often used as pre-processing step for subsequent analyses, included [clustering](../Clustering/index.md), [supervised learning](../../Supervised_Learning/index.md), or visualization. Common techniques for dimensionality reduction include:

- **[Principal Component Analysis (PCA)](./PCA.md)** 
- **[Random Projections](./Random_Projections.md)**
- **[t-distributed Stochastic Neighbor Embeding (t-SNE)](./tsne.md)**
- **[Uniform Manifold Approximation and Projection (UMAP)](./UMAP.md)**
- **[Locally Linear Embeddings (LLE)](./Locally_Linear_Embeddings.md)**
- **[Laplacian Eigenmaps](./Laplacian_Eigenmaps)**


Dimensionality reduction is needed due to a phenomenon known as the *curse of dimensionality*, which states that there is a pessimism-inducing relationship between the dimension of your data. Most dimensionality reduction techniques are based on something called the [manifold hypothesis](https://en.wikipedia.org/wiki/Manifold_hypothesis), which assumes that the data, while living in some high dimensional space, are actually on some much lower dimensional surface. 




## The Curse of Dimensionality

The [curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality) (CoD), roughly speaking, states that as $d$ grows, the number of samples $n$ needed to be able to develop a good statical model increases exponentially on the order of $2^d$. For context, $2^265$ is roughly the number of atoms in the universe and, by modern standards, 265 is relatively small dimension. In pharmacogenomics we often work with datasets where $d\approx 1000$ *after* dimensionality reduction! 


It might be helpful to understand a bit of the *why* behind the CoD. Suppose we  start with $d=1$ and have data that consists of $\{-1,+1\}$ chosen uniformly at random (probability of $\frac{1}{2}$). How many samples would we need to draw in order to get a representative data set? On average, we'd expect the answer to be 2. 


Suppose we now set $d=2$ and consider a similar set up where the data is sampled uniformly at random from the four corners of the square $\{(+1,+1), (+1,-1), (-1,-1),(-1,+1)\}$. Similar reasoning suggests that we need 4 samples, average, to get a data set that overs the sampling domain (i.e. each point is represented at least once). 

If $d=3$ we then have a [hypercube](https://en.wikipedia.org/wiki/Hypercube) with 8 points for each possible combination of $(\pm1, \pm 1, \pm1)$, which suggests we need $8$ samples to get coverage. 

At each step the number of samples needed to cover the data set domain is approximately $2^d$ and this holds in all dimensions. 



## The Manifold Hypothesis

While the curse of dimensionlity paints a bleak picture, the [manifold hypothesis](https://en.wikipedia.org/wiki/Manifold_hypothesis) offers some help. The manifold hypothesis supposes that the observations $x_i\in \mathbb{R}^d$ live on some **unknown** lower-dimensional surface (a *manifold*).

As a visual example, suppose you have a bunch of points in $\mathbb{R}^3$. After some data analysis you discover that they all have the same Euclidean norm, which means they lie on a *sphere,* a two-dimensional surface that lies in a three-dimensional space. 

In a higher dimension, if you have data consisting of vectors $x_i\in\mathbb{R}^d$ but discover that there a vector $w\in \mathbb{R}^d$ such that $w^Tx_i=0$ for all $i$, then the data actually lie on a hyperplane, which must be of smaller dimension. Even simpler, if each $x_i$ is a multiple of some given vector, $\tilde{x}$, that is $x_i=c_i\tilde{x}$ then all the data points lie on a line, which is one-dimensional. 


The dimensionality reduction methods listed at the top of the page differ, in part, in the nature of the manifold they assume and how they try to approximate/learn it. 
