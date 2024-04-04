n, m = map(int, input().split())

board = [
    [0] * (n+1)
    for _ in range(n+1)
]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

for _ in range(m):
    r, c = map(int, input().split())

    board[r][c] = 1

    colored = 0
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]

        if not in_range(nr, nc):
            continue

        if board[nr][nc] == 1:
            colored += 1
    
    if colored == 3:
        print(1)
    else:
        print(0)