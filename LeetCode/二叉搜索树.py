l1 = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
left = 0
right = len(l1)-1
n = int(input('请输入要查找的数字'))
i = 0
while left <= right:
    midpoint = (left + right) // 2
    i += 1
    if n == l1[midpoint]:
        print(midpoint)
        break
    elif n < l1[midpoint]:
        right = midpoint - 1
    elif n > l1[midpoint]:
        left = midpoint + 1
print(i)
