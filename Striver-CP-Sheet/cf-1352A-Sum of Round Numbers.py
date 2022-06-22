from math import remainder


t = int(input())


while(t):
    t -= 1

    n = int(input())

    l = []

    mul = 1
    while(n):

        rem = n % 10

        if rem != 0:
            l.append(rem*mul)

        n = n//10
        mul *= 10
    print(len(l))
    for i in l:
        print(i, end=' ')
    print()
