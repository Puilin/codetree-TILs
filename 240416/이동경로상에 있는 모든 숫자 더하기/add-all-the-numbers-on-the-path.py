n, t = map(int, input().split())
commands = list(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = n//2, n//2
dir_num = 0
cum = grid[x][y]
for c in commands:
    if c == "L":
        dir_num = (dir_num + 3) % 4
    elif c == "R":
        dir_num = (dir_num + 1) % 4
    else:
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]

        if not in_range(nx, ny):
            continue
        
        cum += grid[nx][ny]

        x = nx
        y = ny

print(cum)