#!/user/bin/env python

from distutils.core import setup
from distutils.extension import Extension

setup(name="Hello module",
	ext_modules=[
		Extension("hello",["hellomodule.cpp"],
				libraries = ["boost_python"])
	])
