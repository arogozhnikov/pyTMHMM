"""
Minimal setup.py for Cython extension building.
All package metadata is now in pyproject.toml.
"""

import numpy
from Cython.Build import cythonize
from setuptools import setup, Extension


ext = [
    Extension(
        "pyTMHMM.hmm",
        ["pyTMHMM/hmm.pyx"],
        include_dirs=[numpy.get_include(), "."],
    )
]

setup(
    ext_modules=cythonize(ext),
)
