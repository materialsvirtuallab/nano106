LaTeX input:        mmd-mavrldoc-header
Title:              NANO106 Handout 9 - Einstein Notation
Author:             Shyue Ping Ong
Affiliation:        University of California, San Diego
Address:            9500 Gilman Drive, Mail Code 0448, La Jolla, CA 92093-0448
Web:                http://www.materialsvirtuallab.org
Base Header Level:  2
LaTeX Mode:         mavrldoc
LaTeX input:        mmd-mavrldoc-begin-doc
LaTeX footer:       mmd-mavrldoc-footer
xhtml header:       <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

# Introduction

The Einstein notation, or Einstein summation convention, is a convention that
implies summation over repeated indices. It allows us to write many
relationships in a more succinct manner. For the purposes of crystallography,
we will mainly be working with the range of indices over the set {1, 2, 3}. 
Therefore,

\\[
y = c_i a_i = \sum_{i=1}^3 c_i a_i = c_1 a_1 + c_2 a_2 + c_3 a_3
\\]

To illustrate the power of this notation, we will now write many expressions
in linear algebra in Einstein notation.

## Scalar or dot product of two column vectors

\\[
\mathbf{x} \cdot \mathbf{y} = x_i y_i
\\]

## Product of a matrix with column vector

\\[
\begin{aligned}
\mathbf{y} & = \mathbf{A} \mathbf{x}
& = \begin{pmatrix}a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33}\end{pmatrix} \begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}
\end{aligned}
\\]

In Einstein notation, this is written as:

\\[
y_i = a_{ij} x_j
\\]

It is important to note that non-repeated indices are "dummy" indices and have no
special meaning. Only *repeated indices on the same side of the equation* implies
summation.

## Product of row vector with matrix

\\[
\begin{aligned}
\mathbf{y}^T & = \mathbf{x}^T  \mathbf{A}\\
\begin{pmatrix}y_1 & y_2 & y_3\end{pmatrix} & = \begin{pmatrix}x_1 & x_2 & x_3\end{pmatrix} \begin{pmatrix}a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33}\end{pmatrix}
\end{aligned}
\\]

In Einstein notation, this is written as:

\\[
y_j = a_{ij} x_i
\\]

Be very careful about the indices! Note the difference in the order of the
indices in this expression compared to that of the product of the matrix with
a column vector.

# The Kronecker Delta and Permutation Symbol

To use the Einstein summation notation effectively, we need to introduce two
additional symbols. Note that this is really more for your information on
the power of this notation. We will be using the Kronecker Delta, but in this
course, we will not actually be using the permutation symbol. It is included
for completeness in case you see this in future.

* Kronecker Delta
    \\[
    \delta_{ij} = \begin{cases} 1, & \mbox{if } i=j\\ 0, & \mbox{if } i \ne j\end{cases}
    \\]
* Levi-Civita or Permutation symbol
    \\[
    \epsilon_{ijk} = \begin{cases} 0, & \mbox{for } i=j\mbox{, } j=k \mbox{ or } i=k \\ +1, & \mbox{for } (i,j,k) \in \{(1,2,3), (2,3,1), (3,1,2)\}\\-1, & \mbox{for } (i,j,k) \in \{(1,3,2), (2,1,3), (3,2,1)\}\end{cases}
    \\]

## Some useful relations

\\[
\begin{aligned}
\delta_{ij} \delta_{jk} & = \delta_{ik}\\
\delta_{ij} \epsilon_{ijk} & = 0\\
\epsilon_{ipq} \epsilon_{jpq} & = 2 \delta_{ij}\\
\epsilon_{ijk} \epsilon_{ijk} & = 6\\
\epsilon_{ijk} \epsilon_{pqk} & = \delta_{ip}\delta_{jq} -\delta_{iq}\delta_{jp}
\end{aligned}
\\]

# Cross-product in Einstein notation

If $\mathbf{e_1}$, $\mathbf{e_2}$, and $\mathbf{e_3}$ are the Cartesian unit 
vectors, the cross product of two vectors can be written in Einstein notation as:

\\[
\mathbf{a} \times \mathbf{b} = \epsilon_{ijk} a_i b_j \mathbf{e_k}
\\]

# Proof of triple product using Einstein notation

We can derive a formula for the triple product in Einstein notation as follows:

\\[
\begin{aligned}
\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) & = a_i \mathbf{e_i} \cdot \epsilon_{jkm} b_j c_k \mathbf{e_m}\\
& = \epsilon_{jkm} a_i b_j c_k \mathbf{e_i} \cdot \mathbf{e_m}\\
& = \epsilon_{jkm} a_i b_j c_k \delta_{im}\\
& = \epsilon_{jki} a_i b_j c_k\\
& = \epsilon_{ijk} a_i b_j c_k\\
\end{aligned}
\\]

# Using Einstein notation in tensor properties

Tensors are geometric objects that describe linear relations between vectors,
scalars, and other tensors. We will be using Einstein notation extensively to
work with tensors.

* Rank-0 tensor: Scalar, e.g., temperature
* Rank-1 tensor: Vector, e.g., pyroelectricity ($p_i$)
* Rank-2 tensor: Matrix, e.g., diffusivity ($D_{ij}$)
* Rank>3 tensor: Tensor, e.g., piezoelectric coefficient ($d_{ijk}$), elastic constants ($c_{ijkl}$)

Some examples of denoting relationships using Einstein notation.

* Relationship between diffusion flux and concentration gradient
    \\[
    J_{i} = D_{ij} \nabla \phi_{j}
    \\]
* Relationship between stress and strain
    \\[
    \sigma_{ij} = c_{ijkl} \varepsilon_{kl}
    \\]

# Transformation of Tensors

If we denote $\mathbf{A}$ as the direction cosine matrix relating one set of 
Cartesian axes to another, i.e.,

\\[
\begin{pmatrix}\mathbf{e_1'}\\ \mathbf{e_2'} \\ \mathbf{e_3'}\end{pmatrix} = \mathbf{A} \begin{pmatrix}\mathbf{e_1}\\ \mathbf{e_2} \\ \mathbf{e_3}\end{pmatrix}  \mbox{ where } \mathbf{A} = \begin{pmatrix}a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33}\end{pmatrix}
\\]

or

\\[
\begin{aligned}
\mathbf{e_i'} & = a_{ij} \mathbf{e_j}\\
\mathbf{e_i} & = a_{ji} \mathbf{e_j'}
\end{aligned}
\\]

The transformation of a tensor $r$ under the change in axes is given by:

\\[
r_{ijk\ldots}' = a_{iI} a_{jJ} a_{kK} \ldots r_{IJK\ldots}
\\]

Note that the capital letters on the RHS are repeated indices and hence represents
summation. For a rank-2 tensor, the concise notation summarizes  $9 \times 9 = 81$ 
terms. For a rank-3 tensor, there are 729 terms,  and for rank-4, there are 6561 
terms!
