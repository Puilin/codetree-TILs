n = int(input())

arr = [
    [0] * n
    for _ in range(n)
]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

limit = [] # 현재 단계에서 갈 수 있는 최대 칸 수
for i in range(1, n):
    limit.append(i)
    limit.append(i)
limit.append(n)

dir_num = 0
x, y = n//2, n//2
arr[x][y] = 1
count = 1 # 누적 숫자
now = 0 # now < limit
while count < n*n:
    for l in limit:
        for i in range(l):
            nx = x + dx[dir_num]
            ny = y + dy[dir_num]

            if not in_range(nx, ny):
                break
            
            arr[nx][ny] = arr[x][y] + 1
            count += 1
            x = nx
            y = ny
        dir_num = (dir_num + 1) % 4

for row in arr:
    for num in row:
        print(num, end=" ")
    print("")