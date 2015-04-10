LaTeX input:        mmd-mavrldoc-header
Title:              NANO106 Handout 2 - Summary of Coordinate Transformations
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

This document provides a summary of the various coordinate transformations relations and formulas.

# Notation and definitions

Let us define a series of consistent notations. Note that all vectors are written in *column* format for consistency. All vectors are **bolded**.

| Quantity | Notation |
| -------- | -------- |
| Lattice basis vectors | $\mathbf{a_1}$, $\mathbf{a_2}$, $\mathbf{a_3}$ |
| Cartesian coordinate vectors | $\mathbf{x}$ or $\mathbf{y}$ |
| Crystal coordinate vectors | $\mathbf{p}$ or $\mathbf{q}$ |
| Metric tensor | $g$ |

\\[\textbf{x} = \begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}\\]
\\[\textbf{p} = \begin{pmatrix}p_1\\p_2\\p_3\end{pmatrix}\\]

Let us denote a basis transformation from basis vectors $\mathbf{a_i}$ to $\mathbf{a_i'}$ as:

\\[
\begin{pmatrix}\mathbf{a_1'}\\\mathbf{a_2'}\\\mathbf{a_3'}\end{pmatrix} = \begin{pmatrix}c_{11}&c_{12}&c_{13}\\c_{21}&c_{22}&c_{23}\\c_{31}&c_{32}&c_{33}\end{pmatrix} \begin{pmatrix}\mathbf{a_1}\\\mathbf{a_2}\\\mathbf{a_3}\end{pmatrix}
\\]

or more compactly as:

$$\mathbf{A'} = \mathbf{C} \mathbf{A}$$

In the new coordinate ssytem, we add a $'$, e.g., $\mathbf{p'}$ denotes the crystal coordinates in the new basis.

# Transformation relations

The following table summarizes all the coordinate transformas. Be very careful to note whether we are using the transpose of the vector (i.e., writing it in terms of a row instead of a column), the order of the multiplication, and whether we are using the inverse or the direct transformation matrix $C$!

| Transformation | Old basis-> New basis | New basis-> Old basis |
| -------------- | --------------------- | --------------------- |
|Postion/Vector -> Position/Vector|$\mathbf{p'}^T = \mathbf{p}^T\mathbf{C}^{-1}$|$\mathbf{p} = \mathbf{p'}^T\mathbf{C}$|
|Postion/Vector -> Reciprocal Position/Vector|$\mathbf{p^*}^T = \mathbf{p}^Tg$|$\mathbf{p}^T = \mathbf{p^*}^Tg^{-1}$|
|Reciprocal Postion/Vector -> Reciprocal Position/Vector|$\mathbf{p^*}' = \mathbf{C}\mathbf{p^*}$|$\mathbf{p^*} = \mathbf{C}^{-1}\mathbf{p^*}'$|
|Metric Tensor -> Metric Tensor|$g' = \mathbf{C}g\mathbf{C}^T$|$g = \mathbf{C}^{-1}g'(\mathbf{C}^{-1})^T$|






