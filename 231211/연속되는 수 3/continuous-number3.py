n = int(input())

arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)

maximum = 0; cnt = 0
for i in range(len(arr)):
    if i == 0 or arr[i] * arr[i-1] < 0:
        cnt = 1
        if maximum < cnt:
            maximum = cnt
        continue
    cnt += 1
    if maximum < cnt:
        maximum = cnt

print(maximum)