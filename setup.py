#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="simplegeo",
      version="1.0.0",
      description="Library for interfacing with SimpleGeo's API",
      author="Joe Stump",
      author_email="joe@simplegeo.com",
      url="http://github.com/simplegeo/python-simplegeo",
      packages = find_packages(),
      license = "MIT License",
      install_requires=['httplib2>=0.6.0', 'oauth2>=1.1.3', 'simplejson>=2.0.9'],
      keywords="simplegeo",
      zip_safe = True,
      tests_require=['nose', 'coverage'])
