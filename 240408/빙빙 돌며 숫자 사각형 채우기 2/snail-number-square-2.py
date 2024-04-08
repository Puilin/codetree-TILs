n, m = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

arr = [
    [0] * m
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

x, y = 0, 0
arr[x][y] = 1
dir_num = 0
count = 1
while count < n*m:
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        continue
    
    arr[nx][ny] = arr[x][y] + 1
    count += 1

    x = nx
    y = ny

for row in arr:
    for item in row:
        print(item, end=" ")
    print()