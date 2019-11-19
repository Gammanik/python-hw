
def context_decorator(cls):
    def new_call(self, func):
        def helper(*agrs, **kwargs):
            with self:
                return func(*agrs, **kwargs)

        return helper

    cls.__call__ = new_call
    return cls
