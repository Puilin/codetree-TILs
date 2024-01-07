n, k, p, T = map(int, input().split())

arr = [[0 for _ in range(251)] for _ in range(n+1)]
shake_count = 0
for _ in range(T):
    t, x, y = map(int, input().split())

    # 최초 감염자이면서 악수를 k번보다 적게 했다면
    if (x == p or y == p) and shake_count < k:
        arr[x][t] = 1
        arr[y][t] = 1
        shake_count += 1
    # 둘중 하나가 감염자이면서 악수를 k번보다 적게 했다면
    elif (arr[x].count(1) > 0 or arr[y].count(1)) and shake_count < k:
        arr[x][t] = 1
        arr[y][t] = 1
        shake_count += 1
        
result = []
for developer in arr:
    if developer.count(1) > 0:
        result.append(1)
    else:
        result.append(0)

del(result[-1])

for i in result:
    print(i, end="")