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

import os
from itertools import product

import numpy as np

import yaml


with open(os.path.join(os.path.dirname(__file__), "data.yaml")) as f:
    data = yaml.load(f)

GENERATOR_MATRICES = data["generator_matrices"]
POINT_GROUP_ENC = data["point_group_encoding"]
SPACE_GROUP_ENC = data["space_group_encoding"]
TRANSLATIONS = data["translations"]


class SymmetryGroup(object):

    def get_orbit(self, p):
        orbit = []
        for o in self.symmetry_ops:
            pp = np.dot(o, p)
            if not in_array_list(orbit, pp):
                orbit.append(pp)
        return orbit


class PointGroup(SymmetryGroup):
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
        self.symmetry_ops = generate_full_symm(self.generators)


class SpaceGroup(SymmetryGroup):

    def __init__(self, int_symbol):
        enc = list(SPACE_GROUP_ENC[int_symbol]["enc"])
        inversion = int(enc.pop(0))
        ngen = int(enc.pop(0))
        symm_ops = []
        if inversion:
            symm_ops.append([[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0],
                             [0, 0, 0, 1]])
        for i in xrange(ngen):
            m = np.eye(4)
            m[:3, :3] = GENERATOR_MATRICES[enc.pop(0)]
            m[0, 3] = TRANSLATIONS[enc.pop(0)]
            m[1, 3] = TRANSLATIONS[enc.pop(0)]
            m[2, 3] = TRANSLATIONS[enc.pop(0)]
            symm_ops.append(m)

        print symm_ops
        self.symmetry_ops = generate_full_symm(symm_ops)


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


def generate_full_symm(ops):
    symm_ops = list(ops)
    new_ops = ops
    while len(new_ops) > 0:
        gen_ops = []
        for g1, g2 in product(new_ops, symm_ops):
            op = np.dot(g1, g2)
            if not in_array_list(symm_ops, op):
                gen_ops.append(op)
                symm_ops.append(op)
        new_ops = gen_ops
        print symm_ops
        break
    return symm_ops


if __name__ == "__main__":
    from sympy import symbols

    # for k in POINT_GROUP_ENC.keys():
    #     pg = PointGroup(k)
    #     print "Order of point group %s is %d" % (k, len(pg.symmetry_ops))
    #
    # x, y, z = symbols("x y z")
    # p = [x,y,z]
    # pg = PointGroup("m-3m")
    # for r in pg.get_orbit(p):
    #     print r

    sg = SpaceGroup("Fm-3m")
    print len(sg.symmetry_ops)
