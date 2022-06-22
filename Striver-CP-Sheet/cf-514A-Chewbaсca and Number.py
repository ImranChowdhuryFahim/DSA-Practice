x = list(input())

for i in range(len(x)):
    val = ord(x[i])-ord('0')
    if val >= 5:
        if i == 0 and val == 9:
            continue
        x[i] = str(9-val)

print(''.join(x))
