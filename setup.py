# based on https://github.com/pypa/sampleproject/blob/master/setup.py
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

version = "0.2.1"

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="prettynumbers",
    version=version,
    description="Display a range of numbers in a human readable way",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Gerard Keating",
    author_email="gerardk@gmail.com",
    license="GNU GENERAL PUBLIC LICENSE",
    url="https://github.com/vfxGer/pretty-numbers",
    py_modules=["pretty_numbers"],
    download_url=f"https://pypi.python.org/packages/"
    f"source/d/"
    f"pretty_numbers-{version}.tar.gz?raw=true",
    platforms="Cross-platform",
    classifiers=["Programming Language :: Python :: 3"],
    package_data={"prettynumbers": ["py.typed"]},
)
