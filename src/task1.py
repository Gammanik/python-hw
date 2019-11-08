

class Vector:

    def __init__(self, arr):
        self.arr = arr

    def __getitem__(self, item):
        return self.arr[item]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def __len__(self):
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
        if len(self) != len(other):
            raise TypeError("can't sum Vectors of different len")

        return Vector([self[i] + other[i] for i in range(0, len(other))])

    def __sub__(self, other):
        if len(self) != len(other):
            raise TypeError("can't minus Vectors of different len")

        return Vector([self[i] - other[i] for i in range(0, len(other))])

    def __abs__(self):
        return sum([i*i for i in self])**(1/2.0)

    def __mul__(self, other):
        if isinstance(other, (int, float, complex, bool)):
            res = []
            for i in range(0, len(self)):
                res.append(other * self.arr[i])

            return Vector(res)

        if isinstance(other, Vector):
            res = 0

            if not len(self) == len(other):
                raise TypeError("can multiply only same size vectors")

            for i in range(0, len(self)):
                res += self[i] * other[i]

            return res

        else:
            raise TypeError("can multiply only to number or Vector")

    def __rmul__(self, other):
        if isinstance(other, (int, float, complex, bool)):
            res = []
            for i in range(0, len(self)):
                res.append(other * self.arr[i])

            return Vector(res)

        if isinstance(other, Vector):
            res = 0

            if not len(self) == len(other):
                raise TypeError("can multiply only same size vectors")

            for i in range(0, len(self)):
                res += self[i] * other[i]

            return res

        else:
            raise TypeError("can multiply only to number or Vector")

    def __iadd__(self, other):
        self.arr = self + other
        return self

    def __imul__(self, other):
        self.arr = self * other
        return self

    def __isub__(self, other):
        self.arr = self - other
        return self


if __name__ == '__main__':
    vec1 = Vector([1, 2, 3])
    vec1 += Vector([3, 2, 1])
    vec2 = vec1 * 3
    vec3 = 3 * vec1

    print(vec1)
    print(vec2)
    print(vec2 - vec3)

    print(abs(vec1))

    vec3[2] = 1
    print(vec3[2])

    scal = Vector([1, 2, 3]) * Vector([1, 2, 3])
    print(scal)

    a = Vector([1, 2, 3])
    b = a
    a[0] = 5
    print(b)
    a += Vector([1, 1, 1])
    print(b)
    print(a)





