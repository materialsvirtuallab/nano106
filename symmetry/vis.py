#!/usr/bin/env python

"""
TODO: Modify module doc.
"""

from __future__ import division

__author__ = "Shyue Ping Ong"
__copyright__ = "Copyright 2013, The Materials Virtual Lab"
__version__ = "0.1"
__maintainer__ = "Shyue Ping Ong"
__email__ = "ongsp@ucsd.edu"
__date__ = "4/12/14"


import inspect
import itertools
import numpy as np
from pymatgen import Lattice
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pymatgen.util.plotting_utils import get_publication_quality_plot


class SpaceGroupVisualizer(object):

    def __init__(self):
        pass

    def plot(self, sg):
        cs = sg.crystal_system
        params = {
            "a": 10,
            "b": 12,
            "c": 14,
            "alpha": 20,
            "beta": 30,
            "gamma": 40
        }
        cs = "rhombohedral" if cs == "Trigonal" else cs
        func = getattr(Lattice, cs.lower())
        kw = {k: params[k] for k in inspect.getargspec(func).args}
        lattice = func(**kw)
        global plt
        fig = plt.figure(figsize=(10, 10))
        #ax = fig.add_subplot(111, projection='3d')
        for i in range(2):
            plt.plot([0, lattice.matrix[i][0]], [0, lattice.matrix[i][1]],
                     'k-')
        plt.plot([lattice.matrix[0][0], lattice.matrix[0][0]],
                 [0, lattice.matrix[1][1]],
                     'k-')
        plt.plot([0, lattice.matrix[0][0]],
                 [lattice.matrix[1][1], lattice.matrix[1][1]],
                 'k-')
        
        l = np.arange(0, 0.02, 0.02 / 100)
        theta = np.arange(0, 4 * np.pi, 4 * np.pi / 100) - np.pi / 2

        x = l * np.cos(theta) + 0.025
        y = l * np.sin(theta) + 0.025
        z = 0.001 * theta + 0.02
        d = np.array(zip(x, y, z, [1] * len(x)))

        for op in sg.symmetry_ops:
            dd = np.dot(op, d.T).T
            for tx, ty in itertools.product((-1, 0, 1), (-1, 0, 1)):
                ddd = dd[:, 0:3] + np.array([tx, ty, 0])[None, :]
                color = "r" if 0.5 < ddd[0, 2] > 1 else "b"
                coords = lattice.get_cartesian_coords(ddd[:, 0:3])
                plt.plot(coords[:, 0], coords[:, 1], color + "-")

        #plt.plot(x, y, 'k-')
        max_l = max(params['a'], params['b'])
        #plt = get_publication_quality_plot(8, 8, plt)
        #plt.savefig('test2png.png',dpi=100)
        lim = [-max_l * 0.1, max_l * 1.1]
        plt.xlim(lim)
        plt.ylim(lim)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    from symmetry.groups import SpaceGroup
    sg = SpaceGroup("Pnma")
    SpaceGroupVisualizer().plot(sg)
