n = int(input())

dx = {"W": -1, "S": 0, "N": 0, "E": 1}
dy = {"W": 0, "S": -1, "N": 1, "E": 0}

x, y = 0, 0
sec = 0
done = False
for _ in range(n):
    d, s = input().split()
    for _ in range(int(s)):
        x = x + dx[d]
        y = y + dy[d]

        sec += 1

        if x == 0 and y == 0:
            done = True
            break
    if done:
        print(sec)
        break
if not done:
    print(-1)