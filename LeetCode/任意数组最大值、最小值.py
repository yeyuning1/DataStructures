# 造轮子
def max_min(*args):
    for i in args:
        a = args[0]
        b = args[0]
        a = a if a > i else i
        b = b if b < i else i
    return a, b


max1, min1 = max_min(1, 3, 5, 7, 8, 11, 25, 26, 78, 91)
print(f'最大值为{max1}，最小值为{min1}')


def max_min(*arg):
    nums = args
    max_num = max(nums)
    min_num = min(nums)
    return max_num, min_num


max1, min1 = max_min(1, 3, 5, 7, 8, 11, 25, 26, 78, 91)
print(f'最大值为{max1}，最小值为{min1}')