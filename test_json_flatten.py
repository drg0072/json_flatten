#!/usr/bin/env python
# -*- coding: utf-8 -*-

import doctest


if __name__ == '__main__':
  from json_flatten import flatten, unflatten
  doctest.run_docstring_examples(flatten, globals(), True, __name__)
  doctest.run_docstring_examples(unflatten, globals(), True, __name__)
