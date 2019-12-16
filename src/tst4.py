import inspect
from functools import wraps


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
            f.__name__ = f if isinstance(f, staticmethod) or \
                              isinstance(f, classmethod) else f.__name__

            if not Encapsulator.unfinished == 0:
                raise TypeError("protected method %s could not be called from here"
                          % f.__name__)

            lst_unfin = unfinished[-1]
            if lst_unfin.__name__ != caller_name or lst_unfin.cls_name != f.cls_name:
                raise TypeError("method %s could not be called from here"
                          % f.__name__)

        Encapsulator.unfinished.append(f)
        res = f(*args, **kwargs)
        Encapsulator.unfinished.pop()

        return res

    return inner


class Encapsulator(type):
    unfinished = list()

    def __new__(mcs, name, bases, attrs, **kwargs):
        for atr in attrs:
            print(type(attrs[atr]))

            if callable(attrs[atr]) or isinstance(attrs[atr], staticmethod)\
                    or isinstance(attrs[atr], classmethod):
                print(atr)
                setattr(attrs[atr], 'cls_name', name)
                attrs[atr] = call_private(attrs[atr])

        return super().__new__(mcs, name, bases, attrs)


class A(metaclass=Encapsulator):

    @private
    @staticmethod
    def st_foo1():
        pass

    @private
    @classmethod
    def cls_foo1(cls):
        pass

    @private
    def foo1(self):
        pass


if __name__ == "__main__":

    A.st_foo1()
    a = A()
    # a.foo1()
    # a.cls_foo1()
    # a.st_foo1()


