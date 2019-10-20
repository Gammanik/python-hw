import functools


def n_times(times=1):
    def deco(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            for _ in range(times):
                f(*args, **kwargs)

        return inner

    return deco
