n, m = map(int, input().split())

a = [0]
b = [0]

for _ in range(n):
    v, t = map(int, input().split())

    for _ in range(t):
        pos = a[-1] + v
        a.append(pos)

for _ in range(m):
    v, t = map(int, input().split())

    for _ in range(t):
        pos = b[-1] + v
        b.append(pos)

count = 0
for i in range(1, len(a)):
    if (a[i-1] >= b[i-1] and a[i] < b[i]) or (a[i-1] <= b[i-1] and a[i] > b[i]):
        count += 1

if count == 0:
    print(count)
else:
    print(count-1) # 출발점이 같기 때문에 무조건 처음에 카운트됨