#! /usr/bin/python

import sys
import os
from distutils.core import setup

import PooledProcessMixIn

setup(name='PooledProcessMixIn',
      version=PooledProcessMixIn.__version__,
      description='Fast and simple WSGI-framework for small web-applications.',
      long_description=PooledProcessMixIn.__doc__,
      author=PooledProcessMixIn.__author__,
      author_email='alsadi@gmail.com',
      url='https://github.com/muayyad-alsadi/python-PooledProcessMixIn',
      py_modules=['PooledProcessMixIn'],
      license='PSFL',
      platforms = 'any',
      classifiers=['Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: PSF License',
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


