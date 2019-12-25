from functools import wraps
from timeit import default_timer


spy_list = list()


def spy(f):
    @wraps(f)
    def inner(*args, **kwargs):
        time_start = default_timer()
        spy_list.append((f.__name__, time_start, (args, kwargs)))
        val = f(*args, **kwargs)
        return val
    inner.can_spy = True
    return inner


def bond(f):
    fname = f.__name__
    if not hasattr(f, 'can_spy'):
        raise ValueError("can''t spy on %s" % fname)

    yield from map(lambda x: (x[1], x[2]), filter(lambda x: x[0] == fname, spy_list))



@spy
def foo(num):
    print(num)

@spy
def bar(any):
    pass


if __name__ == "__main__":
    print('*'*60)

    foo(30)
    foo('hello')
    foo(5)

    bar('bar_arg')

    for (time, parameters) in bond(foo):
        print(time)
        print(parameters)
