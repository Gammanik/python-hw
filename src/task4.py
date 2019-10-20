import functools


def trace_if(pred):
    def deco(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            if pred(*args, **kwargs):
                print(f.__name__, args, kwargs)
            return f(*args, **kwargs)

        return inner

    return deco
