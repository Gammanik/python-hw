import inspect
from functools import wraps

unfinished = list()


def public(f):
    if hasattr(f, "is_encapsulated"):
        raise SyntaxError("tho decorators on fun: %s" % f.__name__)

    f.is_encapsulated = True
    f.is_public = True
    return f


def private(f):
    if hasattr(f, "is_encapsulated"):
        raise SyntaxError("tho decorators on fun: %s" % f.__name__)

    f.is_encapsulated = True
    f.is_private = True
    return f


def protected(f):
    if hasattr(f, "is_encapsulated"):
        raise SyntaxError("tho decorators on fun: %s" % f.__name__)

    f._is_encapsulated = True
    f.is_protected = True
    return f


def call_private(f):
    @wraps(f)
    def inner(*args, **kwargs):
        stack = inspect.stack()
        caller_name = stack[1][3]

        if hasattr(f, "is_private") or hasattr(f, "is_protected"):
            if len(unfinished) == 0:
                raise TypeError("protected method %s could not be called from here"
                          % f.__name__)

            lst_unfin = unfinished[-1]
            if lst_unfin.__name__ != caller_name or lst_unfin.cls_name != f.cls_name:
                raise TypeError("protected method %s could not be called from here"
                          % f.__name__)

        unfinished.append(f)
        res = f(*args, **kwargs)
        unfinished.pop()

        return res

    inner.__name__ = f.__name__
    return inner


class Encapsulator(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        for atr in attrs:
            if callable(attrs[atr]):
                attrs[atr].cls_name = name
                attrs[atr] = call_private(attrs[atr])

        return super().__new__(mcs, name, bases, attrs)
