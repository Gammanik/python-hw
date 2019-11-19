
def implicit_int(cls):
    new_cls = cls

    def deco(s, item):
        return 0

    method = getattr(cls, "__getattr__", None)
    if callable(method):
        return cls

    new_cls.__getattr__ = deco

    return new_cls
