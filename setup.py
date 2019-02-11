#! /usr/bin/env python

import sys
import os


# Requirements
requirements = open("requirements.txt").read().strip().split("\n")


# take care of extra required modules depending on Python version
extra = {}
try:
    from setuptools import setup, find_packages
    if sys.version_info < (2, 7):
        extra['install_requires'] = ['argparse']
    if sys.version_info >= (3,):
        extra['use_2to3'] = True
except ImportError:
    from distutils.core import setup
    if sys.version_info < (2, 7):
        extra['dependencies'] = ['argparse']

# setup
setup(
    name="combat",
    packages=find_packages(),
    description="Empirical Bayes method to remove batch effects.",
    long_description="python / numpy / pandas / patsy version of ComBat for removing batch effects.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
    keywords="bioinformatics, sequencing, ngs, ngs analysis, " +
             "ATAC-Seq, ChIP-seq, RNA-seq, project management",
    url="https://github.com/afrendeiro/combat",
    **extra
)
