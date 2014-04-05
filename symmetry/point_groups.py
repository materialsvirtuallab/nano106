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

import itertools
import numpy as np

#Define the fundamental symmetry matrices

D = {
    "a": [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]],
    "b": [[-1, 0, 0],
          [0, -1, 0],
          [0, 0, 1]],
    "c": [[-1, 0, 0],
          [0, 1, 0],
          [0, 0, -1]],
    "d": [[0, 0, 1],
          [1, 0, 0],
          [0, 1, 0]],
    "e": [[0, 1, 0],
          [1, 0, 0],
          [0, 0, -1]],
    "f": [[0, -1, 0],
          [-1, 0, 0],
          [0, 0, -1]],
    "g": [[0, -1, 0],
          [1, 0, 0],
          [0, 0, 1]],
    "h": [[-1, 0, 0],
          [0, -1, 0],
          [0, 0, -1]],
    "i": [[1, 0, 0],
          [0, 1, 0],
          [0, 0, -1]],
    "j": [[1, 0, 0],
          [0, -1, 0],
          [0, 0, 1]],
    "k": [[0, -1, 0],
          [-1, 0, 0],
          [0, 0, 1]],
    "l": [[0, 1, 0],
          [1, 0, 0],
          [0, 0, 1]],
    "m": [[0, 1, 0],
          [-1, 0, 0],
          [0, 0, -1]],
    "n": [[0, -1, 0],
          [1, -1, 0],
          [0, 0, 1]]
}

D = {k: np.array(v) for k, v in D.items()}

POINT_GROUPS_GENERATORS = {
    "1": "a",
    "-1": "h",
    "2": "c",
    "m": "j",
    "2/m": "ch",
    "222": "bc",
    "mm2": "bj",
    "mmm": "bch",
    "4": "g",
    "-4": "m",
    "4/m": "gh",
    "422": "cg",
    "4mm": "gj",
    "-42m": "cm",
    "4/mmm": "cgh",
    "3": "n",
    "-3": "hn",
    "32": "en",
    "3m": "kn",
    "-3m": "fhn",
    "6": "bn",
    "-6": "in",
    "6/m": "bhn",
    "622": "ben",
    "6mm": "bkn",
    "-6m2": "ikn",
    "6/mmm": "benh",
    "23": "cd",
    "m-3": "cdh",
    "432": "dg",
    "-43m": "dml",
    "m-3m": "dghl"
}

class PointGroup(object):
    """
    Object representing a Point Group, with generators and symmetry operations.
    """

    def __init__(self, int_symbol):
        self.generators = [D[c] for c in POINT_GROUPS_GENERATORS[int_symbol]]
        symm_ops = []
        symm_ops.extend(self.generators)
        new_ops = self.generators

        while len(new_ops) > 0:
            gen_ops = []
            for g1, g2 in itertools.product(new_ops, symm_ops):
                #Note that we cast the op to int to improve presentation of the results.
                #This is fine in crystallographic reference frame.
                op = np.dot(g1, g2)
                if not in_array_list(symm_ops, op):
                    gen_ops.append(op)
                    symm_ops.append(op)
                op = np.dot(g2, g1)
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


def in_array_list(array_list, a):
    for i in array_list:
        if np.all(np.equal(a, i)):
            return True
    return False

if __name__ == "__main__":
    for k in POINT_GROUPS_GENERATORS.keys():
        pg = PointGroup(k)
        print "Order of point group %s is %d" % (k, len(pg.symmetry_ops))