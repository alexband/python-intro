#! /usr/bin/python
# -*- coding: utf-8 -*-

class Ugly(object): pass

class MetaPretty(type):
    def __repr__(cls):
        return "I'm the class %s" % cls.__name__

class Pretty(object):
    __metaclass__ = MetaPretty

#Better Singleton

class Singleton(object):
    _singletons = {}
    class __metaclass__(type):
        def __call__(cls, *args, **kwargs):
            S = Singleton
            if cls not in S._singletons:
                super_ = super(S.__metaclass__, cls)
                S._singletons[cls] = super_.__call__(*args, **kwargs)
            return S._singletons[cls]

#Enforcing Naming Rules

class MetaEnsureAttribNames(type):
    def __new__(mcl, name, bases, attrs):
        if any(a for a in attrs if not a.islower()):
            raise TypeError('invalid attribute')
        return super(MetaEnsureAttribNames,
                     mcl).__new__(mcl, name, bases, attrs)


if __name__ == "__main__":
    print ">>> Pretty"
    print repr(Pretty)
    print ">>> type(Pretty)"
    print type(Pretty)
