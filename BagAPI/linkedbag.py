"""
File: linkedbag.py
Author； Yeyuning
"""


class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next=None):
        """Instantiates a Node with a default next of None"""
        self.data = data
        self.next = next


class LinkedBag(object):

    def __init__(self, sourceCollection=None):
        self._size = 0
        self._items = None
        self.clear()
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def clear(self):
        self.__init__()

    def __iter__(self):
        cursor = self._items
        while not cursor in None:
            yield cursor.data
            cursor = cursor.next

    def add(self, item):
        self._items = Node(item, self._items)
        self._size += 1

    def remove(self, item):
        if item not in self:
            raise KeyError(str(item) + "not in bag")
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        self._size -= 1
