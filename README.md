[![Build Status](https://travis-ci.org/vfxGer/pretty-numbers.svg?branch=master)](https://travis-ci.org/vfxGer/pretty-numbers)
[![codecov.io](https://codecov.io/gh/vfxGer/pretty-numbers/coverage.svg?branch=master)](https://codecov.io/gh/vfxGer/pretty-numbers)
[![Code Climate](https://codeclimate.com/github/vfxGer/pretty-numbers/badges/gpa.svg)](https://codeclimate.com/github/vfxGer/pretty-numbers)
[![PYPI](https://img.shields.io/pypi/v/prettynumbers.svg)](https://pypi.python.org/pypi/prettynumbers)

Pretty Numbers
==============

Pretty Numbers is a simple Python package that displays long series of numbers in a more human readable way. 

I have used it for displaying frames of a render in a more human readable way or issues of comic books. It allows the user to quickly see what is included and what is missing.

## Installation
It is available on [PyPi](https://pypi.python.org/pypi/prettynumbers) meaning you can just:

    pip install prettynumbers 


## Usage
```python
import pretty_numbers
pretty_numbers.getPrettyTextFromNumbers([1001, 99, 1004, 1005, 1003, 1008, 
                                         1002, 1007, 1010, 1006, 1111, 1009])
```
Returns:

    "99,1001-1010,1111"

