m, n = map(int, input().split())

arr = []

for i in range(m):
    arr.append(list(map(int, input().split())))

ans = [[-1]*n for i in range(m)]


for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            for k in range(n):
                ans[i][k] = 0

            for k in range(m):
                ans[k][j] = 0

        else:
            for k in range(n):
                if ans[i][k] != 0:
                    ans[i][k] = 1
            for k in range(m):
                if ans[k][j] != 0:
                    ans[k][j] = 1
flag = False
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            count1 = 0
            count2 = 0
            for k in range(n):
                if ans[i][k] == 0:
                    count1 += 1

            for k in range(m):
                if ans[k][j] == 0:
                    count2 += 1
            if not(count1 == n and count2 == m):
                flag = True
                break

        else:
            count1 = 0
            count2 = 0
            for k in range(n):
                if ans[i][k] == 1:
                    count1 += 1
            for k in range(m):
                if ans[k][j] == 1:
                    count2 += 1
            if not(count1+count2 >= 1):
                flag = True
                break

if flag:
    print("NO")

else:
    print("YES")

    for i in range(m):
        for j in range(n):
            print(ans[i][j], end=' ')
        print()
