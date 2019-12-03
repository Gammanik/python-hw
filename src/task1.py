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
    result_lst = list()

    for el in cls.__dict__:
        if hasattr(cls.__dict__[el], "_is_testing"):
            with io.StringIO() as buf, redirect_stdout(buf), redirect_stderr(buf):
                print('-' * 60)

                try:
                    f = cls.__dict__[el]
                    f(cls.instance)
                    stdout.append(buf.getvalue())
                    result_lst.append(".")
                except AssertionError:
                    traceback.print_exc(file=sys.stdout)
                    stdout.append(buf.getvalue())
                    result_lst.append("F")
                except Exception:
                    print("GOT OTHER EXCEPTION")
                    traceback.print_exc(file=sys.stdout)
                    traceback.print_exc(buf.getvalue())

    print('\n \n %s %s' % (cls, "".join(result_lst)))
    print("".join(stdout))


class UnitTest(type):
    childs = list()

    def run_tests(cls=None):
        # for an exact class
        if cls:
            if hasattr(cls, "_set_up"):
                inst = getattr(cls, "_set_up")()
                tst_class(type(inst))

                if hasattr(cls, "_tear_down"):
                    getattr(cls, "_tear_down")(inst)

            else:
                tst_class(cls)
        else:
            for cl in UnitTest.childs:
                tst_class(cl)

    def __new__(mcs, name, bases, attrs, set_up=None, tear_down=None):
        if set_up:
            attrs["_set_up"] = attrs[set_up]

        if tear_down:
            attrs["_tear_down"] = attrs[tear_down]

        cls = super().__new__(mcs, name, bases, attrs)
        UnitTest.childs.append(cls)
        return cls

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
        assert 5 == 6
        print("Func 2 after assertion")


class C(metaclass=UnitTest, set_up="create_a", tear_down="do_nothing"):
    def __init__(self, val):
        self.val = val

    @staticmethod
    def create_a():
        # создает объект, к которому будут применены тестовые методы
        return C(42)

    @staticmethod
    def do_nothing(obj):
        # *** тихонько освобождает obj ***
        print("tear down")
        pass

    @test
    def foo(self):
        print("C enter foo")
        # здесь self -- инстанс, который был создан с помощью create_a перед запуском тестов;
        # соответственно, эта проверка должна проходить

        assert self.val == 42

    @test
    def foo2(self):
        print("C enter foo 2")
        # здесь self -- инстанс, который был создан с помощью create_a перед запуском тестов;
        # соответственно, эта проверка должна проходить

        assert self.val == 22


if __name__ == "__main__":
    print('*' * 50)

    A(42)
    A(43)
    B()
    C(22)
    UnitTest.run_tests()
