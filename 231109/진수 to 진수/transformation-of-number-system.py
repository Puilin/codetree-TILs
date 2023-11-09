a, b = map(int, input().split())

n = input()

before = list(map(int, list(n)))
ans = 0
for i in before:
    ans = ans * a + i

after = []
while ans >= b:
    after.append(ans % b)
    ans //= b
after.append(ans)

for i in range(len(after)-1, -1, -1):
    print(after[i], end="")