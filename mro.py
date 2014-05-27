#! /usr/bin/python
# -*- coding: utf-8 -*-

O=object

class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
class B(D,E): pass
class A(B,C): pass

if __name__ == '__main__':

    def mro_f():
        print ">>> F.__mro__"
        print F.__mro__

    def mro_e():
        print ">>> E.__mro__"
        print E.__mro__

    def mro_d():
        print ">>> D.__mro__"
        print D.__mro__

    def mro_c():
        print ">>> C.__mro__"
        print C.__mro__

    def mro_b():
        print ">>> B.__mro__"
        print B.__mro__

    def mro_a():
        print ">>> A.__mro__"
        print A.__mro__

    print A.__mro__
