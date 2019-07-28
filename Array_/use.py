from My_Array import Array

a = Array(5)
print(len(a))
print(a)
for i in range(len(a)):
    a[i] = i + 1
print(a[0])
for item in a:
    print(item)
