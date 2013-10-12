#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class TestTddbc1(unittest.TestCase):

    def test_lower_endpoint_3_8(self):
        i = Interval(8)
        self.assertEqual(i.lower(), 8)

class Interval(object):
    def __init__(self, lower):
        pass

    def lower(self):
        return 8

if __name__ == '__main__':
    unittest.main()
