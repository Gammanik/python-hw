import inspect
from functools import wraps


all_private = {}


def public(f):
    f.is_public = True
    return f


def private(f):
    f.is_private = True
    return f


def protected(f):
    f.is_protected = True
    return f


def call_private(f):
    @wraps(f)
    def inner(*args, **kwargs):
        print("fun called: ", f.__name__)
        # print("stack: ", f.__name__, inspect.stack())



        stack = inspect.stack()
        f_name = stack[1][3]

        print(f_name)
        print("stack: ", stack)
        # print(inspect.getsourcelines(f))
        mem = inspect.getmembers(f)
        # print(mem.f_code)

        print()


        # if <module>
        if f_name not in all_private:
            TypeError("private method" + f_name + "could not be called from here")

        if f_name == "<module>":
            TypeError("private method" + f_name + "could not be called from here")


        if len(stack) > 1:
            pass

            # call_private(stack[1][3])

        return f(*args, **kwargs)

    inner.__name__ = f.__name__
    return inner



class Encapsulator(type):

    def __new__(mcs, name, bases, attrs, **kwargs):
        # print("__new__ attrs", attrs)

        for atr in attrs:
            val = attrs[atr]

            # if (hasattr(val, "is_private") \
            #         and (hasattr(val, "is_protected") or hasattr(val, "is_public")):
            #     raise AttributeError("shouldn't have more than 1 deco: ", atr.__name__)

            if hasattr(val, "is_private"):
                all_private[atr] = call_private(attrs[atr])
                attrs[atr] = call_private(attrs[atr])

        return super().__new__(mcs, name, bases, attrs)


class A(metaclass=Encapsulator):

    @private
    def foo_pr3(self):
        pass

    @private
    def foo_pr2(self):
        self.foo_pr3()
        pass

    @private
    def foo_pr(self):
        self.foo_pr2()
        pass

    def fooCall(self):
        self.foo_pr()


class B(A):
    pass


if __name__ == "__main__":
    print('*'*60)

    a = A()
    print(dir(a))
    # a.foo()
    a.fooCall()
    a.foo_pr3()

