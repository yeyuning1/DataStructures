'''
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
请你重新排列这些条形码，使其中两个相邻的条形码不能相等。你可以返回任何满足该要求的答案，此题保证存在答案。
示例 1：
输入：[1,1,1,2,2,2]
输出：[2,1,2,1,2,1]
示例 2：
输入：[1,1,1,1,2,2,3,3]
输出：[1,3,1,3,2,1,2,1]
提示：
1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
'''

import random
def rearrange(barcodes):
    l2 = barcodes[:]
    while l2:
        l2 = barcodes[:]
        l1 = []
        l1.append(l2.pop(random.randint(0, len(l2)-1)))
        for i in range(len(l2)):
            j = random.randint(0, len(l2)-1)
            if l1[i] != l2[j]:
                l1.append(l2.pop(j))
            else:
                break
    return l1


print(rearrange([1, 1, 2, 2, 3, 3, 4, 4]))
