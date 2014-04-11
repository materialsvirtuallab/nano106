from setuptools import setup, find_packages


setup(
    name="symmetry",
    packages=find_packages(),
    version="0.1",
    install_requires=["numpy"],
    author="Shyue Ping Ong",
    author_email="ongsp@ucsd.edu",
    maintainer="Shyue Ping Ong",
    license="BSD",
    description="Symmetry is a library for materials symmetry analysis.",
    long_description="Symmetry is a library for materials symmetry analysis. "
                     "Please visit the doc and Github repo for more "
                     "information and examples.",
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
