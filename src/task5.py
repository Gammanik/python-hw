
def context_decorator(cls):
    def new_call(self, func):
        def helper():
            with self:
                return func()

        return helper

    cls.__call__ = new_call
    return cls
