

class staticmethod:
    """
    Декорирую функции с помощью класса
    и делаю их дескрипторами, задав __get__
    из диаграммы в статье
    https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
    видно, что так как задекорированная фукнция будет дескриптором,
    то будем искать ее в словаре класса
    """

    def __init__(self, function):
        self.function = function

    def __get__(self, instance, owner):
        return self.function


class classmethod:
    pass


class C:
    @staticmethod
    def f(arg1, arg2):
        print(arg1, arg2)

    def g(self):
        print(self)


if __name__ == "__main__":
    print("_" * 50)
    print(C.f(1, 2))


