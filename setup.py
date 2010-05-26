from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='wrapper', version=version,
  author='Asko Soukka',
  author_email='asko.soukka@iki.fi',
  description="Google App Engine wrapper for Repoze BFG.",
  long_description=open("README.txt").read() + "\n" +
                   open("CHANGES.txt").read(),
  license='GPL3',
  # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
  keywords="gae repoze bfg wrapper",
  classifiers=[
    "Programming Language :: Python",
  ],
  url='',
  packages=find_packages(os.sep.join(['src', 'wrapper'])),
  package_dir = {'': os.sep.join(['src', 'wrapper'])},
  include_package_data=True,
  zip_safe=False,
  install_requires=[
    'setuptools',
    # -*- Extra requirements: -*-
    'repoze.bfg',
    'myapp',
  ],
)