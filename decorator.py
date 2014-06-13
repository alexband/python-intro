#! /usr/bin/python
# -*- coding: utf-8 -*-


#simple deco

def simple_deco(func):
    def _(*args, **kwargs):
        print "before"
        retval = func(*args, **kwargs)
        print "after"
        return retval
    return _

#deco with parameters

def para_deco(s):
    def deco(func):
        def _(*args, **kwargs):
            print "this function is decorated by %s" % s
            return func(*args, **kwargs)
        return _
    return deco

# callable object as decorator

class MyDeco(object):
    def __init__(self, s):
        self.s = s

    def __call__(self, func):
        def _(*args, **kwargs):
            print "this function is decorated by %s" % self.s
            return func(*args, **kwargs)
        return _


# functools.wraps

from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print "Calling decorated function"
        return f(*args, **kwargs)
    return wrapper

# class decorator
def register(kind, kind_name):
    def deco(cls):
        register.registry[kind] = cls
        register.registry[kind_name] = cls
        return cls
    return deco
register.registry = {}

@register(kind=K_VOTE, kind_Name='vote')
class Vote(Commentable):
    pass
