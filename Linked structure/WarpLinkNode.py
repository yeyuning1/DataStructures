class Node(object):
    """链表节点实现"""

    def __init__(self, item):
        """创建一个节点"""
        self.pre = None
        self.next = None
        self.item = item


class WarpLinkNode(object):
    """双向列表的实现"""

    def __init__(self):
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def __len__(self):
        """链表长度"""
        length = 0
        if not self.__head:
            return 0
        cur = self.__head
        while cur.next is not None:
            length += 1
            cur = cur.next
        return length

    def travel(self):
        """遍历列表"""
        cur = self.__head
        while cur.next != None:
            print(cur.item)
            cur = cur.next
        print("")

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        node.pre = cur

    def add(self, item):
        """链表的头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        cur = self.__head
        cur.pre = node
        node.next = cur

    def delete(self, item):
        """链表中删除对应元素"""
        if self.is_empty():
            return '空链表'
        cur = self.__head
        while cur.next is not None:
            if cur.item == item:
                cur.pre.next = cur.next.pre
                return
            cur = cur.next
        return '目标元素不存在'
