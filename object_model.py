#! /usr/bin/python
# -*- coding: utf-8 -*-
import traceback

class C1(object):
    """python object model test

    >>> isinstance(C1, object)
    True
    >>> type(C1)
    <type 'type'>
    >>> C1.__name__
    'C1'
    >>> C1.__module__
    '__main__'
    >>> type(C1.__dict__)
    <type 'dictproxy'>
    >>> C1.__dict__['a']
    'a'
    >>> C1.a
    'a'
    """

    a = 'a'

    def f1(self):
        return 'f1'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    #import pdb
    #pdb.set_trace()

    class C2(object): pass
    class C3(C1): pass
    class C4(C2, C1): pass

    def function1():
        print ">>> C1.__dict__['f1']"
        print C1.__dict__['f1']
        print ">>> C1.f1"
        print C1.f1
        print ">>> C1.f2 = lambda self: 'f2'"
        C1.f2 = lambda self: 'f2'
        print ">>> C1.__dict__['f2']"
        print C1.__dict__['f2']
        print ">>> C1.f2"
        print C1.f2


    # im_self is the class instance object,
    # im_func is the function object;
    # im_class is the class of im_self for bound methods or
    # the class that asked for the method for unbound methods;

    def function2():
        print ">>> C1.f1.im_class"
        print C1.f1.im_class
        print ">>> C1.f1.im_func"
        print C1.f1.im_func
        print ">>> C1.f1.im_func is C1.__dict__['f1']"
        print C1.f1.im_func is C1.__dict__['f1']


    def function3():
        print ">>> c1 = C1()"
        print ">>> class C2(object): pass"
        print ">>> c2 = C2()"
        c1 = C1()
        c2 = C2()
        print ">>> C1.__dict__['f1'](c1)"
        print C1.__dict__['f1'](c1)
        print ">>> C1.f1(c1)"
        print C1.f1(c1)
        print ">>> C1.f1(c2)"
        try:
            C1.f1(c2)
        except:
            traceback.print_exc()

    def function4():
        print ">>> class C3(C1): pass"
        print ">>> C3.a"
        print C3.a

        print ">>> C3.__dict__['a']"
        try:
            C3.__dict__['a']
        except:
            traceback.print_exc()

        print ">>> C3.__bases__"
        print C3.__bases__
        print ">>> C3.__bases__[0].a"
        print C3.__bases__[0].a

    def function5():
        print ">>> class C4(C2, C1): pass"
        print ">>> C4.a"
        print C4.a
        print ">>> C4.__bases__"
        print C4.__bases__
        print ">>> C4.__bases__[0].a"
        try:
            print C4.__bases__[0].a
        except:
            traceback.print_exc()
        print ">>> C4.__bases__[1].a"
        print C4.__bases__[1].a

    def function6():
        print ">>> c1 = C1()"
        print ">>> c1.b = 'b'"
        c1 = C1()
        c1.b = 'b'
        print ">>> c1.__dict__['b']"
        print c1.__dict__['b']
        print ">>> c1.a"
        print c1.a
        print ">>> c1.__dict__['a']"
        try:
            print c1.__dict__['a']
        except:
            traceback.print_exc()
        print ">>> C1.__dict__['a']"
        print C1.__dict__['a']
        print ">>> c1.__class__"
        print c1.__class__
        print ">>> c1.__class__.a"
        print c1.__class__.a
        


