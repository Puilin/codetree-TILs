n = int(input())

arr = [int(input()) for _ in range(n)]

maximum = 0; cnt = 0
for i in range(len(arr)):
    if i == 0 or arr[i] <= arr[i-1]:
        cnt = 1
        maximum = max(cnt, maximum)
        continue
    cnt += 1
    maximum = max(cnt, maximum)

print(maximum)