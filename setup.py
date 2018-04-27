#!/usr/bin/python

import os
from setuptools import setup
from lib import __version__

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "vSPC",
    version = __version__,
    author = "Zach Loafman",
    author_email = "zmerlynn@sf.net",
    description = ("vSPC is a virtual Serial Port Concentrator for VMware virtual serial ports,"
                   "available in ESXi 4.1+."),
    license = "BSD",
    keywords = "ESX VMWare serial port concentrator",
    url = "https://github.com/romracer/vSPC.py",
    package_dir = {'vSPC': 'lib'},
    scripts = [ 'vSPCClient', 'vSPCServer' ],
    packages=['vSPC'],
    install_requires=['future'],
    #apparently this doesn't always work need to look into this
    #long_description=read('README.md'),
    classifiers=[
      "Development Status :: 3 - Alpha",
      "Topic :: Utilities",
      "License :: OSI Approved :: BSD License",
    ],
)

















