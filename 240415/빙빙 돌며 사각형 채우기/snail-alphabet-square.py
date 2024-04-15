n, m = map(int, input().split())

arr = [
    [""] * m
    for _ in range(n)
]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def is_range(x, y):
    return 0 <= x < n and 0 <= y < m

ascii = 65
count = 1
dir_num = 0
x, y = 0, 0
arr[x][y] = chr(ascii)
while count < n*m:
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if not is_range(nx, ny) or arr[nx][ny] != "":
        dir_num = (dir_num + 1) % 4
        continue
    
    if ascii == 90:
        ascii = 64
    
    ascii += 1
    arr[nx][ny] = chr(ascii)
    count += 1
    x = nx
    y = ny

for row in arr:
    for char in row:
        print(char, end=" ")
    print("")