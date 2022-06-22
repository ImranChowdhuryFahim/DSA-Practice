arr = []

for i in range(5):
    arr.append(list(map(int, input().split())))


loc_i, loc_j = -1, -1
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            loc_i = i+1
            loc_j = j+1

print(abs(loc_i-3)+abs(loc_j-3))
