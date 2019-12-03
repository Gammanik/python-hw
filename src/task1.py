import io
import sys
import traceback
from contextlib import redirect_stdout, redirect_stderr
from functools import wraps


def tests_for(cls):
    def wrapper(cls_dec):
        for i in cls_dec.__dict__:
            if i not in cls.__dict__ \
                    and hasattr(cls_dec.__dict__[i], '_is_testing'):
                setattr(cls, i, cls_dec.__dict__[i])
        return cls

    return wrapper


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


def init_tst(cls):
    if hasattr(cls, "_set_up"):
        inst = getattr(cls, "_set_up")()
        tst_class(type(inst))

        if hasattr(cls, "_tear_down"):
            getattr(cls, "_tear_down")(inst)

    else:
        tst_class(cls)


class UnitTest(type):
    childs = list()

    def run_tests(cls=None):
        # for an exact class
        if cls:
            init_tst(cls)
        else:
            for cl in UnitTest.childs:
                init_tst(cl)

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
