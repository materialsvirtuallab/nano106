import glob
import os

from setuptools import setup, find_packages, Extension

with open("README.md") as f:
    long_desc = f.read()
    ind = long_desc.find("\n")
    long_desc = long_desc[ind + 1:]

setup(
    name="symmetry",
    packages=find_packages(),
    version="0.0.1",
    install_requires=["numpy", "sympy"],
    author="Shyue Ping Ong",
    author_email="ongsp@ucsd.edu",
    maintainer="Shyue Ping Ong",
    license="BSD",
    description="Symmetry package for NANO106 - Crystallography of Materials",
    long_description=long_desc,
    keywords=["crystallography", "materials", "symmetry", "crystals"],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
)
