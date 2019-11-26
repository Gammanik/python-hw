import inspect


class Singleton(type):

    def __iter__(self):
        return iter(list(map(lambda x: x[1], self.__cache)))

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.__cache = list()

    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)

        sig = inspect.signature(cls.__init__)\
            .bind_partial(cls, *args, **kwargs)
        sig.apply_defaults()
        all_args = list(sig.arguments.items())

        for i in range(0, len(cls.__cache)):
            if cls.__cache[i][0] == all_args:
                return cls.__cache[i][1]

        cls.__cache.append((all_args, obj))

        return obj


