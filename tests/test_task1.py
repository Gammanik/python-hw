import unittest

try:
    from src.task1 import Vector
except ImportError as e:
    raise unittest.SkipTest("Task 1 is not complete yet")


class Task1Tests(unittest.TestCase):
    repeats = 25

    @staticmethod
    def vec_to_list(vec):
        return [vec[i] for i in range(len(vec))]

    @staticmethod
    def create_vector(*args):
        # WARN: CHANGE THIS METHOD IF YOUR VECTOR DOESN'T HAVE
        # LIST CONSTRUCTOR
        return Vector([*args])

    def test_check_index(self):
        v = self.create_vector(0, 0, 0)
        v[1] = 3
        self.assertEqual(v[1], 3)
        v[2] = 5
        self.assertEqual(v[2], 5)
        self.assertRaises(IndexError, lambda: v[3])

    def test_add(self):
        vec1 = self.create_vector(1, 2, 3)
        vec2 = self.create_vector(1, 2, 3)
        vec3 = vec1 + vec2

        vec1 += vec2
        self.assertListEqual(self.vec_to_list(vec1), [2, 4, 6])
        self.assertListEqual(self.vec_to_list(vec3), [2, 4, 6])

    def test_sub(self):
        vec1 = self.create_vector(1, 2, 3)
        vec2 = self.create_vector(1, 2, 3)
        vec3 = vec1 - vec2

        vec1 -= vec2
        self.assertListEqual(self.vec_to_list(vec1), [0, 0, 0])
        self.assertListEqual(self.vec_to_list(vec3), [0, 0, 0])

    def test_scalar_product(self):
        vec1 = self.create_vector(1, 2, 3)
        vec2 = self.create_vector(1, 2, 3)

        vec3 = vec1 * vec2
        self.assertEqual(vec3, 14)

        vec4 = vec1 * 3
        vec5 = 3 * vec1
        vec1 *= 3
        self.assertListEqual(self.vec_to_list(vec4), self.vec_to_list(vec5))
        self.assertListEqual(self.vec_to_list(vec4), self.vec_to_list(vec1))

    def test_raises_on_invalid_demensions(self):
        vec1 = self.create_vector(1, 2, 3)
        vec2 = self.create_vector(1, 2, 3, 4)

        self.assertRaises(TypeError, lambda: vec1 * vec2)
        self.assertRaises(TypeError, lambda: vec1 - vec2)
        self.assertRaises(TypeError, lambda: vec1 + vec2)

        def assign_with_sub():
            vec3 = self.create_vector(1, 2, 3)
            vec4 = self.create_vector(1, 2, 3, 4)
            vec3 -= vec4

        self.assertRaises(TypeError, assign_with_sub)

        def assign_with_add():
            vec3 = self.create_vector(1, 2, 3)
            vec4 = self.create_vector(1, 2, 3, 4)
            vec3 += vec4

        self.assertRaises(TypeError, assign_with_add)
