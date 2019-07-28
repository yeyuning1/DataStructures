'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。
'''


def majorityElement(nums):
    l1 = list(str(nums))
    for num in set(l1):
        if l1.count(num) > len(str(nums)) / 2:
            return int(num)

