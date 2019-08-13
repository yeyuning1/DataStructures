"""
FizzBuzz问题
"""
l1 = []
for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        l1.append('FizzBuzz')
    elif x % 3 == 0:
        l1.append('Fizz')
    elif x % 5 == 0:
        l1.append('Buzz')
    else:
        l1.append('%d' % x)
print(l1)


with open() as f:
    f.write()