n = int(input())

arr = list(map(int, input().split()))

mn = arr[0]
mni = 0
mx = arr[0]
mxi = 0

for i in range(n):
    if arr[i] <= mn:
        mn = arr[i]
        mni = i
    elif arr[i]>mx:
        mx = arr[i]
        mxi = i

if mxi > mni:
    print(mxi+n-1-mni-1)
else:
    print(mxi+n-1-mni)
