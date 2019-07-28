'''
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.
 (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)
学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。

请你返回至少有多少个学生没有站在正确位置数量。该人数指的是：能让所有学生以 非递减 高度排列的必要移动人数。
'''
class height(object):
    def heightChecker(self, myList):
        """
        :type heights: List[int]
        :rtype: int
        """
        newList = sorted(myList)
        ret = 0
        for i in range(len(myList)):
            if myList[i] != newList[i]:
                ret += 1
        return ret


a = [1, 2, 3, 6, 5, 7, 10, 9, 8]
c = height()
print(c.heightChecker(a))