n, b = map(int, input().split())

result = [] # [3, 3, 2, 1]
while n >= b:
    result.append(n % b)
    n //= b
result.append(n)

ans = 0
for i in range(len(result)-1, -1, -1):
    ans = ans * 10 + result[i]
print(ans)