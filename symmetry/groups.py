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
        self.symbol = int_symbol
        self.generators = [GENERATOR_MATRICES[c]
                           for c in POINT_GROUP_ENC[int_symbol]]
        self.symmetry_ops = generate_full_symm(self.generators)


class SpaceGroup(SymmetryGroup):

    def __init__(self, int_symbol):
        """
        Initializes a Point Group from its *full* international symbol.
        """
        self.symbol = int_symbol
        enc = list(SPACE_GROUP_ENC[int_symbol]["enc"])
        inversion = int(enc.pop(0))
        ngen = int(enc.pop(0))
        symm_ops = [np.eye(4)]
        if inversion:
            symm_ops.append(np.array(
                [[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0],
                 [0, 0, 0, 1]]))
        for i in xrange(ngen):
            m = np.eye(4)
            m[:3, :3] = GENERATOR_MATRICES[enc.pop(0)]
            m[0, 3] = TRANSLATIONS[enc.pop(0)]
            m[1, 3] = TRANSLATIONS[enc.pop(0)]
            m[2, 3] = TRANSLATIONS[enc.pop(0)]
            symm_ops.append(m)

        self.symmetry_ops = generate_full_symm_sg(symm_ops)

    @classmethod
    def from_int_number(cls, int_number):
        for n, v in SPACE_GROUP_ENC.items():
            if v["int_number"] == int_number:
                return SpaceGroup(n)

    def __str__(self):
        return "Spacegroup %s with order %d" % (self.symbol,
                                                len(self.symmetry_ops))


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
    while len(new_ops) > 0 and len(symm_ops) < 192:
        gen_ops = []
        for g1, g2 in product(new_ops, symm_ops):
            op = np.dot(g1, g2)
            if not in_array_list(symm_ops, op):
                gen_ops.append(op)
                symm_ops.append(op)
        new_ops = gen_ops
    return symm_ops


def generate_full_symm_sg(ops):
    symm_ops = list(ops)
    for op in symm_ops:
        op[0:3, 3] = np.mod(op[0:3, 3], 1)
    new_ops = ops
    while len(new_ops) > 0:
        gen_ops = []
        for g1, g2 in product(new_ops, symm_ops):
            op = np.dot(g1, g2)
            op[0:3, 3] = np.mod(op[0:3, 3], 1)
            if not in_array_list(symm_ops, op):
                gen_ops.append(op)
                symm_ops.append(op)
        new_ops = gen_ops
    return symm_ops


def get_spacegroup():
    sg = SpaceGroup("Fm-3m")
    print len(sg.symmetry_ops)


def profile_sg():
    import cProfile
    cProfile.run('get_spacegroup()', 'stats')
    import pstats
    p = pstats.Stats('stats')
    p.strip_dirs().sort_stats(-1).print_stats()
    import os
    os.remove("stats")


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
    sg = SpaceGroup.from_int_number(1)
    print sg
    sg = SpaceGroup("Fm-3m")
    print sg
    # print len(sg.symmetry_ops)
    #sg = SpaceGroup("Im-3m")
    #print len(sg.symmetry_ops)
    # import json
    # with open("names") as f:
    #     names = json.load(f)
    # for i, n in enumerate(names):
    #     try:
    #         int_no = SPACE_GROUP_ENC[n]["int_number"]
    #         if i != int_no - 1:
    #             print "Bad number for %s" % n
    #     except KeyError:
    #         for k, v in SPACE_GROUP_ENC.items():
    #             if v["int_number"] == i + 1:
    #                 print "%s --> %s" % (k, n)

