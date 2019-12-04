import inspect
from functools import wraps

fun_args = dict()
fun_ret_types = dict()


def types_tracker(f):
    fun_args[f.__name__] = list()
    fun_ret_types[f.__name__] = list()

    @wraps(f)
    def inner(*args, **kwargs):
        sig = inspect.signature(f)\
            .bind_partial(*args, **kwargs)
        sig.apply_defaults()
        all_args = list(sig.arguments.items())
        dc_types = {}
        # map(lambda x: {dc_types[x[0]] = type(x[1]).__name__}, all_args)

        for k, v in all_args:
            dc_types[k] = v

        # arg_and_types = map(lambda x: {x[0], type(x[1]).__name__}, all_args)
        fun_args[f.__name__].append(dc_types)
        val = f(args, kwargs)

        if type(val) not in fun_ret_types[f.__name__]:
            fun_ret_types[f.__name__].append(type(val))

        return val

    inner._types_tracked = True
    inner.__name__ = f.__name__
    return inner


def types_info(f):
    if not hasattr(f, "_types_tracked"):
        return AttributeError("The function os not tracked")

    print("tup agrs", tuple(fun_args[f.__name__]))
    print("tup ret: ", tuple(fun_ret_types[f.__name__]))

    yield tuple(fun_args[f.__name__])
    yield tuple(fun_ret_types[f.__name__])


@types_tracker
def foo(a, b=42):
    pass

@types_tracker
def bar(a, b=42):
    if a < 42:
        return 1
    else:
        return "qwe"

@types_tracker
def id(a):
    return a


def pretty_print_types_info(func):
    for call_args_types, res_types in types_info(func):
        s = "{}({}) -> {}".format(
            func.__name__,
            ", ".join("{}={}".format(k, v.__name__)
                        for k, v in call_args_types.items()),
            " & ".join(type.__name__ for type in res_types)
        )
        print(s)


if __name__ == "__main__":

    foo(1)
    foo(2.0)
    # foo(2.0, 2.2)
    pretty_print_types_info(foo)

    print('*' * 60)

    print('all', fun_args)


