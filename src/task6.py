#!/usr/bin/env python3

from collections import namedtuple

Nil = namedtuple('Nil', ())
Cons = namedtuple('Cons', ('car', 'cdr'))

def null(lst):
    pass

def fromseq(seq):
    pass

def head(lst):
    pass

def tail(lst):
    pass

def foldr(func, acc, lst):
    pass

def foldl(func, acc, lst):
    pass

def length(lst):
    pass

def tolist(lst):
    pass

def map_(func, lst):
    pass

def append(lst1, lst2):
    pass

def filter_(pred, lst):
    pass

def reverse(lst):
    pass

def elem(value, lst):
    pass

if __name__ == '__main__':
