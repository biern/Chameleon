#!/usr/bin/env python
#-*- coding: utf-8 -*-

import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

import os

here = os.path.abspath(os.path.dirname(__file__))
NAME = "Chameleon"
VERSION = open(os.path.join(here, 'VERSION')).read()
README = ""
NEWS = ""

install_requires = [

]

setup(name=NAME,
      version=VERSION,
      entry_points={
        'console_scripts': [
            'chameleon = chameleon.tools:shell_eval'
            ]
        },
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=True,
      install_requires=install_requires,
      description="{}".format(NAME),
      long_description=README + '\n\n' + NEWS,
      keywords='{}'.format(NAME),
)
