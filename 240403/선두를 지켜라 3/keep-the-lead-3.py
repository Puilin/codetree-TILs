n, m = map(int, input().split())

a_pos = [0]
b_pos = [0]

now = 1
for _ in range(n):
    v, t = map(int, input().split())

    for _ in range(t):
        a_pos.append(a_pos[now-1] + v)
        now += 1

now = 1
for _ in range(m):
    v, t = map(int, input().split())

    for _ in range(t):
        b_pos.append(b_pos[now-1] + v)
        now += 1

leader = []
cnt = 0
for i in range(1, len(a_pos)):
    if a_pos[i] > b_pos[i] and a_pos[i-1] <= b_pos[i-1]:
        leader.append("a")
    elif a_pos[i] < b_pos[i] and a_pos[i-1] >= b_pos[i-1]:
        leader.append("b")
    elif a_pos[i] == b_pos[i] and a_pos[i-1] != b_pos[i-1]:
        leader.append("ab")
print(len(leader))