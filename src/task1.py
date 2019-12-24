from functools import wraps


unfinished = list()


def deco(f):
    @wraps(f)
    def inner(*args, **kwargs):
        # print("bef: ", list(map(lambda ls: ls[2], Dictator.cls_inst)), f.__name__)
        num_before = len(Dictator.cls_inst)
        unfinished.append((num_before, f, args[0]))
        val = f(*args, **kwargs)
        num_after = len(Dictator.cls_inst)
        # print("after: ", list(map(lambda ls: ls[2], Dictator.cls_inst)), f.__name__)
        # print("unfin: ", unfinished[-1][2])

        was_before = unfinished[-1][0]
        unfinished.pop()


        if num_after > was_before:
            slf = args[0]
            for i in range(0, len(Dictator.cls_inst)):
                if slf.id == Dictator.cls_inst[i][2]:
                    pass
                    # Dictator.cls_inst[unfinished[-1][2].id][1].append("-> %s.%s" % (slf.__class__.__name__, f.__name__))
                    # Dictator.cls_inst[i][1].append("-> %s.%s" % (slf.__class__.__name__, f.__name__))
        return val

    return inner


class Dictator(type):
    curr_id = 0
    cls_inst = list()

    def show_log(cls=None):
        if not cls:
            yield from map(lambda ls: " ".join(ls[1]), Dictator.cls_inst)
        else:
            if not isinstance(cls, Dictator):
                raise TypeError("class %s should be a metaclass of %s" % (cls.__name__, Dictator.__name__))

            yield from [" ".join(x[1]) for x in list(filter(lambda obj: obj[0].__class__ == cls, Dictator.cls_inst))]


    @staticmethod
    def clear_log():
        Dictator.cls_inst.clear()

    def __new__(mcs, name, bases, attrs):
        # print("new %s %s" % (mcs.__name__, name))

        for key, item in attrs.items():
            if callable(item):
                attrs[key] = deco(attrs[key])
                # attrs[key].class_name = name
            if key == '__init__':
                print('__init: ')
                attrs[key] = deco(attrs[key])

        cls = super().__new__(mcs, name, bases, attrs)
        # cls.id = Dictator.curr_id
        return cls

    def __call__(cls, *args, **kwargs):
        Dictator.curr_id += 1
        # print("call %s %s id:%s" % (cls.__name__, args, Dictator.curr_id))
        obj = super().__call__(*args, **kwargs)
        obj.id = Dictator.curr_id

        lst_rep = list()
        lst_rep.append("id:%s" % Dictator.curr_id)
        lst_rep.append(str(obj))
        # str_rep = " ".join(lst_rep)
        str_rep = lst_rep

        Dictator.cls_inst.append((obj, str_rep, Dictator.curr_id))
        return obj


# class A(metaclass=Dictator):
#     pass
#
#
# class B(metaclass=Dictator):
#     pass


if __name__ == "__main__":
    # print('*'*60)
    # a = A()
    # aa = A()
    # b = B()
    #
    # for log in Dictator.show_log(A):
    #     print(log)

    Dictator.clear_log()

    class A(metaclass=Dictator):
        def __init__(self, x):
            print(x)


    class B(metaclass=Dictator):
        def foo(self, y):
            tmp = A(y)

        def bar(self):
            self.foo(3)


    b = B()
    print('b id: ', b.id)
    b.bar()

    for log in Dictator.show_log():
        print(log)

    # Dictator.clear_log()
    #
    #
    # class A(metaclass=Dictator):
    #     def __init__(self, b):
    #         b.bar()
    #
    #
    # class B(metaclass=Dictator):
    #     def foo(self, y):
    #         tmp = C()
    #
    #     def bar(self):
    #         self.foo(3)
    #
    #
    # class C(metaclass=Dictator):
    #     pass
    #
    #
    # c = C()
    # b1 = B()
    # b2 = B()
    # a = A(b2)
    #
    # for log in Dictator.show_log():
    #     print(log)






