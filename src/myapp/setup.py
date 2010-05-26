from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='myapp', version=version,
  author='Asko Soukka',
  author_email='asko.soukka@iki.fi',
  description="Repoze BFG Example.",
  long_description=open("README.txt").read() + "\n" +
                   open("CHANGES.txt").read(),
  license='GPL3',
  # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
  keywords="",
  classifiers=[
    "Programming Language :: Python",
  ],
  url='',
  packages=find_packages(exclude=['ez_setup']),
  namespace_packages=[],  
  zip_safe=False,
  install_requires=[
    'setuptools',
    # -*- Extra requirements: -*-
    'repoze.bfg'
  ],
)