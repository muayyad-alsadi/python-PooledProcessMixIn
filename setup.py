#! /usr/bin/python

# review classifiers http://pypi.python.org/pypi?%3Aaction=list_classifiers

import sys
import os

from setuptools import setup

import PooledProcessMixIn

setup(name='PooledProcessMixIn',
      version=PooledProcessMixIn.__version__,
      description='A Pool of processes and threads Mix-in for socketserver.',
      long_description=PooledProcessMixIn.__doc__,
      author=PooledProcessMixIn.__author__,
      author_email='alsadi@gmail.com',
      url='https://github.com/muayyad-alsadi/python-PooledProcessMixIn',
      py_modules=['PooledProcessMixIn'],
      data_files=[('', ('README.md','TODO')), ('demos', ('demos/demo.py', 'demos/wsgi-demo.py'))],
      license='PSFL',
      platforms = 'any',
      classifiers=['Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'],
     )


