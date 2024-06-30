# Readme on Dimensionality Reduction Techniques

## Eigendecomposition
Eigendecomposition decomposes a square matrix \( A \) into eigenvalues and eigenvectors:
\[ A = V \Lambda V^{-1} \]
where \( V \) contains eigenvectors and \( \Lambda \) is a diagonal matrix of eigenvalues.

## Singular Value Decomposition (SVD)
SVD factors any \( m \times n \) matrix \( A \) into three matrices:
\[ A = U \Sigma V^T \]
where \( U \) and \( V \) are orthogonal matrices, and \( \Sigma \) is a diagonal matrix of singular values.

## Difference Between Eigendecomposition and SVD
- **Applicability**: Eigendecomposition is for square matrices; SVD is for any matrix.
- **Components**: Eigendecomposition uses eigenvalues/vectors; SVD uses singular values and orthogonal matrices.
- **Use Cases**: Eigendecomposition is for linear algebra properties; SVD is for dimensionality reduction and data compression.

## Dimensionality Reduction
Dimensionality reduction reduces the number of variables in data to:
- Simplify interpretation and visualization.
- Reduce noise and redundancy.
- Lower computational cost.
- Improve machine learning performance.

## Principal Components Analysis (PCA)
PCA is a linear technique that transforms data to new coordinates, maximizing variance along principal components, reducing dimensions while retaining most information.

## t-distributed Stochastic Neighbor Embedding (t-SNE)
t-SNE is a non-linear technique for visualizing high-dimensional data by minimizing divergence between high-dimensional and low-dimensional data representations.

## Manifold
A manifold is a space that locally resembles Euclidean space. In dimensionality reduction, manifolds help map high-dimensional data to lower dimensions while preserving data properties.

## Linear vs. Non-Linear Dimensionality Reduction
- **Linear**: Assumes data lies on a linear subspace. Examples: PCA, Linear Discriminant Analysis (LDA).
- **Non-Linear**: Captures non-linear data relationships. Examples: t-SNE, Isomap, Locally Linear Embedding (LLE).

## Techniques
- **Linear**: PCA, LDA
- **Non-Linear**: t-SNE, Isomap, LLE, Kernel PCA