#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
