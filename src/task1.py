import inspect
import io
import sys
import traceback
from contextlib import redirect_stdout, redirect_stderr
from functools import wraps


def test(f):
    @wraps(f)
    def inner(*args, **kwargs):
        return f(*args, **kwargs)

    inner._is_testing = True
    return inner


def tst_class(cls):
    if not isinstance(cls, UnitTest):
        raise TypeError("class should be an instance on UnitTest")

    stdout = list()
    is_failed = False

    for el in cls.__dict__:
        if hasattr(cls.__dict__[el], "_is_testing"):
            with io.StringIO() as buf, redirect_stdout(buf), redirect_stderr(buf):
                print('-' * 60)

                try:
                    f = cls.__dict__[el]
                    f(cls.instance)
                    stdout.append(buf.getvalue())
                except AssertionError:
                    traceback.print_exc(file=sys.stdout)
                    stdout.append(buf.getvalue())
                    is_failed = True
                except Exception:
                    pass
    if is_failed:
        print('<class ''__main__ %s ''>: F.' % cls.__name__)
    else:
        print('<class ''__main__ %s ''>: .' % cls.__name__)

    print("".join(stdout))


class UnitTest(type):
    childs = list()

    def run_tests(cls = None):
        # for an exact class
        if cls:
            tst_class(cls)
        else:
            print("all")
            for cl in UnitTest.childs:
                tst_class(cl)

    def __init__(cls, *args, **kwargs):
        UnitTest.childs.append(cls)
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        cls.instance = obj
        return obj


class A(metaclass=UnitTest):

    def __init__(self, val):
        self.val = val

    @test
    def func1(self):
        print("Func 1 is called")
        assert 2 == 3
        print("Func 1 prints nothing after assertion")

    @test
    def func2(self):
        print("Func 2 is called")
        assert 5 == 5
        print("Func 2 after assertion")

    def func3(self):
        return True

    @test
    def foo(self):
        # здесь self -- последний созданный инстанс
        # соответственно, эта проверка должна проходить для кода ниже
        print("foo from A")
        assert self.val == 43


class B(metaclass=UnitTest):
    @test
    def b_func2(self):
        print("Func 2 is called")
        assert 5 == 5
        print("Func 2 after assertion")

#
# class C(metaclass=UnitTest, set_up="create_a", tear_down="do_nothing"):
#     def __init__(self, val):
#         self.val = val
#
#     @staticmethod
#     def create_a():
#         # создает объект, к которому будут применены тестовые методы
#         return A(42)
#
#     @staticmethod
#     def do_nothing(obj):
#         # *** тихонько освобождает obj ***
#         pass
#
#     @test
#     def foo(self):
#         # здесь self -- инстанс, который был создан с помощью create_a перед запуском тестов;
#         # соответственно, эта проверка должна проходить
#         assert self.val == 42


if __name__ == "__main__":
    print('*' * 50)

    A(42)
    A(43)
    UnitTest.run_tests()
    

