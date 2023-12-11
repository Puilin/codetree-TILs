n, t = map(int, input().split())

arr = list(map(int, input().split()))

maximum = 0; cnt = 0
for i in range(len(arr)):
    if i == 0 or not (arr[i] > t and arr[i-1] > t):
        cnt = 1
        maximum = max(maximum, cnt)
        continue
    cnt += 1
    maximum = max(maximum, cnt)

print(maximum)