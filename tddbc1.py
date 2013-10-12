#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestInterval(unittest.TestCase):

    def test_lower_endpoint(self):
        with self.assertRaises(TypeError):
            Interval()

    def test_lower_endpoint_8(self):
        with self.assertRaises(TypeError):
            Interval(8)

    def test_lower_endpoint_4_9(self):
        i = Interval(4, 9)
        self.assertEqual(i.lower(), 4)
        self.assertEqual(i.upper(), 9)

    def test_lower_endpoint_3_8(self):
        i = Interval(3, 8)
        self.assertEqual(i.lower(), 3)
        self.assertEqual(i.upper(), 8)

    def test_lower_endpoint_9_4(self):
        with self.assertRaises(TypeError):
            Interval(9, 4)

    def test_lower_endpoint_8_3(self):
        with self.assertRaises(TypeError):
            Interval(8, 3)

    def test_string(self):
        i = Interval(3, 8)
        self.assertEquals(str(i), "[3,8]")

    def test_contains_5(self):
        i = Interval(3, 8)
        self.assertTrue(i.contains(5))

    def test_contains_1(self):
        i = Interval(3, 8)
        self.assertFalse(i.contains(1))

    def test_equals_3_8(self):
        i = Interval(3, 8)
        self.assertEquals(i, Interval(3, 8))

    def test_equals_1_6(self):
        i = Interval(3, 8)
        self.assertNotEquals(i, Interval(1, 6))


class Interval(object):

    def __init__(self, lower, upper):
        if upper < lower:
            raise TypeError

        self._lower = lower
        self._upper = upper

    def lower(self):
        return self._lower

    def upper(self):
        return self._upper

    def __str__(self):
        return "[%d,%d]" % (self._lower, self._upper)

    def contains(self, value):
        if self._lower <= value <= self._upper:
            return True
        else:
            return False

    def __eq__(self, closedinterval):
        if (self._lower == closedinterval.lower() and
                self._upper == closedinterval.upper()):
            return True
        else:
            return False


if __name__ == '__main__':
    unittest.main()
