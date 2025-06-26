# Introduction

Unsupervised Learning (UL) is a branch of machine learning where the inputs are not labeled. Generally speaking, the goal of UL is to find some sort of "hidden" (sometimes called "latent") structure in the dataset. 

The two most common tasks in UL are [dimensionality reduction](./Dimensionality_Reduction/index.md) and [clustering](./Clustering/index.md). Parts of the field known as [generative modeling](./Generative_Modeling/index.md) also fit under the umbrella of unspervised learning. 


- **[Dimensionality Reduction](./Dimensionality_Reduction/index.md)** consists of techniques to, as the name suggests, reduce the dimension of the data. Concretely, suppose your data consists of vectors that are in $\mathbb{R}^d$. Dimensionality reduction procedures will, for each data point $x_i\in\mathbb{R}^d$ in your dataset, create a corresponding vector $\tilde{x}_i\in \mathbb{R}^k$ where $k$ is **much** smaller than $d$. 


- **[Clustering](./Clustering/index.md)** consists of methods to partition the data into subgroups that are disjoint (i.e., do not overlap). After clustering has been performed the discovered groups can be analyzed and compared.


- **[Generative Modeling](./Generative_Modeling/index.md)** is a subfield of machine learning that aims to learn the probability distribution that generated the dataset. This can be useful for trying to generate synthetic examples of data. In addition some techniques for generative modeling, such as [variational autoencoders](./Generative_Modeling/VAE.md) (VAEs), can also be used for dimensionality reduction. 