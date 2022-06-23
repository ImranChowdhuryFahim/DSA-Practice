n = int(input())
arr = list(map(int, input().split()))
hard = False
for i in range(n):
    if arr[i] == 1:
        hard = True
        break
if hard:
    print("HARD")
else:
    print("EASY")
