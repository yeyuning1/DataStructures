def back_str(num):
    j = 0
    count = len(num) // 2
    for i in range(count):
        if num[i] == num[-(i+1)]:
            j += 1
        else:
            break
    if j == count:
        print(f'{num}是回文数')
    else:
        print(f'{num}不是回文数')
