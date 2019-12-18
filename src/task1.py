import sys


class SuperStorer(type):
    cls_list = {}
    cls_obj_list = list()

    def __new__(mcs, name, bases, attrs, **kwargs):
        cls_inst = super().__new__(mcs, name, bases, attrs)
        SuperStorer.cls_list[name] = cls_inst
        return cls_inst

    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        SuperStorer.cls_obj_list.append(obj)
        return obj

    @staticmethod
    def store(file):
        with open(file, "w") as f_out:
            for var in globals():
                print(var)
                data = globals()[var]
                cls_name = data.__class__.__name__

                if cls_name in SuperStorer.cls_list:
                    names = [cls_name, var]

                    for attr, value in data.__dict__.items():
                        names.append(attr)
                        names.append(str(value))
                        print(" ".join(names), file=f_out)

    @staticmethod
    def load(filename):
        with open(filename, "r") as f_in:
            for cls_vars in f_in:
                cls_name, var, *valls = cls_vars.split(" ")
                cls_obj = SuperStorer.cls_list[cls_name]()

                print("in: ", cls_obj)
                for i in range(len(valls) // 2):
                    setattr(cls_obj, valls[2 * i], int(valls[2 * i + 1]))

                # setattr(globals(), var, cls_obj)
                globals()[var] = cls_obj


if __name__ == '__main__':
    class A(metaclass=SuperStorer):
        pass


    class B(metaclass=SuperStorer):
        pass

    a = A()
    a.x = 5
    b = B()
    b.tst = 6
    c = b
    SuperStorer.store('text.txt')

    # print("instances: ", SuperStorer.cls_obj_list)

    # ##################################
    # sys.modules[__name__].__dict__.clear()

    SuperStorer.load('text.txt')
    print(a.x)
    print(c)


