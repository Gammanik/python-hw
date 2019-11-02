
def implicit_int(cls):
    new_cls = cls

    def deco(s, item):
        s.__dict__[item] = 0
        return 0

    new_cls.__getattr__ = deco

    return new_cls


if __name__ == '__main__':
    @implicit_int
    class A:
        def m1(self): pass


    a = A()

    print(a.e + 589)  # Вывод: 589
    print(a.m1() is None)
    print(a.dd)
