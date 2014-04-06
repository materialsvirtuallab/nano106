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
__date__ = "4/5/14"


import yaml
import os

with open(os.path.join(os.path.dirname(__file__), "data.yaml")) as f:
    data = yaml.load(f)

GENERATOR_MATRICES = data["generator_matrices"]
POINT_GROUP_ENC = data["point_group_encoding"]
SPACE_GROUP_ENC = data["space_group_encoding"]
TRANSLATIONS = data["translations"]