n = int(input())

x = 0
temp = 0

while(n):
    n -= 1

    statement = input()

    if statement == '++X' or statement == 'X++':
        x += 1
    else:
        x -= 1

print(x)
