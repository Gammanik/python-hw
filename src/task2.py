

class Multiset:

    def __init__(self):
        self.lst = []

    def __iadd__(self, *args):
        self.lst.append(args)
        return self

    def __setitem__(self, key, value):
        self.lst[key] = value

    def __getitem__(self, item):
        return self.lst[item]

    def __add__(self, other):
        self.lst.append(other)
        return self

    def __ior__(self, other):
        for i in other:
            self.lst.append(i)
        return self

    def __le__(self, other):
        cnt = 0

        for i in other:
            if i in other:
                ++cnt

        return cnt > len(self)


    def __ge__(self, other):
        pass

    def __str__(self):
        return "".join(self.lst)

    def __or__(self, other):
        for i in other:
            self.lst.append(i)
        return self

    def __and__(self, other):
        for i in other:
            if i in other and i in self:
                self.lst.append(i)
        return self

    def __iter__(self):
        print("iter: ", self.lst)

        return self.lst.sort()

    # def __sub__(self, other):
    #     return iter(self.storage.sort())


if __name__ == '__main__':
    s = Multiset()
    print(s)
    print(type(s))
    s += 1
    s += 1
    s += 2
    s += 1
    # print(list(s))  # [1, 1, 1, 2]
    s -= 1
    # print(list(s))  # [1, 1, 2]
    #
    # b = Multiset()
    # b += 1
    # b += 2
    # print(b <= s)  # True
    # print(s <= b)  # False
    #
    # print(list(s - b))  # [1]
