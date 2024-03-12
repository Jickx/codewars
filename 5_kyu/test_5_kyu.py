from .add import add
from .increment_string import increment_string
from .rot13 import rot13
from .move_zeros import move_zeros
from .approx_equals import approx_equals
from unittest import TestCase


class Test5Kyu(TestCase):

    def test_add(self):
        self.assertEqual(add(1), 1)
        self.assertEqual(add(1)(2), 3)
        self.assertEqual(add(1)(2)(3), 6)

    def test_approx_equals(self):
        a1 = [1, 2, 3]
        a2 = [4, 5, 6]

        self.assertEqual(approx_equals(a1, a2), 9)

        b1 = [10, 20, 10, 2]
        b2 = [10, 25, 5, -2]
        self.assertEqual(approx_equals(b1, b2), 16.5)

        c1 = [0, -1]
        c2 = [-1, 0]
        self.assertEqual(approx_equals(c1, c2), 1)

        d1 = [10, 10]
        d2 = [10, 10]
        self.assertEqual(approx_equals(d1, d2), 0)

    def test_incriment_string(self):
        self.assertEqual(increment_string("foo"), "foo1")
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar1"), "foobar2")
        self.assertEqual(increment_string("foobar00"), "foobar01")
        self.assertEqual(increment_string("foobar99"), "foobar100")
        self.assertEqual(increment_string("foobar099"), "foobar100")
        self.assertEqual(increment_string("fo99obar99"), "fo99obar100")
        self.assertEqual(increment_string(""), "1")

    def test_rot_13(self):
        self.assertEqual(rot13('test'), 'grfg')
        self.assertEqual(rot13('Test'), 'Grfg')
        self.assertEqual(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%')

    def test_move_zeroes(self):
        self.assertEqual(move_zeros([1, 0, 1, 2, 0, 1, 3]), [1, 1, 2, 1, 3, 0, 0])
        self.assertEqual(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        self.assertEqual(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
                         [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
