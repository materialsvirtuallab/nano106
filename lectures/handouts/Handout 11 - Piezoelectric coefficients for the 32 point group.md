LaTeX input:        mmd-mavrldoc-header
Title:              NANO106 Handout 11 - Piezoelectric coefficients for the 32 point group
Author:             Shyue Ping Ong
Affiliation:        University of California, San Diego
Address:            9500 Gilman Drive, Mail Code 0448, La Jolla, CA 92093-0448
Web:                http://www.materialsvirtuallab.org
Base Header Level:  2
LaTeX Mode:         mavrldoc
LaTeX input:        mmd-mavrldoc-begin-doc
LaTeX footer:       mmd-mavrldoc-footer
xhtml header:       <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

In this handout, we will go through the full exercise of deriving the form of
the piezoelectric matrix for the 32 point group, which is fairly complex.

# The $32$ point group

![The 32 point group][]

The IEEE standard setting for the $32$ point group is given above. The
3-fold rotation is oriented parallel to $Z_3$ and one of the 2-fold
rotations is oriented parallel to $Z_1$.

# General procedure for deriving symmetry restrictions

The general procedure for deriving symmetry restrictions in tensors is given
below.

1. Convert from Voigt to tensor notation if necessary. This is only required
   if you are working with higher-order tensors that utilizes the Voigt matrix
   form.
2. Determine the mapping of axes for the symmetry operations of the point
   group.
3. Apply mapping to tensor elements and Neumann's Principle.
4. Determine equalities and elements with value 0.

# Piezoelectric matrix and tensor

The piezoelectric matrix has the following Voigt form:
\\[
\begin{pmatrix}
d_{11} & d_{12} & d_{13} & d_{14} & d_{15} & d_{16}\\
d_{21} & d_{22} & d_{23} & d_{24} & d_{25} & d_{26}\\
d_{31} & d_{32} & d_{33} & d_{34} & d_{35} & d_{36}
\end{pmatrix}
\\]

If we explicitly write out all the elements in terms of the tensor elements,
we have:

\\[
\begin{pmatrix}
d_{111} & d_{122} & d_{133} & d_{123} + d_{132} & d_{113} + d_{131} & d_{112} + d_{121}\\
d_{211} & d_{222} & d_{233} & d_{223} + d_{232} & d_{213} + d_{231} & d_{212} + d_{221}\\
d_{311} & d_{322} & d_{333} & d_{323} + d_{332} & d_{313} + d_{331} & d_{312} + d_{321}
\end{pmatrix}
\\]

# Symmetry constraints of the 2-fold rotation about $Z_1$

Let us start with the simpler symmetry operation of the 2-fold rotation
about $Z_1$. The relationship between the rotated axes and the original axes
is given as:

\\[
\begin{aligned}
X_1' & = X_1\\
X_2' & = -X_2\\
X_3' & = -X_3
\end{aligned}
\\]

Let us consider the implications of this mapping on a few tensor elements.

For $d_{11}$, we have $d_{11} \rightarrow d_{111}$ (Voigt to tensor). $d_{111}$
transforms as:

\\[
\begin{aligned}
X_1'X_1'X_1' & = X_1 X_1 X_1\\
\implies d_{111}' & = d_{111} = d_{111} \mbox{ (Neumann's Principle)}
\end{aligned}
\\]

Hence, there are no restrictions on $d_{11}$.

For $d_{21}$, we have $d_{21} \rightarrow d_{211}$ (Voigt to tensor). $d_{211}$
transforms as:

\\[
\begin{aligned}
X_2'X_1'X_1' & = (-X_2) X_1 X_1\\
\implies d_{211}' & = -d_{211} = d_{211} \mbox{ (Neumann's Principle)}\\
\implies d_{211} & = 0
\end{aligned}
\\]

Hence, $d_{21} = 0$. From this result, we can infer that all tensor elements
that have an odd number of indices 2 and 3 will be constrained to be 0 by the
2-fold rotation (because of the negation of the $X_2$ and $X_3$). Hence,

\\[
\begin{aligned}
d_{113} = d_{131} = d_{112} = d_{121} = d_{211} = d_{222} = d_{233} =  d_{223} = d_{232} = d_{311} = d_{322} = d_{333} = d_{323} = d_{332} = 0\\
\implies d_{15} = d_{16} = d_{21} = d_{22} = d_{23} = d_{24} = d_{31} = d_{32} = d_{33} = d_{34} = 0 \mbox{ (after conversion to Voigt form) }
\end{aligned}
\\]

Hence, our piezoelectric matrix is now simplified to:

\\[
\begin{pmatrix}
d_{11} & d_{12} & d_{13} & d_{14} & 0 & 0\\
0 & 0 & 0 & 0 & d_{25} & d_{26}\\
0 & 0 & 0 & 0 & d_{35} & d_{36}
\end{pmatrix}
\\]

# Symmetry constraints of the 3-fold rotation about $Z_3$

For the 3-fold rotation about $Z_3$, the relationship between the rotated axes and the original axes is given as:

\\[
\begin{aligned}
\begin{pmatrix} \mathbf{e_1'} \\ \mathbf{e_2'} \\ \mathbf{e_3'} \end{pmatrix} = \begin{pmatrix} \cos{120^\circ} & -\sin{120^\circ} & 0 \\ \sin{120^\circ} & \cos{120^\circ} & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} \mathbf{e_1} \\ \mathbf{e_2} \\ \mathbf{e_3} \end{pmatrix}
\end{aligned}
\\]

Hence, the mapping is given as:

\\[
\begin{aligned}
X_1' & = -\frac{1}{2} X_1 - \frac{\sqrt{3}}{2} X_2\\
X_2' & =  \frac{\sqrt{3}}{2} X_1 - \frac{1}{2} X_2\\
X_3' & = X_3
\end{aligned}
\\]

## Constraints on $d_{13}$

Let us start with some of the simpler relationships first.

For $d_{13}$, we have $d_{13} \rightarrow d_{133}$ (Voigt to tensor).
$d_{133}$ transforms as:

\\[
\begin{aligned}
X_1'X_3'X_3' & = (-\frac{1}{2} X_1 - \frac{\sqrt{3}}{2} X_2)X_3X_3\\
& = -\frac{1}{2} X_1 X_3 X_3 - \frac{\sqrt{3}}{2} X_2 X_3 X_3 \\
\implies d_{133}' & = -\frac{1}{2} d_{133} - \frac{\sqrt{3}}{2} d_{233}\\
\implies d_{133}' & = -\frac{1}{2} d_{133} \mbox{ ($d_{233}$ was shown to be zero earlier) }\\
\implies  -\frac{1}{2} d_{133} & = d_{133} \mbox{ (Neumann's Principle) }\\
\implies d_{133} & = 0\\
\implies d_{13} & = 0
\end{aligned}
\\]

## Constraints on $d_{35}$

For $d_{35}$, we have $d_{35} \rightarrow d_{313} + d_{331}$ (Voigt to tensor).
$d_{313}$ transforms as:

\\[
\begin{aligned}
X_3'X_1'X_3' & = X_3(-\frac{1}{2} X_1 - \frac{\sqrt{3}}{2} X_2)X_3\\
& = -\frac{1}{2} X_3 X_1 X_3 - \frac{\sqrt{3}}{2} X_3 X_2 X_3 \\
\implies d_{313}' & = -\frac{1}{2} d_{313} - \frac{\sqrt{3}}{2} d_{323}\\
\implies d_{313}' & = -\frac{1}{2} d_{313} \mbox{ ($d_{323}$ was shown to be zero earlier)} = d_{313}\\
\implies d_{313} & = 0\\
\mbox{Similarly, } d_{331} & = 0\\
\implies d_{35} & = 0
\end{aligned}
\\]

## Constraints on $d_{36}$

For $d_{36}$, we have $d_{36} \rightarrow d_{312} + d_{321}$ (Voigt to tensor).
$d_{312}$ transforms as:

\\[
\begin{aligned}
X_3'X_1'X_2' & = X_3(-\frac{1}{2} X_1 - \frac{\sqrt{3}}{2} X_2)(\frac{\sqrt{3}}{2} X_1 - \frac{1}{2} X_2)\\
& = -\frac{\sqrt{3}}{4} X_3 X_1 X_1 + \frac{1}{4} X_3 X_1 X_2 - \frac{3}{4} X_3 X_2 X_1 + \frac{\sqrt{3}}{4} X_3 X_2 X_2 \\
\implies d_{312}' & = -\frac{\sqrt{3}}{4} d_{311} + \frac{1}{4} d_{312} - \frac{3}{4} d_{321} + \frac{\sqrt{3}}{4} d_{322}
\end{aligned}
\\]

Zeroing out the elements we have determined earlier and applying Neumann's
Principle, we have

\\[
\begin{aligned}
d_{312}' & = \frac{1}{4} d_{312} - \frac{3}{4} d_{321} = d_{312}\\
\implies d_{312} & = - d_{321}
\end{aligned}
\\]

Hence, $d_{36} = d_{312} + d_{321} = 0$

## Constraints on $d_{14}$ and $d_{25}$

For $d_{25}$, we have $d_{25} \rightarrow d_{213} + d_{231}$ (Voigt to tensor).
$d_{213}$ transforms as:

\\[
\begin{aligned}
X_2'X_1'X_3' & = (\frac{\sqrt{3}}{2} X_1 - \frac{1}{2} X_2)(-\frac{1}{2} X_1 - \frac{\sqrt{3}}{2} X_2)X_3\\
& = -\frac{\sqrt{3}}{4} X_1 X_1 X_3 - \frac{3}{4} X_1 X_2 X_3 + \frac{1}{4} X_2 X_1 X_3 + \frac{\sqrt{3}}{4} X_2 X_2 X_3 \\
\implies d_{213}' & = -\frac{\sqrt{3}}{4} d_{113} - \frac{3}{4} d_{123} + \frac{1}{4} d_{213} + \frac{\sqrt{3}}{4} d_{223} \\
\implies d_{213}' & = -\frac{3}{4} d_{123} + \frac{1}{4} d_{213} = d_{213} \\
\implies -d_{123} & = d_{213} \\
\implies d_{25} & = - d_{14}
\end{aligned}
\\]

## Constraints on $d_{11}$, $d_{12}$ and $d_{26}$

For $d_{11}$, we have $d_{11} \rightarrow d_{111}$ (Voigt to tensor).
$d_{111}$ transforms as:

\\[
\begin{aligned}
X_1'X_1'X_1' & = (-\frac{1}{2} X_1 - \frac{\sqrt{3}}{2} X_2)(-\frac{1}{2} X_1 - \frac{\sqrt{3}}{2} X_2)(-\frac{1}{2} X_1 - \frac{\sqrt{3}}{2} X_2)\\
& = -\frac{1}{8} X_1 X_1 X_1 - \frac{\sqrt{3}}{8} X_1 X_1 X_2 \\
& - \frac{\sqrt{3}}{8} X_1 X_2 X_1 - \frac{3}{8} X_1 X_2 X_2 \\
& - \frac{\sqrt{3}}{8} X_2 X_1 X_1 - \frac{3}{8} X_2 X_1 X_2 \\
& - \frac{3}{8} X_2 X_2 X_1 - \frac{3\sqrt{3}}{8} X_2 X_2 X_2\\
\implies d_{111}' & = -\frac{1}{8} d_{111} - \frac{\sqrt{3}}{8} d_{112} - \frac{\sqrt{3}}{8} d_{121} - \frac{3}{8} d_{122} - \frac{\sqrt{3}}{8} d_{211} - \frac{3}{8} d_{212} - \frac{3}{8} d_{221} - \frac{3\sqrt{3}}{8} d_{222}\\
& = -\frac{1}{8} d_{111} - \frac{3}{8} d_{122} - \frac{3}{8} d_{212} - \frac{3}{8} d_{221} \mbox{ (some of the tensor elements are already 0)}
\end{aligned}
\\]

In matrix form, we have:

\\[
\begin{aligned}
d_{11}' = -\frac{1}{8} d_{11} - \frac{3}{8} d_{12} - \frac{3}{8} d_{26} = d_{11}\\
\implies 3d_{11} + d_{12} + d_{26} = 0
\end{aligned}
\\]

For $d_{12}$, we have $d_{12} \rightarrow d_{122}$ (Voigt to tensor).
$d_{122}$ transforms as:

\\[
\begin{aligned}
X_1'X_2'X_2' & = (-\frac{1}{2} X_1 - \frac{\sqrt{3}}{2} X_2)(\frac{\sqrt{3}}{2} X_1 - \frac{1}{2} X_2)(\frac{\sqrt{3}}{2} X_1 - \frac{1}{2} X_2)\\
& = -\frac{3}{8} X_1 X_1 X_1 + \frac{\sqrt{3}}{8} X_1 X_1 X_2 \\
& + \frac{\sqrt{3}}{8} X_1 X_2 X_1 - \frac{1}{8} X_1 X_2 X_2 \\
& - \frac{3\sqrt{3}}{8} X_2 X_1 X_1 + \frac{3}{8} X_2 X_1 X_2 \\
& + \frac{3}{8} X_2 X_2 X_1 - \frac{\sqrt{3}}{8} X_2 X_2 X_2\\
\implies d_{122}' & = -\frac{3}{8} d_{111} + \frac{\sqrt{3}}{8} d_{112} + \frac{\sqrt{3}}{8} d_{121} - \frac{1}{8} d_{122} - \frac{3\sqrt{3}}{8} d_{211} + \frac{3}{8} d_{212} + \frac{3}{8} d_{221} - \frac{\sqrt{3}}{8} d_{222}\\
& = -\frac{3}{8} d_{111} - \frac{1}{8} d_{122} + \frac{3}{8} d_{212} + \frac{3}{8} d_{221} \mbox{ (some of the tensor elements are already 0)}
\end{aligned}
\\]

In matrix form, we have:

\\[
\begin{aligned}
d_{12}' = -\frac{3}{8} d_{11} - \frac{1}{8} d_{12} + \frac{3}{8} d_{26} = d_{12}\\
\implies d_{11} + 3 d_{12} - d_{26} = 0
\end{aligned}
\\]

Combining the relations derived for $d_{11}$ and $d_{12}$, we get:

\\[
\begin{aligned}
4d_{11} + 4 d_{12} = 0\\
\implies d_{12} = -d_{11} \mbox{ and } d_{26} = -2d_{11}
\end{aligned}
\\]

# Conclusion

Incorporating all the symmetry restrictions, we finally get the simplified
form of the piezoelectric matrix as follows:

\\[
\begin{pmatrix}
d_{11} & -d_{11} & 0 & d_{14} & 0 & 0\\
0 & 0 & 0 & 0 & -d_{14} & -2d_{11}\\
0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
\\]

In general, this is a more involved process than usual because the trigonal
3-fold rotation does not align with orthogonal axes. For 4-fold symmetry, the
process is considerably simpler. But it is useful to go through this, which illustrates all the key steps of deriving symmetry restrictions.

[The 32 point group]: 32.png "The 32 point group" width=150px
