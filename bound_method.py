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
        print ">>> c1 = C1()"
        c1 = C1()
        print ">>> c1.f1"
        print c1.f1
        print "'f1' in c1.__dict__"
        print 'f1' in c1.__dict__
        print ">>> c1.__class__.f1"
        print c1.__class__.f1
        print ">>> isinstance(c1, c1.__class__.f1.im_class)"
        print isinstance(c1, c1.__class__.f1.im_class)
        print ">>> c1.f1.im_class"
        print c1.f1.im_class
        print ">>> c1.f1(c1)"
        try:
            print c1.f1(c1)
        except:
            traceback.print_exc()
        # im_self is the class instance object,
        # im_func is the function object;
        # im_class is the class of im_self for bound methods
        # or the class that asked for the method for unbound methods;
        print ">>> c1.f1.im_self"
        print c1.f1.im_self
        print ">>> c1.f1.im_func"
        print c1.f1.im_func
        print ">>> c1.f1()"
        print c1.f1()
        print ">>> c1.f1.im_func(c1.f1.im_self)"
        print c1.f1.im_func(c1.f1.im_self)

        print ">>> dynamic add function to instance"
        print ">>> add to class"
        print ">>> C1.f2 = lambda self: 'f2'"
        C1.f2 = lambda self: 'f2'
        print ">>> c1.f2()"
        print c1.f2()
        print ">>> add to instance"
        print ">>> c1.f3 = lambda self: 'f3'"
        c1.f3 = lambda self: 'f3'
        try:
            c1.f3()
        except:
            traceback.print_exc()
        print ">>> c1.f3"
        print c1.f3

    def function2():
        c1 = C1()
        print ">>> type(C1.f1)"
        print type(C1.f1)
        print ">>> import types"
        import types
        print ">>> type(C1.f1) is types.MethodType"
        print type(C1.f1) is types.MethodType
        print ">>> f3 = lambda self: 'f3'"
        print ">>> m3 = types.MethodType(f3, c1, C1)"
        f3 = lambda self: 'f3'
        m3 = types.MethodType(f3, c1, C1)
        print ">>> m3"
        print m3
        print ">>> c1.f3 = m3"
        c1.f3 = m3
        print ">>> c1.f3()"
        print c1.f3()
        print ">>> c1.f4 = m3"
        c1.f4 = m3
        print ">>> c1.__dict__['f4']"
        print c1.__dict__['f4']
        print ">>> c1.f4.im_self"
        print c1.f4.im_self
