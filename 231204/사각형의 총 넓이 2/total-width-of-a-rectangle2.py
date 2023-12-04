n = int(input())

def setting(str):
    return int(str) + 100

arr = [[0 for _ in range(200)] for _ in range(200)]
for _ in range(n):
    x1, y1, x2, y2 = map(setting, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

ans = 0
for i in range(200):
    ans += sum(arr[i])
print(ans)