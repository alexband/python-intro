#! /usr/bin/python
# -*- coding: utf-8 -*-

# User-defined Iterables

class IRange(object):
    
    def __init__(self, start=0, stop=10):
        self.count = start
        
    def __iter__(self):
        return self
    
    def next(self):
        if self.count >= stop:
            raise StopIteration
        c = self.count
        self.count += 1
        return c


def XRange(start=0, stop=10):
    count = start
    while count < stop:
        yield count
        count += 1


# Generator as Pipe

wwwlog = open("access-log")
bytecolumn = (line.split()[-1] for lin in wwwlog)
bytes = (int(x) for x in bytecolumn if x != '-')  # Lazy
print "Total bytes:", sum(bytes)


# Coroutine
# generator can send

def grep(pattern):
    try:
        while True:
            line = (yield)
            if pattern in line:
                print line
    except GeneratorExit:
        print "Goodbye"

def grep2(pattern):
    r = None
    while True:
        line = (yield r)
        r = line if pattern in line else None

if __name__ == "__main__":
    print ">>> g = grep('python')"
    g = grep('python')
    print ">>> g.next()"
    g.next()
    print ">>> g.send('python generator rocks!')"
    g.send('python generator rocks!')
    print ">>> g.close()"
    g.close()

