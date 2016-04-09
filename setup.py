import os
from distutils import file_util
from distutils import dir_util
from distutils import sysconfig
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

import eigency
import numpy as np

__package_name__ = "eigency"
__eigen_dir__ = eigency.__eigen_dir__

extensions = [
    Extension("eigency.core", ["eigency/core.pyx"],
              include_dirs = [np.get_include(), __eigen_dir__]
    ),
    Extension("eigency.conversions", ["eigency/conversions.pyx"],
              include_dirs = [np.get_include(), __eigen_dir__]
    )
]

dist = setup(
    name = __package_name__,
    version = "1.0",
    description = "Cython interface between the numpy arrays and the Matrix/Array classes of the Eigen C++ library",
    author = "Wouter Boomsma",
    author_email = "wb@bio.ku.dk",
    url = "https://github.com/wouterboomsma/eigency",
    ext_modules = cythonize(extensions),
    packages = [__package_name__]
)

if dist.command_obj.has_key('install'):
    destination_path = dist.command_obj['install'].install_lib
    package_path = os.path.join(destination_path, __package_name__)

    # Copy cython files
    file_util.copy_file('eigency/core.pxd', package_path, update=1, preserve_mode=0)
    file_util.copy_file('eigency/core.pyx', package_path, update=1, preserve_mode=0)
    file_util.copy_file('eigency/conversions.pxd', package_path, update=1, preserve_mode=0)
    file_util.copy_file('eigency/conversions.pyx', package_path, update=1, preserve_mode=0)

    # Copy Eigen header files
    eigen_path = os.path.join(package_path, __eigen_dir__)
    dir_util.copy_tree(__eigen_dir__, eigen_path, update=1, preserve_mode=0)
