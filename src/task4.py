
class Wrapper:
    def __init__(self, obj):
        self.obj = obj
        self.deleted = set()

    def __getattr__(self, item):
        if item in self.deleted:
            raise AttributeError(
                'you''ve deleted the attribute', item)

        return getattr(self.obj, item)

    def __delattr__(self, key):
        if key in self.deleted:
            raise AttributeError(
                'you''ve already deleted the attribute: ', key)

        if key in self.__dict__:
            super().__delattr__(key)

        self.deleted.add(key)


class View(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        def view(slf):
            return Wrapper(slf)

        attrs['view'] = view
        return super().__new__(mcs, name, bases, attrs)
