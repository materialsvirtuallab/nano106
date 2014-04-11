#!/usr/bin/env python

"""
TODO: Modify unittest doc.
"""

from __future__ import division

__author__ = "Shyue Ping Ong"
__copyright__ = "Copyright 2012, The Materials Virtual Lab"
__version__ = "0.1"
__maintainer__ = "Shyue Ping Ong"
__email__ = "ongsp@ucsd.edu"
__date__ = "4/10/14"

import unittest

from symmetry.groups import PointGroup, SpaceGroup


class PointGroupTest(unittest.TestCase):

    def test_order(self):
        order = {"mmm": 8, "432": 24, "-6m2": 12}
        for k, v in order.items():
            pg = PointGroup(k)
            self.assertEqual(order[k], len(pg.symmetry_ops))


class SpaceGroupTest(unittest.TestCase):

    def test_order_symm_ops(self):
        for i in range(1, 231):
            sg = SpaceGroup.from_int_number(i, False)
            self.assertEqual(len(sg.symmetry_ops), sg.order)

    def test_crystal_system(self):
        sg = SpaceGroup("R-3c")
        self.assertEqual(sg.crystal_system, "Trigonal")
        sg = SpaceGroup("R-3cH")
        self.assertEqual(sg.crystal_system, "Trigonal")

if __name__ == '__main__':
    unittest.main()
