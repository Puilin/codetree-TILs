r, c = map(int, input().split())

grid = []
for _ in range(r):
    grid.append(input().split())

cnt = 0
for i in range(1, r-1):
    for j in range(1, c-1):
        if grid[i][j] != grid[0][0]:
            for k in range(i+1, r-1):
                for l in range(j+1, c-1):
                    if grid[k][l] == grid[0][0]:
                        cnt += 1
print(cnt)