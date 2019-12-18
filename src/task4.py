from functools import wraps

apply_dc = {}


def apply(func, predicate):
    @wraps(func)
    def deco(decorated):
        fname = func.__name__

        if fname not in apply_dc:
            apply_dc[fname] = list()

        apply_dc[fname].append((decorated, predicate))

    return deco


def register(f):
    @wraps(f)
    def inner(*args, **kwargs):
        # print("inside inner: ", f)
        fname = f.__name__

        if fname not in apply_dc:
            return f(*args, **kwargs)

        f_list = apply_dc[fname]
        # print("lst: ", f_list)

        for decorated in f_list:
            # print("deco: ", decorated[1](*args, **kwargs))

            if decorated[1](*args, **kwargs):
                return decorated[0](*args, **kwargs)

        return f(*args, **kwargs)

    return inner


def pred1(num):
    return (num > 0) and (num % 2 == 1)


def pred2(num):
    return num >= 3


@register
def foo(num):
    print("Original")


@apply(foo, pred2)
def bbb(num):
    print("Magic")


@apply(foo, pred1)
def asd(num):
    print("Modified")


"""
Если вызывается функция func, "зарегистрированная" с помощью register, 
от какого-то набора параметров, 
то нужно найти первую продекорированную apply функцию, 
у которой в качестве первого
параметра apply указан func и для которой соответствующий
predicate для данного набора параметров вернет true.

"""


if __name__ == '__main__':
    print('*'*60)

    # print(apply_dc)
    # print("app: ", foo(-1))
    # print("orig: ", foo)

    foo(-1)
    foo(1)
    foo(2)
    foo(3)

