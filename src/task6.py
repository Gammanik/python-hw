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
    if lst == Nil():
        return acc
    else:
        return func(head(lst), foldr(func, acc, tail(lst)))


def foldl(func, acc, lst):
    if lst == Nil():
        return acc
    else:
        return func(foldl(func, acc, tail(lst)), head(lst))


def length(lst):
    if lst == Nil():
        return 0
    else:
        return 1 + length(tail(lst))


# using '+' because I want to make it immutable
def tolist(lst):
    if lst == Nil():
        return []
    else:
        return [head(lst)] + tolist(tail(lst))


def map_(func, lst):
    if lst == Nil():
        return Nil()
    else:
        return Cons(func(head(lst)), map_(func, tail(lst)))


def append(lst1, lst2):
    if lst1 == Nil():
        return lst2
    else:
        return Cons(head(lst1), append(tail(lst1), lst2))


def filter_(pred, lst):
    if lst == Nil():
        return Nil()

    if pred(head(lst)):
        return Cons(head(lst), filter_(pred, tail(lst)))
    else:
        return filter_(pred, tail(lst))


def reverse(lst):
    if lst == Nil():
        return Nil()
    else:
        return append(reverse(tail(lst)), Cons(head(lst), Nil()))


def elem(value, lst):
    if lst == Nil():
        return False

    if head(lst) == value:
        return True
    else:
        return elem(value, tail(lst))


if __name__ == '__main__':
    pass
