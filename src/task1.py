

class Vector:

    def __init__(self, arr):
        self.arr = arr

    @property
    def arr(self):
        return self.__arr

    @arr.setter
    def arr(self, val):
        self.__arr = val

    def __getitem__(self, item):
        return self.arr[item]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def get_len(self):
        return len(self.arr)

    def at(self, i):
        return self.arr[i]

    def __str__(self):
        return str(self.arr)

    def __repr__(self):
        return str(self.arr)

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, other):
        if len(self.arr) != other.get_len():
            raise ValueError("can't sum Vectors of different len")

        res = []
        for i in range(0, other.get_len()):
            res.append(self.arr[i] + other.at(i))

        return Vector(res)

    def __mul__(self, other):
        if isinstance(other, (int, float, complex, bool)):
            res = []
            for i in range(0, self.get_len()):
                res.append(other * self.arr[i])

            return Vector(res)

        if isinstance(other, Vector):
            res = 0

            if not self.get_len() == other.get_len():
                return ValueError("can multiply only same size vectors")

            for i in range(0, self.get_len()):
                res += self[i] * other[i]

            return res

        else:
            raise ValueError("can multiply only to number or Vector")

    __rmul__ = __mul__


if __name__ == '__main__':
    vec1 = Vector([1, 2, 3])
    vec1 += Vector([3, 2, 1])
    vec2 = vec1 * 3
    vec3 = 3 * vec1

    print(vec1)
    print(vec2)
    print(vec2 == vec3)

    vec3[2] = 1
    print(vec3[2])

    scal = Vector([1, 2, 3]) * Vector([1, 2, 3])
    print(scal)



