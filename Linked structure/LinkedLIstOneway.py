from Node import Node
class LinkedLIstOneway(object):
    def __init__(self, node=None):
        self.__head = node
    
    def __len__(self):
        # 游标，用来遍历列表
        cur = self.__head
        # 记录遍历次数
        count = 0
        # 当前节点为None则说明已经遍历完毕
        while cur:
            count += 1
            cur = cur.next
        return count
    
    def is_empty(self):
        # 头节点不为None则不为空
        return self.__head == None
    
    
