n, m = map(int, input().split())

arr_a = [0]
arr_b = [0]
for _ in range(n):
    t, d = input().split()

    for _ in range(int(t)):
        if d == 'L':
            pos = arr_a[-1] - 1
            arr_a.append(pos)
        elif d == 'R':
            pos = arr_a[-1] + 1
            arr_a.append(pos)

for _ in range(m):
    t, d = input().split()

    for _ in range(int(t)):
        if d == 'L':
            pos = arr_b[-1] - 1
            arr_b.append(pos)
        elif d == 'R':
            pos = arr_b[-1] + 1
            arr_b.append(pos)

count = 0
for i in range(1, max(len(arr_a), len(arr_b))):
    if i >= len(arr_a):
        if arr_a[-1] != arr_b[i-1] and arr_a[-1] == arr_b[i]:
            count += 1
    elif i >= len(arr_b):
        if arr_b[-1] != arr_a[i-1] and arr_b[-1] == arr_a[i]:
            count += 1
    else:
        if arr_a[i-1] != arr_b[i-1] and arr_a[i] == arr_b[i]:
            count += 1
print(count)