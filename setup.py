#!/usr/bin/python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
 
module1 = Extension("openhmd", 
    ["pyopenhmd.pyx", "OpenHMD.cpp"],
    language="c++",
    libraries=["hidapi-libusb"],
    extra_objects=["lib/libopenhmd.a"],
    include_dirs=['lib/'])
 
setup(name = 'openhmd',
    version = '1.0',
    description = 'Python OpenHMD Wrapper',
    ext_modules=[module1],
    cmdclass = {'build_ext': build_ext})
