.. symmetry documentation master file, created by
   sphinx-quickstart on Tue Nov 15 00:13:52 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
============

Symmetry is a library for materials symmetry analysis written by Professor
Shyue Ping Ong for his class NANO 106 on Crystallography of Materials.

    *The code is mightier than the pen.*

Latest Change Log
=================

v0.1.0
------
1. First actual working release.

Stable version
--------------

The version at the Python Package Index (PyPI) is always the latest stable
release that will be hopefully, be relatively bug-free. The easiest way to
install symmetry on any system is to use easy_install or pip, as follows::

    easy_install symmetry

or::

    pip install symmetry

Developmental version
---------------------

The bleeding edge developmental version is at the NANO 106's `Github repo
<https://github.com/materialsvirtuallab/nano106>`_. The developmental
version is likely to be more buggy, but may contain new features. The
Github version include test files as well for complete unit testing. After
cloning the source, you can type::

    python setup.py install

or to install the package in developmental mode::

    python setup.py develop

Running unittests
~~~~~~~~~~~~~~~~~

To run the very comprehensive suite of unittests included with the
developmental version, make sure you have nose installed and then just type::

    nosetests

in the symmetry root directory.

Acknowledgements
====================

## Acknowledgements

The author uses the following textbooks and much of the code and material
contained therein is based on concepts in these books. They are highly
recommended for students of crystallography, symmetry and its implications
for material properties.

1. Structure of Materials: An Introduction to Crystallography, Diffraction and
   Symmetry by Marc De Graef and Michael E. McHenry
2. Properties of Materials: Anisotropy, Symmetry, Structure by Robert E.
   Newnham

License
=======

Symmetry is released under the BSD License. The terms of the license are as
follows::

    Copyright (c) 2014, Materials Virtual Lab
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this
      list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.

    * Neither the name of the {organization} nor the names of its
      contributors may be used to endorse or promote products derived from
      this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
