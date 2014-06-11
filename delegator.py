#! /usr/bin/python
# -*- coding: utf-8 -*-

from object_model import C1
c1 = C1()

class Delegator(object):
    def __init__(self, delegatee):
        self.__dict__['o'] = delegatee

    def __getattr__(self, name):
        return getattr(self.o, name)

    def __setattr__(self, name, value):
        setattr(self.o, name, value)

    def __delattr__(self, name):
        delattr(self.o, name)

class PrivateDele(object):
    def __init__(self, delegatee):
        self.__o = delegatee

    def __getattr__(self, name):
        return getattr(self.__o, name)
    
if __name__ == '__main__':
    
    def delegate():
        print ">>> d = Delegator(c1)"
        print ">>> c1.a = 2"
        print ">>> d.a"
        d = Delegator(c1)
        c1.a = 2
        print d.a
        print ">>> c1.o = 3"
        print ">>> d.o"
        print d.o

    def pridele():
        print ">>> d = PrivateDele(c1)"
        print ">>> c1.__o = 2"
        print ">>> d.__o"
        d = PrivateDele(c1)
        c1.__o = 2
        print d.__o
        print ">>> c1._PrivateDele__o = 3"
        c1._PrivateDele__o = 3
        print ">>> d._PrivateDele__o"
        print d._PrivateDele__o
