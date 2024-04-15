n = int(input())

arr = [
    [0] * n
    for _ in range(n)
]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

dir_num = 0
x, y = n//2, n//2
arr[x][y] = 1
count = 1

while count < n*n:
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if not is_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        continue
    
    arr[nx][ny] = arr[x][y] + 1
    count += 1
    x = nx
    y = ny

for row in arr:
    for num in row:
        print(num, end=" ")
    print("")