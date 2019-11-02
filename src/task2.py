

class Logger:

    def __init__(self):
        self.logs = []

    def __getattribute__(self, item):
        logs = object.__getattribute__(self, "logs")
        logs.append(item)
        return object.__getattribute__(self, item)

    def m1(self):
        return 0

    def m2(self):
        return 1

    def __str__(self):
        return str(self.logs)


if __name__ == '__main__':
    lg = Logger()
    # print(dir(l))
    lg.m1()
    lg.m2()
    print(lg.m1())
    print(lg)

