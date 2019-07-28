# l1 = [x * x for x in range(10)]
generator = (x * x for x in range(10))
for i in generator:
    print(i, end='')
