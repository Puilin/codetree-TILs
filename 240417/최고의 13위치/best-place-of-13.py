n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

largest = 0
for row in grid:
    largest = max(largest, sum(row))
print(largest)