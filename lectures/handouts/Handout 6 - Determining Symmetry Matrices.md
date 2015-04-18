LaTeX input:        mmd-mavrldoc-header
Title:              NANO106 Handout 6 - Determining Symmetry Matrices
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

This document outlines how you determine crystal summary matrices. Two fairly
complicated examples are provided to demonstrate the procedure in addition to
the lecture slides.

Let us first outline the general procedure.

1. Find an appropriate crystal system for the symmetry operation. This is
   typically indicated. Otherwise, you should use the more convenient lattice
   compatible with that symmetry. E.g., for 4-fold or 6-fold rotations, you use
   a tetragonal or hexagonal cell.
2. Align the crystal to the appropriate symmetry positions. Sometimes this is
   also specifically spelled out.
3. "Inspect" how your crystal axes transform under the symmetry operation, i.e.,
   just imagine performing the operation on the crystal axes.
4. Express the new lattice vectors in terms of your old lattice vectors.
5. Determine the transformation matrix C that relates your new lattice vectors
   to your old ones.
6. The transpose of the transformation matrix is your crystal symmetry matrix.

![Symmetry operations on crystal axes](SymmetryOperationsOnCrystal.pdf)

# Example 1: Six-fold rotation in hexagonal crystal

Consider the symmetry operation as shown in Figure (i) above. Let us now follow
the steps. Steps 1 and 2 are already done.

Step 3: Figure (i) shows the effect of the symmetry operation on the lattice
vectors.

Step 4: The new lattice vectors can be expressed in terms of the old lattice
vectors as:

$$\mathbf{a'} = \mathbf{a} + \mathbf{b}$$
$$\mathbf{b'} = - \mathbf{a}$$
$$\mathbf{c'} = \mathbf{c}$$

Step 5: We may express the above relationships as the following matrix operation.

\\[
\begin{pmatrix}\mathbf{a'}\\\mathbf{b'}\\\mathbf{c'}\end{pmatrix} = 
\begin{pmatrix}1 & 1 & 0\\-1 & 0 & 0\\0 & 0 & 1\end{pmatrix}
\begin{pmatrix}\mathbf{a}\\\mathbf{b}\\\mathbf{c}\end{pmatrix}
\\]

Step 6: Taking the transpose of the transformation matrix, we have the rotation
matrix as:

\\[
D(6) = \begin{pmatrix}1 & -1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{pmatrix}
\\]

# Example 2: Diagonal vertical mirror plane in tetragonal crystal

Consider the symmetry operation as shown in Figure (ii) above. Let us now follow
the steps. Steps 1 and 2 are already done.

Step 3: Figure (ii) shows the effect of the symmetry operation on the lattice
vectors.

Step 4: The new lattice vectors can be expressed in terms of the old lattice
vectors as:

$$\mathbf{a'} = \mathbf{b}$$
$$\mathbf{b'} = \mathbf{a}$$
$$\mathbf{c'} = \mathbf{c}$$

Step 5: We may express the above relationships as the following matrix operation.

\\[
\begin{pmatrix}\mathbf{a'}\\\mathbf{b'}\\\mathbf{c'}\end{pmatrix} = 
\begin{pmatrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{pmatrix}
\begin{pmatrix}\mathbf{a}\\\mathbf{b}\\\mathbf{c}\end{pmatrix}
\\]

Step 6: Taking the transpose of the transformation matrix, we have the rotation
matrix as:

\\[
D(m_diagonal) = \begin{pmatrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{pmatrix}
\\]