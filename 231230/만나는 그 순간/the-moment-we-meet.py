n, m = map(int, input().split())

timestamp_a = [0]
timestamp_b = [0]
for _ in range(n):
    d, t = input().split()

    point = 0
    for _ in range(int(t)):
        if d == 'L':
            point = timestamp_a[-1] - 1
        elif d == 'R':
            point = timestamp_a[-1] + 1
        timestamp_a.append(point)

for _ in range(m):
    d, t = input().split()

    point = 0
    for _ in range(int(t)):
        if d == 'L':
            point = timestamp_b[-1] - 1
        elif d == 'R':
            point = timestamp_b[-1] + 1
        timestamp_b.append(point)

time = 0
for a, b in zip(timestamp_a, timestamp_b):
    if a == b and a != 0:
        print(time)
        break
    time += 1