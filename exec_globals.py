#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
>>> class C(object):
...     a = 1
...     def __init__(self, b):
...         self.b = b
>>> d = {}
>>> exec """
... a = 1
... def __init__(self, b):
...     self.b = b
... """ in globals(), d
>>> C = type('C', (object,), d)
"""
