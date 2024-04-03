n, m = map(int, input().split())

a_pos = [0] * 1001
b_pos = [0] * 1001

now = 1
for _ in range(n):
    v, t = map(int, input().split())

    for _ in range(t):
        a_pos[now] = a_pos[now-1] + v
        now += 1

now = 1
for _ in range(m):
    v, t = map(int, input().split())

    for _ in range(t):
        b_pos[now] = b_pos[now-1] + v
        now += 1

leader = ""
cnt = -1
for i, (a, b) in enumerate(zip(a_pos, b_pos)):
    if a > b:
        if leader != "a" and i != 0:
            cnt += 1
        leader = "a"
    elif a < b:
        if leader != "b" and i != 0:
            cnt += 1
        leader = "b"
    elif a == b:
        if leader != "ab" and i != 0:
            cnt += 1
        leader = "ab"
print(cnt)