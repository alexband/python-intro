#! /usr/bin/python
# -*- coding: utf-8 -*-

class MyProperty(object):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget, self.fset, self.fdel, self.__doc__ = \
                 fget, fset, fdel, doc

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError
        self.fdel(obj)


class C(object):
    def get_x(self):
        return 1
    x = MyProperty(get_x)

if __name__ == "__main__":
    print ">>> c = C()"
    print ">>> c.x"
    c = C()
    print c.x
