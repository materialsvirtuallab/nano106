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

This document provides a summary of the basic linear algebra concepts and their
application in crystallography.

# Notation and definitions

Let us define a series of consistent notations. Note that all vectors are
written in *column* format for consistency. All vectors are **bolded**.

| Quantity | Notation |
| -------- | -------- |
| Lattice basis vectors | $\mathbf{a_1}$, $\mathbf{a_2}$, $\mathbf{a_3}$ or $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$ |
| Cartesian coordinate vectors | $\mathbf{x}$ or $\mathbf{y}$ |
| Crystal coordinate vectors | $\mathbf{p}$ or $\mathbf{q}$ |
| Metric tensor | $g$ |

\\[\textbf{x} = \begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}\\]
\\[\textbf{p} = \begin{pmatrix}p_1\\p_2\\p_3\end{pmatrix}\\]

For matrices, we will use simple $\mathbf{A}$ and $\mathbf{B}$ to denote them.
$\mathbf{E}$ refers to the identity matrix. In the full form, we denote each element 
as $a_{ij}$. E.g.

\\[
\mathbf{A} = \begin{pmatrix}a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33}\end{pmatrix}
\\]

Transposes and inverses are indicated by superscript $T$ and $-1$ respectively, e.g.,
$\mathbf{A}^T$ and $\mathbf{A}^{-1}$. 

# Required Linear Algebra Relations

We will start with the standard linear algebra relations in Cartesian coordinates.
Make sure you understand the difference between Cartesian and crystal coordinates. 
They are not the same thing and you need to use different formulas for them.

## Norm of a vector in Cartesian coordinates

\\[
\begin{aligned}
|\mathbf{x}| & = \sqrt{\mathbf{x} \cdot \mathbf{x}}\\
& = \sqrt{\mathbf{x}^T \mathbf{x}}\\
&= \sqrt{x_1^2 + x_2^2 + x_3^2}
\end{aligned}
\\]

## Dot product in Cartesian coordinates

\\[
\begin{aligned}
\mathbf{x} \cdot \mathbf{y} &= \begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix} \cdot \begin{pmatrix}y_1\\y_2\\y_3\end{pmatrix}\\
&= x_1y_1 + x_2y_2 + x_3y_3\\
& = |\mathbf{x}||\mathbf{y}| \cos \theta
\end{aligned}
\\]

Finding the angle between two vectors in Cartesian coordinates
\\[
\theta = \cos^{-1}\frac{\mathbf{x}\cdot\mathbf{y}}{|\mathbf{x}||\mathbf{y}|}
\\]

## Cross product in Cartesian coordinates

\\[ \mathbf{x} \times \mathbf{y} = \begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix} \times \begin{pmatrix}y_1\\y_2\\y_3\end{pmatrix} = \begin{pmatrix}x_2y_3 - x_3y_2\\-(x_1y_3 - x_3y_1)\\x_1y_2 - x_2y_1\end{pmatrix}
\\]

## Some matrix relations

\\[
\begin{aligned}
(\mathbf{A} \mathbf{B})^T & = \mathbf{B}^T\mathbf{A}^T \\
(\mathbf{A} + \mathbf{B}) \mathbf{C} & = \mathbf{A}\mathbf{C} + \mathbf{B}\mathbf{C}\\
\mathbf{A}\mathbf{A}^{-1} & = \mathbf{A}^{-1}\mathbf{A} = \mathbf{E} 
\end{aligned}
\\]

## Finding the determinant and inverse of a $3 \times 3$ matrix.

\\[
\begin{aligned}
\det(\mathbf{A}) &= \begin{vmatrix}a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33}\end{vmatrix}
\\&= a_{11} (a_{22}a_{33}-a_{32}a_{23}) -
a_{12} (a_{21}a_{33}-a_{31}a_{23}) + a_{13} (a_{21}a_{32}-a_{31}a_{22})
\end{aligned}
\\]

\\[
\mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})}\begin{pmatrix}a_{22}a_{33}-a_{32}a_{23} & -(a_{21}a_{33}-a_{31}a_{23}) & a_{21}a_{32}-a_{31}a_{22}\\ -(a_{12}a_{33}-a_{32}a_{13} & a_{11}a_{33}-a_{31}a_{13} & -(a_{11}a_{32}-a_{31}a_{12})\\ a_{12}a_{23}-a_{22}a_{13} & -(a_{11}a_{23}-a_{21}a_{13}) & a_{11}a_{22}-a_{21}a_{12}\end{pmatrix}
\\]

# Crystal Coordinates

![Crystal vs Cartesian coordinates](CrystalvsCartesian.pdf)

Refer to the figure above. The figure on the left represents a crystal. In general,
the lattice vectors $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$ may not be orthogonal to 
each other, and are not of unit length. On the right, we have the Cartesian 
coordinate system where the basis vectors are orthogonal and unit length.

Consider the point P in the crystal, which has *crystal coordinates* (also known
as *fractional* or *direct* coordinates) denoted by [u, v, w]. In the example
above, the crystal coordinates are [0.25, 0.25, 0.25]. The conversion from
crystal coordinates to Cartesian coordinates is given as:

\\[
\mathbf{x} = u \mathbf{a} + v \mathbf{b} + w \mathbf{c}
\\]

For the sake of illustration, let's say the lattice vectors, when expressed in the 
Cartesian coordinate system are:

\\[
\begin{aligned}
\mathbf{a} = \begin{pmatrix}2\\0\\0\end{pmatrix},
\mathbf{b} = \begin{pmatrix}-1\\3\\0\end{pmatrix},
\mathbf{c} = \begin{pmatrix}0\\0\\4\end{pmatrix}
\end{aligned}
\\]

The Cartesian coordinates of point P are then:

\\[
\mathbf{x} = 0.25 \begin{pmatrix}2\\0\\0\end{pmatrix} + 0.25 \begin{pmatrix}-1\\3\\0\end{pmatrix} + 0.25 \begin{pmatrix}0\\0\\4\end{pmatrix} = \begin{pmatrix}0.25\\0.75\\1\end{pmatrix}
\\]

Note that the **crystal coordinates are different from the Cartesian coordinates**.
The crystal coordinates are the coordinates defined in the vector space formed by the
lattice vectors. In crystallography, you frequently work with crystal coordinates.
To compute things like distances, angles, etc. you can either convert your crystal
coordinates to Cartesian first before using your usual Cartesian relations, or you 
can use the metric tensor to perform the necessary dot products and distances 
computations directly from your crystal coordinates.

# Calculating lattice parameters

Given a set of basis vectors $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$, the lattice parameters are given by:

\\[
\begin{aligned}
a & = |\mathbf{a}|\\
b & = |\mathbf{b}|\\
c & = |\mathbf{c}|\\
\alpha & = \cos^{-1}\frac{\mathbf{b}\cdot\mathbf{c}}{|\mathbf{b}||\mathbf{c}|}\\
\beta & = \cos^{-1}\frac{\mathbf{a}\cdot\mathbf{c}}{|\mathbf{a}||\mathbf{c}|}\\
\gamma & = \cos^{-1}\frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{a}||\mathbf{b}|}
\end{aligned}
\\]

# Relations in crystal coordinates

For a lattice with basis vectors $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$, the
metric tensor $g$ is given by:

\\[
g = \begin{pmatrix}\mathbf{a}\cdot\mathbf{a} & \mathbf{a}\cdot\mathbf{b}  & \mathbf{a}\cdot\mathbf{c} \\ \mathbf{b}\cdot\mathbf{a} & \mathbf{b}\cdot\mathbf{b} & \mathbf{b}\cdot\mathbf{c} \\ \mathbf{c}\cdot\mathbf{a}  & \mathbf{c}\cdot\mathbf{b}  & \mathbf{c}\cdot\mathbf{c} \end{pmatrix} =
\begin{pmatrix} a^2 & ab \cos \gamma  &  ac \cos \beta \\  ab \cos \gamma &  b^2 &  bc \cos \alpha \\  ac \cos \beta  &  bc \cos \alpha  &  c^2 \end{pmatrix}
\\]

## Dot product in crystal coordinates

Dot products between crystal coordinates is not performed the same way as in 
Cartesian! You need to use the metric tensor to perform dot products. The dot product 
is given by:

\\[
\mathbf{p}^Tg\mathbf{q}
\\]

## Distance between points and length of vector in crystal coordinates

For two points defined by $\mathbf{p}$ and $\mathbf{q}$ in crystal coordinates,

\\[
\begin{aligned}
d^2 &= (\mathbf{q} - \mathbf{p})^Tg(\mathbf{q} - \mathbf{p})\\
d &= \sqrt{(\mathbf{q} - \mathbf{p})^Tg(\mathbf{q} - \mathbf{p})}
\end{aligned}
\\]

Similarly, the length of a vector $\mathbf{p}$ in crystal coordinates is given as:

\\[
d = \sqrt{\mathbf{p}^Tg\mathbf{p}}
\\]

## Angles in crystal coordinates

For three points O, P and Q defined by $\mathbf{o}$, $\mathbf{p}$, and $\mathbf{q}$ in crystal coordinates respectively,

\\[
\begin{aligned}
\vec{OP} & = \mathbf{p} - \mathbf{o}\\
\vec{OQ} & = \mathbf{q} - \mathbf{o}\\
\hat{POQ} & = \cos^{-1} \frac{\vec{OP}^Tg\vec{OQ}}{|\vec{OP}||\vec{OQ}|}
\end{aligned}
\\]

