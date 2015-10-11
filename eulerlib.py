"""
Library for solving euler project problems.
"""

import itertools
import math

def fib():
    """
    Fibonacci number generator
    """
    p = 1
    pp = 0
    #yield 1 
    while True:
        yield p + pp 
        p, pp = p + pp, p

def fibon(n):
    a = b = 1
    for i in xrange(n):
        yield a
        a, b = b, a + b

def digit_rotator(num):
    """
    rotates number by digits
    
    >>> list(digit_rotator(1))
    [1]

    >>> list(digit_rotator(21))
    [12, 21]
    """
    s = str(num)
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        yield int(s)

def filtered_generator(it, filter):
    """
    Wrapper for filtering generator.
    """
    while True:
        f = it.next()
        if filter(f):
            yield f

def conditioned_generator(it, func):
    """
    Wrapper for conditioning generator.
    """
    while True:
        item = it.next()
        if not func(item):
            raise StopIteration
        yield item


if __name__ == '__main__':
    import doctest
    #doctest.testmod()
    for x in fibon(10): 
        print x

    for x in range(10): print fib().next()
