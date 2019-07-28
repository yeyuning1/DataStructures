class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None  # 初始设置下一节点为空


'''
上面定义了一个节点的类，当然可以直接使用python的结构，例如元组(elem, None)
'''


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):  # 使用一个默认参数，在传入头节点时则接收，在没有传入时，就默认头节点为空
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur游标， 用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('\n')

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        # 由于特殊情况当链表为空时没有next， 所有在前面做个判断
        if self.is_empty():
            self.__head = Node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            # 如果pos位置在0或者以前， 当措施头插法
            self.add(item)
        elif pos > self.length() - 1:
            # 如果pos位置比原链表长， 当作尾插法
            self.append(item)
        else:
            per = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                per = per.next
            # 当循环推出后， pre指向pos-1位置
            node = Node(item)
            node.next = per.next
            per.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                # 先判断节点是否为头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
            return False


if __name__ == '__main__':
    node = Node(100)

    ll = SingleLinkList(node)
    print(ll.is_empty())
    print(ll.length())
    ll.add(1)
    ll.append(3)
    ll.add(4)
    ll.insert(-2, 111)
    ll.travel()
    ll.remove(4)
    ll.travel()
    print(ll.search(111))
