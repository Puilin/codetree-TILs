n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

largest = 0
for i in range(0, n):
    for j in range(0, n-2):
        coins = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        largest = max(largest, coins)
print(largest)