n = input()

before = list(map(int, list(n)))

ans = 0
for i in before:
    ans = ans * 2 + i
ans *= 17

after = []
while ans >= 2:
    after.append(ans % 2)
    ans //= 2
after.append(ans)

for j in range(len(after)-1, -1, -1):
    print(after[j], end="")