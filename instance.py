#! /usr/bin/python!
# -*- coding: utf-8 -*-

"""
x = C(*args, **kwargs)
等价于
x = C.__new__(C, *args, **kwargs)
if isinstance(x, C)
    type(x).__init__(x, *args, **kwargs)
"""

class Singleton(object):
    _singletons = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._singletons:
            cls._singletons[cls] = \
              super(Singleton, cls).__new__(
                             cls, *args, **kwargs)
        return cls._singletons[cls]
