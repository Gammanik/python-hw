import inspect
from functools import wraps


class Logger:

    def logs_deco(self, method):
        @wraps(method)
        def inner(*args, **kwargs):
            full_args = inspect.getcallargs(method, *args, **kwargs)
            del full_args[inspect.getfullargspec(method).args[0]]
            self.logs.append((method.__name__, full_args))

        return inner

    def __init__(self):
        self.logs = []

    def __getattribute__(self, item):
        # logs = object.__getattribute__(self, "logs")
        method = super().__getattribute__(item)

        # print()
        # args = inspect.getargvalues(method)

        deco = object.__getattribute__(self, 'logs_deco')
        if inspect.ismethod(method):
            return deco(method)
            # logs.append("item: ", args)

        return object.__getattribute__(self, item)

    def m1(self):
        return 0

    def m2(self, a, b):
        return 1

    def __str__(self):
        return str(self.logs)


if __name__ == '__main__':
    lg = Logger()
    # print(dir(l))
    lg.m1()
    lg.m2(10, 20)
    print(lg.m1())
    print(lg)

