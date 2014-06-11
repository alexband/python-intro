#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
object.__getattribute__(self, name)

called unconditionally
if AttributeError raised, __getattr__() is checked
To avoid infinite recursion, user BaseClass.__getattribute__ to
access any attributes it needs
"""

from object_model import C1
c1 = C1()

class Delegator(object):
    def __init__(self, delegatee):
        super(Delegator, self).__setattr__('o', delegatee)

    def __getattribute__(self, name): # notice not __getattr__
        o = super(Delegator, self).__getattribute__('o')
        return getattr(o, name)

    def __setattr__(self, name, value):
        o = super(Delegator, self).__getattribute__('o')
        setattr(o, name, value)

    def __delattr__(self, name):
        o = super(Delegator, self).__getattribute__('o')
        delattr(self.o, name)

    
if __name__ == '__main__':
    
    def delegate():
        print ">>> d = Delegator(c1)"
        print ">>> c1.o = 2"
        print ">>> d.o"
        d = Delegator(c1)
        c1.o = 2
        print d.o
        # notice the result, because we use __getattribute__

