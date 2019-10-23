import functools
from collections import OrderedDict
from collections import deque
from see import see
import inspect


def cached(cache_size=None):
    # we could've used a map of a fixed size also
    d = deque()

    def deco(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            print(inspect.getfullargspec(f))
            # arg_names = inspect.signature(f)

            f_spec = inspect.getfullargspec(f)
            arg_names = f_spec.args
            default_valls = f_spec.defaults

            mp = dict()
            for i in range(0, len(arg_names)):
                if i < len(args):
                    mp[arg_names[i]] = args[i]
                else:
                    mp[arg_names[i]] = default_valls[i - len(args)]

            for kw_name in kwargs:
                mp[kw_name] = kwargs[kw_name]

            # full_args = set(f.__defaults__ + args)
            # print("full_args", full_args)

            # if mp in d:

            #     return d[tuple(args)]
            #
            # else:
            #     if len(d) > cache_size and not (cache_size is None):
            #         d.popleft()

            return f(*args, **kwargs)

        return inner

    return deco


@cached(2)
def fun(a1, a2=2, a3=4, **kw):
    print("fun called")
    return 42



if __name__ == "__main__":
    fun(1)
    print("----------")
    fun(1, 1, 2, akw="v")

