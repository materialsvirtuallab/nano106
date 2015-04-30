LaTeX input:        mmd-mavrldoc-header
Title:              NANO106 Handout 8 - Einstein Notation
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

This document provides a summary of the Einstein notation.

# General Principle

The Einstein notation, or Einstein summation convention, is a convetion that implies
summation over repeated indices. It allows us to write many relationships in a much
more succinct manner. For the purposes of crystallography, we will mainly be working
with the range of indices over the set {1, 2, 3}. Therefore,

\\[
y = c_i a_i = \sum_{i=1}^3 c_i a_i = c_1 a_1 + c_2 a_2 + c_3 a_3
\\]

To illustrate the power of this notation, we will now write many expressions in 
linear algebra in Einstein notation.

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
special meaning. Only *repeated* indices on the same side of the equation implies
summation.

## Product of row vector with matrix

\\[
\begin{aligned}
\mathbf{y}^T & = \mathbf{x}^T  \mathbf{A} 
& = \begin{pmatrix}x_1 & x_2 & x_3\end{pmatrix} \begin{pmatrix}a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33}\end{pmatrix} 
\end{aligned}
\\]

In Einstein notation, this is written as:

\\[
y_j = a_{ij} x_i
\\]

Be very careful about the indices! Note the difference in the order of the indices
in this expression compared to that of the product of the matrix with a column 
vector. 
