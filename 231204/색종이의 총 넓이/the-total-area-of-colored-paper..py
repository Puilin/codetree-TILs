n = int(input())

def setting(str):
    return int(str) + 100

arr = [[0 for _ in range(200)] for _ in range(200)]
for _ in range(n):
    x, y = map(setting, input().split())

    for i in range(x, x+8):
        for j in range(y, y+8):
            arr[i][j] = 1

ans = 0
for row in arr:
    ans += sum(row)
print(ans)