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

class Interval(object):
    def __init__(self, lower):
        self._lower = lower

    def lower(self):
        return self._lower

if __name__ == '__main__':
    unittest.main()
