num = 1
while num <= 1000:
    temp = num - 1
    flag = 0
    while temp > 1:
        if num % temp == 0:
            flag = 1
            break
        temp -= 1
    if flag == 0:
        print(num)
    num += 1