from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["fib_c.pyx","fib.py"],annotate=True),
)

""" Build the extension fib.pyx:
$ python setup.py build_ext --inplace
"""