#! /usr/bin/python
# -*- coding: utf-8 -*-

"""

A new style object containing the following methods

__get__(self, instance, owner_class)
__set__(self, instance, value)
__delete__(self, instance)

This object appears in the class dictionary of
another new-style class(owner class)

The customized method will be called when the
owner class (or its instances) access the
object as attribute

Data Descriptor
  has __set__() or __delete__()
  not overridable by instance
  e.g. property

Non-Data Descriptor
  has __get__() only
  overridable by instance
  e.g. function, staticmethod, classmethod

"""

class Descriptor(object):
    def __get__(self, instance, owner):
        return 'd', instance, owner

class Owner(object):
    descriptor = Descriptor()


if __name__ == "__main__":
    print ">>> Owner.descriptor"
    print Owner.descriptor
    print ">>> owner = Owner()"
    print ">>> owner.descriptor"
    owner = Owner()
    print owner.descriptor
