from My_Array import Array

DEFAULT_CAPACITY = 5  # 创建数组的默认容量
logicalSize = 0  # 逻辑大小
a = Array(DEFAULT_CAPACITY)

"""python列表中调整数组物理大小内存的原理"""
# 增加数组的物理大小
if logicalSize == len(a):  # 当数组的物理大小等于逻辑大小
    temp = Array(len(a) + 1)
    for i in range(logicalSize):
        temp[i] = a[i]
    a = temp
# 创建一个新的更大的数组对象，把旧的数组中的数据复制到新的数组中，将旧的数组替换

# 减少数组的物理大小
if logicalSize <= len(a) // 4 and len(a) >= DEFAULT_CAPACITY * 2:  # 数组的逻辑大小小于物理大小的四分之一且大于默认容量的二倍
    temp = Array(len(a) // 2)
    for i in range(logicalSize):
        temp[i] = a[i]
    a = temp
# 创建一个新的更小的数组对象，把旧的数组中的数据复制到新的数组中，将旧的数组替换

# insert/向数组中插入一项
targetIndex = 2  # 插入目标索引
newItem = 1
# 判断数组的物理大小是否满足要求
# 将数组中的每一项都往后赋值，直到到达目标索引项为止
for i in range(logicalSize, targetIndex, -1):
    a[i] = a[i - 1]
# 使用新获得的数据替换目标索引处的值,逻辑大小+1
a[targetIndex] = newItem
logicalSize += 1

# pop/remove/del/从数组中删除一项
for i in range(targetIndex, logicalSize - 1):  # 从删除位置开始讲后续值上移
    a[i] = a[i + 1]

logicalSize -= 1  # 将逻辑大小减一
