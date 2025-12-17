# Principal Component Analysis (PCA)

### Intuition

The rough idea behind PCA is to find the **directions** in which the data varies. The PCA algorithm proceeds iteratively, beginning by finding the direction in which the data set "points most." The algorithm then finds the direction that is *orthogonal* (that is, perpendicular) to the first direction and captures the most variation, and so on. Recall that two vectors $x,y$ are orthogonal if $x^Ty=0$ and we write this as $x\perp y$.


### Details 

Suppose we have a collection of $n$ observations in $\mathbb{R}^d$, that is we have $x_1, \dots, x_n$ where $x_i\in \mathbb{R}^d$. Since we are looking for **directions** we only focus on vectors $v$ with unit norm: 

$||v||_2 = \sqrt{\sum_i v_i^2} = 1$

Suppose we have such a $v$. We can then compute how much each $x_i$ points in the direction of $v$ by computing $\tilde{x}_i=x_i^Tv$. We can do this for all of our data points to get a collection of $n$ *real numbers* $\{\tilde{x}_1, \dots, \tilde{x}_n\}$. To compute how much the data varies in the direction $v$ we can just compute the variance of this set of real numbers, that is we compute Var$(\tilde{x}_1, \dots, \tilde{x}_n)$. 

Now that we have a way to compute how much the data varies in a given direction, we need to find the optimal directions as outlined at the top of this page. PCA computes:


$$
u_1 = \underset{v\in \mathbb{R}^d, ||v||_2=1}{\text{argmax}}\text{Var}(x_1^Tv, \dots, x_n^Tv)\\
u_2 = \underset{v\in \mathbb{R}^d, ||v||_2=1, v\perp u_1}{\text{argmax}}\text{Var}(x_1^Tv, \dots, x_n^Tv)\\
u_3 = \underset{v\in \mathbb{R}^d, ||v||_2=1, v\perp u_1, v\perp u_2}{\text{argmax}}\text{Var}(x_1^Tv, \dots, x_n^Tv)\\
\vdots \\
u_d = \underset{v\in \mathbb{R}^d, ||v||_2=1, v\perp u_1, \dots, u_{d-1}}{\text{argmax}}\text{Var}(x_1^Tv, \dots, x_n^Tv)\\
$$



Note that $u_1, \dots, u_d$ are $d$ orthogonal vectors with unit length in $\mathbb{R}^d$, and thus form an [orthonormal basis](https://en.wikipedia.org/wiki/Orthonormal_basis). 

But how *do* we compute these vectors? The answer comes via matrix algebra, in particular we use the [singular value decomposition (SVD)](https://en.wikipedia.org/wiki/Singular_value_decomposition) to find the directions (which will be the singular vectors) and the amounts of variation (the singular values). To keep this page relatively self-contained we recall a few facts about the SVD.

**SVD Reminders**

- The SVD is a *decomposition* of a matrix. Meaning it re-writes a matrix $M\in\mathbb{R}^{n\times d}$ as a product of other matrices. 
- The SVD rewrites $M$ as the product of three matrices, $U, \Sigma, W$. Explicitly we have
$$
M=U\Sigma W^T
$$ 
- $U\in \mathbb{R}^{n \times n}$ where the columns are unit vectors that are orthogonal. The columns of $U$ are called the **right singular vectors**.
- $\Sigma\in \mathbb{R}^{n\times d}$ and is diagonal with non-negative real numbers along the diagonal. The diagonal entries are called the **singular values**. We assume that the columns of $\Sigma$ are listed in decreasing order of the singular values. These are written as $\sigma_i$. 
- $W\in \mathbb{R}^{d\times d}$ where the the columns are unit vectors that are orthogonal. The columns are called the **right** singular vectors. 

## The PCA Procedure

The full PCA procedure is as follows. 


1. Compute the mean of the data $\bar{x}=\frac{1}{n}\sum_{i}x_i$
2. Center the data, that is subtract $\bar{x}$ from each data point to create a new collection $a_i=x_i-\bar{x}$
3. Stack the $a_i$ into a matrix $A = \begin{bmatrix}a_1 \\ a_2 \\ \vdots \\ a_n\end{bmatrix}\in\mathbb{R}^{n\times d}$
4. Compute the SVD of the matrix $A$, that is $A=U\Sigma W^T$. 



???+ warning
	Centering the data is **required** for PCA to succeed. If you do fail to do this the first principal component will be just the mean and thus, a waste of computation. 

???+ tip
	It is wise to make sure that your data is, roughly, on the same scale. This is due to the construction of PCA. Suppose one of the dimensions contains values around 100 and the other features are in between 0 and 1. Then the dot product will be distorted by that dimension even if the variation in one of the other dimensions is larger. 

### Dimensionality Reduction

So far we've only just computed an SVD which hasn't actually reduced the dimensionality. Note that each column $w_j$ of $W$ is in $\mathbb{R}^d$ and so we can compute $a_i^Tw_j$ for all data points. Doing this for all the $w_j$ could be written as the matrix product $AW$. However, doing this doesn't change the dimension, as this is a product of an $n\times d$ matrices and a $d\times d$ matrix. 

The way to reduce dimensionality is to only pick a subset of the $w_j$. Suppose we pick the first $L$ columns of $W$, write this $W_L$, then $AW_L\in \mathbb{R}^{n\times L}$ which *is* dimensionally reduced.  The question then is how to choose $L$. There are two methods:

1. Since the singular values are assumed to be listed in decreasing order, we can choose the first $L$ columns to pick the largest one where $L$ is a user-determined design point. 
2. The second method aims to capture a percentage of the variance. Specifically let $B$ be the sum of the singular values and suppose we want to capture $p$ percentage of the variance. Pick $L$ such that: $\frac{\sum_{i=1}^L\sigma_i}{B}\geq p$


**Mathematical Note**

Looking at the SVD again we can note that $AW=U\Sigma W^TW = U\Sigma$ and so the principal components are the left singular vectors and the principal values the corresponding singular values. 

### Worked Example

First we generate some data. We perform a simulation that generates data that should look a little like gene expression data in log-transformed [transcripts per million (TPM)](https://www.rna-seqblog.com/rpkm-fpkm-and-tpm-clearly-explained/).

```python
from sklearn.decomposition import PCA
from scipy.stats import nbinom
import numpy as np

seed = 1234 # seed to get reproducible behavior
n1, p1 = 10, 0.3
n2, p2 = 15, 0.5

g1 = nbinom.rvs(n1, p1, size = 50,random_state = seed).reshape(10,5) # simulated expression for distribution 1
g2 = nbinom.rvs(n2, p2, size = 50,random_state = seed).reshape(10,5) # simulated expression for distribution 2


X = np.log2(np.vstack((g1,g2))+0.001)
```

The centering of `X` can be done manually or using `scikit-learn` built in functionality. The latter is recommended but we give both for completeness.
```python
# manual
X = X-np.mean(X,axis=0,keepdims=True)

# scikit-learn
from sklearn.preprocessing import StandardScaler
sclr = StandardScaler(with_std=False) # only want to center, not scale in this instance. 
X = sclr.fit_transform(X)
```

To see how to get explained variance, let's try with the maximum number of principle components which is the dimensionality of the data, which in this instance is 5. 
```python
dim_red = PCA(n_components=5)
dim_red.fit(X)
```

Luckily `sciki-learn` has functions for immediately giving percentage of variance. Suppose we want to explain 70% of the variance.  The following block will find the minimum number of principal components to compute to above this value. If the data was much higher dimension, say over 500 features, this approach will be **slow** and it is better to start with a guess at number of principal components needed. 

```python

explain_variance = dim_red.explained_variance_ratio_
cumulative_explained_variance = np.cumsum(dim_red.explained_variance_ratio_)
tol = 0.7
locations_above_tol = [k for k in range(len(cumulative_explained_variance)) if cumulative_explained_variance[k]>=tol]
nc = min(locations_above_tol)+1 # add 1 because python uses 0 indexing. 
```

Now that we have the minimum required number of components, we can compute the PCA and reduce down to desired number of dimensions.:
```python
dim_red = PCA(n_components=nc)
dim_red.fit(X)
X_reduced = dim_red.transform(X)

print(X.shape) # (20,5)
print(X_reduced.shape) #(20,2)
```
