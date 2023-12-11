def setting(string):
    return int(string) + 100

n = int(input())

arr = [[0 for _ in range(201)] for _ in range(201)]
for i in range(n):
    x1, y1, x2, y2 = map(setting, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            if i % 2 == 0: # 빨간 직사각형
                arr[x][y] = -1
            else: # 파란 직사각형
                arr[x][y] = 1

result = 0
for row in arr:
    result += row.count(1)
print(result)