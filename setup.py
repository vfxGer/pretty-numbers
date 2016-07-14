from distutils.core import setup

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
    license = 'LICENCE.txt',
    url = 'https://github.com/vfxGer/pretty-numbers',
    py_modules = ['pretty_numbers'],
    download_url = 'https://pypi.python.org/packages/source/d/pretty_numbers-%s.tar.gz?raw=true' % (version),
    platforms='Cross-platform',
    classifiers=[
      'Programming Language :: Python',
      'Programming Language :: Python :: 3'
    ],
)
