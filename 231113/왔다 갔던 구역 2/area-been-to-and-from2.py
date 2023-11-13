n = int(input())

arr = [0 for _ in range(2001)]

idx = 1000
for _ in range(n):
    quantity, direction = input().split()

    if direction == "L":
        for i in range(int(quantity)):
            idx -= 1
            arr[idx] += 1
    else:
        for i in range(int(quantity)):
            arr[idx] += 1
            idx += 1

count = 0
for item in arr:
    if item >= 2:
        count += 1
print(count)