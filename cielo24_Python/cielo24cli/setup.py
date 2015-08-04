#!/usr/bin/env python

from setuptools import setup
# Script for PyPI

setup(name='cielo24cli',
      version='1.0.9',
      description='Commmand line for cielo24 package.',
      author='cielo24',
      author_email='support@cielo24.com',
      url='http://www.cielo24.com',
      install_requires=['compago','cielo24'],
      py_modules=['cielo24cli']
      )
