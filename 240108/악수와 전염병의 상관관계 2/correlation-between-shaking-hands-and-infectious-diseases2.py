n, k, p, T = map(int, input().split())

arr = [[0 for _ in range(251)] for _ in range(n+1)]
# [
#   1  [1, 1, 0, 0, 0, 0, 0, 0, ...],
#   2  [0, 1, 1, 0, 0, 0, 0, 0, ...],
#   3  [0, 0, 1, 1, 1, 0, 0, 0, ...],
#   4  [0, 0, 0, 1, 0, 0, 0, 0, ...],
#   5  [0, 0, 0, 0, 1, 0, 0, 0, ...],
#     ...
# ]
#최초 감염자
arr[p][0] = 1

logs = []
for _ in range(T):
    t, x, y = map(int, input().split())
    logs.append((t, x, y))

logs.sort(key=lambda x: x[0])

for log in logs:
    t, x, y = log
    # 최초 감염자
    if x == p and arr[x].count(1) < k+1:
        arr[y][t] = 1
    elif y == p and arr[y].count(1) < k+1:
        arr[x][t] = 1
    # 둘중 하나가 감염자이면서 악수를 k번보다 적게 했다면
    if (0 < arr[x].count(1) < k+1):
        arr[y][t] = 1
    if (0 < arr[y].count(1) < k+1):
        arr[x][t] = 1
        
result = []
for developer in arr:
    if developer.count(1) > 0:
        result.append(1)
    else:
        result.append(0)

for i in range(1, len(result)):
    print(result[i], end="")