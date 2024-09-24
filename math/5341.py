flag = True
while flag:
    n = int(input())

    if n == 0:
        flag = False
        break

    print(sum(i for i in range(n+1)))