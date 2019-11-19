
def implicit_int(cls):

    def deco(s, item):
        return 0

    method = getattr(cls, "__getattr__", None)
    if not callable(method):
        cls.__getattr__ = deco
    return cls
