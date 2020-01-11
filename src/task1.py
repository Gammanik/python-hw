from functools import wraps

unfinished = list()


def deco(f):
    @wraps(f)
    def inner(self, *args, **kwargs):
        _id = self.id if f.__name__ != '__init__' else self.last_id + 1
        unfinished.append((self, f'{f.__name__}', _id))
        val = f(self, *args, **kwargs)
        unfinished.pop()
        return val
    return inner


def cls_log(cls):
    for pair in cls.instances:
        inst = pair[0]
        str_rep = f"{inst.__class__.__name__}.id{inst.id}: {inst}"
        if pair[1]:
            str_rep += f' | {pair[1]}'
        yield str_rep


class Dictator(type):
    reg_cls = {}

    @staticmethod
    def show_log(cls=None):
        if cls:
            yield from cls_log(cls)
        else:
            for reg_cls in Dictator.reg_cls:
                yield from cls_log(reg_cls)

    @staticmethod
    def clear_log(cls=None):
        if cls:
            del Dictator.reg_cls[cls]
            del cls.instances
        else:
            for _c in Dictator.reg_cls:
                del _c.instances
            Dictator.reg_cls.clear()

    def __new__(mcs, name, bases, attrs, **kwargs):
        for k, fun in attrs.items():
            if callable(fun):
                attrs[k] = deco(attrs[k])

        cls = super().__new__(mcs, name, bases, attrs)
        cls.last_id = 0
        cls.instances = []
        return cls

    def __call__(cls, *args, **kwargs):
        inst = super().__call__(*args, **kwargs)
        cls.last_id += 1
        inst.id = cls.last_id
        str_unfin = " -> ".join(map(lambda p: f'{p[0].__class__.__name__}.id{p[2]}.{p[1]}', unfinished))
        cls.instances.append((inst, None if not len(str_unfin) else str_unfin))
        Dictator.reg_cls[cls] = cls
        return inst
