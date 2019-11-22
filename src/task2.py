# def final(func):
#     pass


# class WithFinals(type):
#     pass


## Setup
# class A(metaclass=WithFinals):
#     @final
#     def foo(self):
#         pass


# class X(metaclass=WithFinals):
#     @final
#     def foo(self):
#         pass


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


# 3) Fail
# class C:
#     def foo(self):
#         pass
#
#
# class B(C, A):
#     pass


# 4) Ok
# class C:
#     def foo(self):
#         pass
#
#
# class B(A, C):
#     pass


# 5) Fail
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
