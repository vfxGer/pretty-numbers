# based on https://github.com/pypa/sampleproject/blob/master/setup.py
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

version = '0.0.1'

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name = 'prettynumbers',
    version = version,
    description = 'Display a range of numbers in a human readable way',
    long_description = long_description,
    author = 'Gerard Keating',
    author_email = 'gerardk@gmail.com',
    license = 'MIT',
    url = 'https://github.com/vfxGer/pretty-numbers',
    py_modules = ['pretty_numbers'],
    download_url = 'https://pypi.python.org/packages/source/d/pretty_numbers-%s.tar.gz?raw=true' % (version),
    platforms='Cross-platform',
    classifiers=[
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3'
    ],
)
