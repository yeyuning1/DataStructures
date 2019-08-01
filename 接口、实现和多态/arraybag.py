"""
File: arraybag.py
author: yeyuning
"""
from Array_.My_Array import Array


class ArrayBag(object):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceColletion=None):
        """Sets the initial state of self, which includes the
        contents of sourceColletion, if it's present."""
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        self._size = 0
        if sourceColletion:
            for item in sourceColletion:
                self.add(item)
