def fibonacii(n):
    if n == 1:
        num = 0
        return num
    elif n == 2:
        num = 1
        return num
    else:
        num = fibonacii(n - 2) + fibonacii(n - 1)
        return num


def print_fibonacii(n):
    for i in range(1, n + 1):
        print(fibonacii(i), end=',')


print_fibonacii(50)