def setting(str):
    return int(str) + 1000

x1, y1, x2, y2 = map(setting, input().split())
x3, y3, x4, y4 = map(setting, input().split())
x5, y5, x6, y6 = map(setting, input().split())

arr = [[0 for _ in range(2000)] for _ in range(2000)]

for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i][j] = 1

for i in range(x3, x4):
    for j in range(y3, y4):
        arr[i][j] = 1

for i in range(x5, x6):
    for j in range(y5, y6):
        arr[i][j] = 0

ans = 0
for row in arr:
    ans += sum(row)
print(ans)