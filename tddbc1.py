#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class TestTddbc1(unittest.TestCase):

    def test_lower_endpoint_8(self):
        i = Interval(8)
        self.assertEqual(i.lower(), 8)

    def test_lower_endpoint_9(self):
        i = Interval(9)
        self.assertEqual(i.lower(), 9)

    def test_lower_endpoint_8_3(self):
        i = Interval(8, 3)
        self.assertEqual(i.lower(), 8)
        self.assertEqual(i.upper(), 3)

class Interval(object):
    def __init__(self, lower, upper=None):
        self._lower = lower
        self._upper = upper

    def lower(self):
        return self._lower

    def upper(self):
        return self._upper

if __name__ == '__main__':
    unittest.main()
