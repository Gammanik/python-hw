import functools

f_list = dict()
# todo: instead of storing in global scope
# getattr(register, 'f_list')[f.__name__] = f


def register(f):
    f.visiting = False
    f_list[f.__name__] = f

    @functools.wraps(f)
    def inner(*args, **kwargs):
        return f(*args, **kwargs)

    return inner


def depends_on(list):
    def deco(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            inner.visiting = True
            
            for fun_name in list:
                # todo: instead of storing in global scope
                # func = getattr(register, "f_list")[fun_name]
                func = f_list[fun_name]

                if func.visiting:
                    raise RecursionError("circular dependency")

                func()
            return f(*args, **kwargs)

        inner.visiting = False
        f_list[inner.__name__] = inner
        return inner

    return deco



@register
def d2():
    print("call d2")


# @depends_on(["d2", "do_other_thing"])
@depends_on(["d2"])
@register
def d1():
    print("call d1")


# @depends_on(["do_other_thing"])
@register
def do_something():
    print("doing something")


@depends_on(["do_something", "d1"])
def do_other_thing():
    print("doing other thing")



if __name__ == "__main__":
    print("kkk")
    do_other_thing()
    print("----------")
    d1()
