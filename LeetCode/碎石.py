class Solution(object):
    def break_stone(self, l1):
        l1.sort()
        for i in range(len(l1)):
            if len(l1) > 1:
                l1.append(l1.pop(len(l1)-1)-l1.pop(len(l1)-2))
                l1.sort()
            else:
                break
        a = l1.pop()
        return a


b = Solution()
print(b.break_stone([1, 2, 3, 3]))