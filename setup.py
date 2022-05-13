from setuptools import setup
from cython.Build import cythonize

setup(
    ext_modules = cythonize("cython.pyx")
)