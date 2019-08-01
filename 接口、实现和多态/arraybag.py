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

    # Accessor methods
    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def clear(self):
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        self._items[len(self)] = item
        self._size += 1

    def __iter__(self):
        """Support iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __str__(self):
        return "{" + ", ".join(map(str, self)) + "}"

    def __add__(self, other):
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    # def __contains__(self, item):
    #     """在线性搜索的情况下，contains方法的效率不一定比for循环更好，所以先不定定义
    #     in 的判断 可以在 __iter__ 中进行"""
    #     pass

    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        targetIndex = 0
        for item in self:
            if targetIndex == item:
                break
            targetIndex += 1

        for i in range(targetIndex, len(self) -1):
            self._items[i] = self._items[i + 1]

        self._size -= 1