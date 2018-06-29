from pkg_resources import resource_filename
import numpy as np
import os.path
import sys


# conda paths
if sys.platform == 'win32':
    __eigen_dir__ = os.path.abspath(os.__file__ + '\\..\\..\\Library\\include\\eigen3')
else:
    __eigen_dir__ = os.path.abspath(os.__file__ + '/../../../include/eigen3')
assert os.path.isdir(__eigen_dir__)

def get_includes(include_eigen=True):
    root = os.path.dirname(__file__)
    path = [root, np.get_include()]
    if include_eigen:
        path.append(os.path.join(root, __eigen_dir__))
    return path

