for num in range(2, 101):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break;
    if flag == True: 
        print(num, end=' ')
