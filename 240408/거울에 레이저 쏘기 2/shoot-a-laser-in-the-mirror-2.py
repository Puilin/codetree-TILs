n = int(input())

board = []

for _ in range(n):
    dirs = list(input())
    board.append(dirs)

def start_index(k):
    if k <= n:
        return (0, k-1, 0)
    elif k <= 2*n:
        return ((k-1)%n, 2, 1)
    elif k <= 3*n:
        return (2, 3*n-k, 2)
    else:
        return (4*n-k, 0, 3)

# 아래 왼 오른 위
# 0 1 2 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def reflect(direction, mirror):
    if mirror == "/":
        if direction in [1, 3]:
            return (direction + 3) % 4
        else:
            return (direction + 1) % 4
    else:
        if direction in [0, 2]:
            return (direction + 3) % 4
        else:
            return (direction + 1) % 4

k = int(input())

x, y, d = start_index(k)

cnt = 0
while 0 <= x < n and 0 <= y < n:
    d = reflect(d, board[x][y])
    cnt += 1
    x = x + dx[d]
    y = y + dy[d]
print(cnt)