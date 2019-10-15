#!/usr/bin/env python3

from collections import namedtuple

Nil = namedtuple('Nil', ())
Cons = namedtuple('Cons', ('car', 'cdr'))


def null(lst):
    return lst == Nil()


def fromseq(seq):
    if len(seq) != 0:
        return Cons(car=seq[0], cdr=fromseq(seq[1:]))
    else:
        return Nil()


def head(lst):
    return getattr(lst, 'car')


def tail(lst):
    return getattr(lst, 'cdr')


def foldr(func, acc, lst):
    if head(lst) == null(lst):
        return 2



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
    pass
