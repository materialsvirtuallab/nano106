LaTeX input:        mmd-mavrldoc-header
Title:              NANO106 Handout 1 - Linear Algebra and Lattice Computations
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

This document provides a summary of the basic linear algebra concepts and their application in crystallography.

# Notation and definitions

Let us define a series of consistent notations. Note that all vectors are written in *column* format for consistency. All vectors are **bolded**.

| Quantity | Notation |
| -------- | -------- |
| Lattice basis vectors | $\mathbf{a_1}$, $\mathbf{a_2}$, $\mathbf{a_3}$ or $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$ |
| Cartesian coordinate vectors | $\mathbf{x}$ or $\mathbf{y}$ |
| Crystal coordinate vectors | $\mathbf{p}$ or $\mathbf{q}$ |
| Metric tensor | $g$ |

\\[\textbf{x} = \begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}\\]
\\[\textbf{p} = \begin{pmatrix}p_1\\p_2\\p_3\end{pmatrix}\\]

For matrices, we will use simple $A$ and $B$ to denote them. $E$ refers to the
identity matrix. In the full form, we denote each element as $a_{ij}$. E.g.

\\[ A = \begin{pmatrix}a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33}\end{pmatrix}
\\]

# Required Linear Algebra Relations

## Norm of a vector in Cartesian coordinates

\\[|\mathbf{x}| = \sqrt{\mathbf{x} \cdot \mathbf{x}} = \sqrt{x_1^2 + x_2^2 + x_3^2}\\]

## Dot product in Cartesian coordinates

\\[ \mathbf{x} \cdot \mathbf{y} = \begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix} \cdot \begin{pmatrix}y_1\\y_2\\y_3\end{pmatrix} = x_1y_1 + x_2y_2 + x_3y_3 =
|\mathbf{x}||\mathbf{y}| \cos \theta
\\]

Finding the angle between two vectors in Cartesian coordinates
\\[
\theta = \cos^{-1}\frac{\mathbf{x}\cdot\mathbf{y}}{|\mathbf{x}||\mathbf{y}|}
\\]

## Cross product in Cartesian coordinates

\\[ \mathbf{x} \times \mathbf{y} = \begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix} \times \begin{pmatrix}y_1\\y_2\\y_3\end{pmatrix} = \begin{pmatrix}x_2y_3 - x_3y_2\\-(x_1y_3 - x_3y_1)\\x_1y_2 - x_2y_1\end{pmatrix}
\\]

## Some matrix relations

\\[ (AB)^T = B^TA^T \\]
\\[(A + B) C = AC + BC\\]
\\[AA^{-1} = A^{-1}A = E \\]

## Finding the determinant and inverse of a $3 \times 3$ matrix.

\\[
det(A) = \begin{vmatrix}a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33}\end{vmatrix} = a_{11} (a_{22}a_{33}-a_{32}a_{23}) -
a_{12} (a_{21}a_{33}-a_{31}a_{23}) + a_{13} (a_{21}a_{32}-a_{31}a_{22})
\\]

\\[
A^{-1} = \frac{1}{det(A)}\begin{pmatrix}a_{22}a_{33}-a_{32}a_{23} & -(a_{21}a_{33}-a_{31}a_{23}) & a_{21}a_{32}-a_{31}a_{22}\\ -(a_{12}a_{33}-a_{32}a_{13} & a_{11}a_{33}-a_{31}a_{13} & -(a_{11}a_{32}-a_{31}a_{12})\\ a_{12}a_{23}-a_{22}a_{13} & -(a_{11}a_{23}-a_{21}a_{13}) & a_{11}a_{22}-a_{21}a_{12}\end{pmatrix}
\\]

# Crystal Coordinates

Given a lattice with basis vectors $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$,
any point in the lattice can be represented in *crystal coordinates* $[uvw]$.
The conversion from crystal coordinates to Cartesian coordinates is given as:

\\[
\mathbf{x} = u \mathbf{a} + v \mathbf{b} + w \mathbf{c}
\\]

# Calculating lattice parameters

Given a set of basis vectors $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$, the lattice parameters are given by:

\\[
a = |\mathbf{a}|\\
b = |\mathbf{b}|\\
c = |\mathbf{c}|\\
\alpha = \cos^{-1}\frac{\mathbf{b}\cdot\mathbf{c}}{|\mathbf{b}||\mathbf{c}|}\\
\beta = \cos^{-1}\frac{\mathbf{a}\cdot\mathbf{c}}{|\mathbf{a}||\mathbf{c}|}\\
\gamma = \cos^{-1}\frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{a}||\mathbf{b}|}
\\]

# Relations in crystal coordinates

For a lattice with basis vectors $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$, the
metric tensor $g$ is given by:

\\[
g = \begin{pmatrix}\mathbf{a}\cdot\mathbf{a} & \mathbf{a}\cdot\mathbf{b}  & \mathbf{a}\cdot\mathbf{c} \\ \mathbf{b}\cdot\mathbf{a} & \mathbf{b}\cdot\mathbf{b} & \mathbf{b}\cdot\mathbf{c} \\ \mathbf{c}\cdot\mathbf{a}  & \mathbf{c}\cdot\mathbf{b}  & \mathbf{c}\cdot\mathbf{c} \end{pmatrix} =
\begin{pmatrix} a^2 & ab \cos \gamma  &  ac \cos \beta \\  ab \cos \gamma &  b^2 &  bc \cos \alpha \\  ac \cos \beta  &  bc \cos \alpha  &  c^2 \end{pmatrix}
\\]

## Dot product in crystal coordinates

It is important to note that dot products between crystal coordinates is not
performed the same way as in Cartesian! You need to use the metric tensor to
perform dot products. The dot product is given by:

\\[
\mathbf{p}^Tg\mathbf{q}
\\]

## Distance in crystal coordinates

For two points defined by $\mathbf{p}$ and $\mathbf{q}$ in crystal coordinates,

\\[
d^2 = (\mathbf{q} - \mathbf{p})^Tg(\mathbf{q} - \mathbf{p})\\
d = \sqrt{(\mathbf{q} - \mathbf{p})^Tg(\mathbf{q} - \mathbf{p})}
\\]

## Angles in crystal coordinates

For three points O, P and Q defined by $\mathbf{o}$, $\mathbf{p}$, and $\mathbf{q}$ in crystal coordinates respectively,

\\[
\vec{OP} = \mathbf{p} - \mathbf{o}\\
\vec{OQ} = \mathbf{q} - \mathbf{o}\\
\hat{POQ} = \cos^{-1} \frac{\vec{OP}^Tg\vec{OQ}}{|\vec{OP}||\vec{OQ}|}
\\]

