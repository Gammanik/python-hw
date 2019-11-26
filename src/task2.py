import inspect
from functools import wraps


def final(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func(args, kwargs)
    inner.is_final = True

    return inner


class WithFinals(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        mro = inspect.getmro(cls)

        methods = set()
        finals = set()
        all_finals = set()

        for base in mro:
            bd = base.__dict__

            for atr in bd:
                if hasattr(bd[atr], 'is_final'):
                    finals.add(atr)
                else:
                    methods.add(atr)

            if len(all_finals.intersection(finals)) > 0:
                raise LookupError("you've overriding finals: "
                                  + str(all_finals.intersection(finals)))

            all_finals = all_finals.union(finals)
            impl_finals = finals.intersection(methods)

            if len(impl_finals) > 0:
                raise LookupError("you've implemented finals: "
                                  + str(impl_finals) +
                                  " in: " + name +
                                  " from: " + base.__name__)

            finals.clear()

        super().__init__(name, bases, attrs)
