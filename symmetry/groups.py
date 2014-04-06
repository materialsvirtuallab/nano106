#!/usr/bin/env python

"""
TODO: Modify module doc.
"""

from __future__ import division

__author__ = "Shyue Ping Ong"
__copyright__ = "Copyright 2012, The Materials Project"
__version__ = "0.1"
__maintainer__ = "Shyue Ping Ong"
__email__ = "shyuep@gmail.com"
__date__ = "4/4/14"

from itertools import product
import numpy as np

from symmetry.data import GENERATOR_MATRICES, POINT_GROUP_ENC


class PointGroup(object):
    """
    Object representing a Point Group, with generators and symmetry operations.
    """

    def __init__(self, int_symbol):
        """
        Initializes a Point Group from its international symbol.

        Args:
            int_symbol (str): International or Hermann-Mauguin Symbol.
        """
        self.generators = [GENERATOR_MATRICES[c]
                           for c in POINT_GROUP_ENC[int_symbol]]
        symm_ops = []
        symm_ops.extend(self.generators)
        new_ops = self.generators
        while len(new_ops) > 0:
            gen_ops = []
            for g1, g2 in product(new_ops, symm_ops):
                op = np.dot(g1, g2)
                if not in_array_list(symm_ops, op):
                    gen_ops.append(op)
                    symm_ops.append(op)
            new_ops = gen_ops
        self.symmetry_ops = symm_ops

    def get_orbit(self, p):
        orbit = []
        for o in self.symmetry_ops:
            pp = np.dot(o, p)
            if not in_array_list(orbit, pp):
                orbit.append(pp)
        return orbit


class SpaceGroup(object):

    def __init__(self, int_symbol):
        pass


def in_array_list(array_list, a):
    """
    Extremely efficient nd-array comparison using numpy's broadcasting. This
    function checks if a particular array a, is present in a list of arrays.
    It works for arrays of any size, e.g., even matrix searches.
    """
    if len(array_list) == 0:
        return False
    axes = tuple(range(1, a.ndim + 1))
    return np.any(np.all(np.equal(array_list, a[None, :]), axes))


if __name__ == "__main__":
    for k in POINT_GROUP_ENC.keys():
        pg = PointGroup(k)
        print "Order of point group %s is %d" % (k, len(pg.symmetry_ops))

    from sympy import symbols
    x, y, z = symbols("x y z")
    p = [x,y,z]
    pg = PointGroup("m-3m")
    for r in pg.get_orbit(p):
        print r
