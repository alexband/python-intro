#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
create a class

type(name, bases, attribs):
    name: string, C.__name__
    bases: tuple, C.__bases__
    attribs: dict, C.__dict__

class C(object): pass =>

C = type('C', (object,), {})

"""

class Ugly(object): pass

class MetaPretty(type):
    def __repr__(cls):
        return "I'm the class %s" % cls.__name__

class Pretty(object):
    __metaclass__ = MetaPretty

if __name__ == "__main__":
    print ">>> type(object) is type"
    print type(object) is type
    print ">>> type(type) is type"
    print type(type) is type
    print ">>> isinstance(type, object)"
    print isinstance(type, object)
    print ">>> isinstance(object, type)"
    print isinstance(object, type)
    print ">>> isinstance(type, type)"
    print isinstance(type, type)
    print ">>> isinstance(object, object)"
    print isinstance(object, object)
    print ">>> issubclass(type, object)"
    print issubclass(type, object)
    print ">>> issubclass(object, type)"
    print issubclass(object, type)
