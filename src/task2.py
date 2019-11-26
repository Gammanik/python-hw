import inspect
from functools import wraps


def final(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func(args, kwargs)
    inner.is_final = True

    return inner


class WithFinals(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        mro = inspect.getmro(cls)

        methods = set()
        finals = set()
        all_finals = set()

        for base in mro:
            bd = base.__dict__

            for atr in bd:
                if hasattr(bd[atr], 'is_final'):
                    finals.add(atr)
                else:
                    methods.add(atr)

            if len(all_finals.intersection(finals)) > 0:
                raise LookupError("you've overriding finals: "
                                  + str(all_finals.intersection(finals)))

            all_finals = all_finals.union(finals)
            impl_finals = finals.intersection(methods)

            if len(impl_finals) > 0:
                raise LookupError("you've implemented finals: "
                                  + str(impl_finals) +
                                  " in: " + name +
                                  " from: " + base.__name__)

            finals.clear()

        super().__init__(name, bases, attrs)


# Setup
class A(metaclass=WithFinals):
    @final
    def foo(self):
        pass


class X(metaclass=WithFinals):
    @final
    def foo(self):
        pass


# Далее приведено 6 примеров использования метакласса WithFinals.
# Примеры 1, 2, 3 и 5 НЕ должны компилироваться.

# 1) Fail
# class B(A):
#     def foo(self):
#         pass


# 2) Fail
# class B(A):
#     pass
#
#
# class C(B):
#     def foo(self):
#         pass

#
# # 3) Fail
# class C:
#     def foo(self):
#         pass
#
#
# class B(C, A):
#     pass

#
# # 4) Ok
# class C:
#     def foo(self):
#         pass
#
#
# class B(A, C):
#     pass

#
# # 5) Fail
# class B(A, X):
#     pass


# 6) Ok
# class Y:
#     def foo(self):
#         pass
#
#
# class X(Y, metaclass=WithFinals):
#     @final
#     def foo(self):
#         pass
#
#
# class A(X):
#     pass
