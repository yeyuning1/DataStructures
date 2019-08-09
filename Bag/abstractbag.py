"""
File: abstractbag.pu
Author: yeyuning
"""


class AbstractBag(object):
    """An abstracct bag implementation."""

    def __init__(self, sourceCollection=None):
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __add__(self, other):
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

