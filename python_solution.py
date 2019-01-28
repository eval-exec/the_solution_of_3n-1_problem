n = int(input('please input a integrat number:'))
count = 0
while n != 1:
    print(n, end=' ')
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n = n // 2

    count += 1
print('1')
print('count = ',count)



