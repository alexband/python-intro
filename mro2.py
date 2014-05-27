#! /usr/bin/python
# -*- coding: utf-8 -*-

import traceback

"""
取第一个列表的头，比如[B,object] ，如果这个头(B)不在任何表的尾部，
那么将它加到线性化中，并且从合并中的列表里删除；
否则查找下一个列表的头，如果是个好的表头则取出它。
需要注意的是：表头指是第一个元素，尾部是指除表头之外的其它所有元素。
如[A,B,C,D,E,F],A是表头，[B,C,D,E,F]是尾部。
"""

O=object

class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
class B(E,D): pass
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

    def diamond_old():
        class A(): pass
        class B(A): pass
        class C(A): pass
        class D(B, C): pass
        print ">>> class A(): pass"
        print ">>> class B(A): pass"
        print ">>> class C(A): pass"
        print ">>> class A(B, C): pass"
        print ">>> C.__mro__"
        try:
            print C.__mro__
        except:
            traceback.print_exc()
        print ">>> A.__mro__"
        try:
            print D.__mro__
        except:
            traceback.print_exc()
        print ">>> Should Be "
        print "D B A C A"

    def diamond_new():
        class A(object): pass
        class B(A): pass
        class C(A): pass
        class D(B, C): pass
        print ">>> class A(object): pass"
        print ">>> class B(A): pass"
        print ">>> class C(A): pass"
        print ">>> class A(B, C): pass"
        print ">>> C.__mro__"
        print C.__mro__
        print ">>> D.__mro__"
        print D.__mro__
