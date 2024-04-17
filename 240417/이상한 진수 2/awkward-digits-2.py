a = list(map(int, list(input())))

# 모두 1인 경우
if sum(a) == len(a):
    a[-1] = 0
else:
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = 1
            break
# 1110
ans = 0
level = 1
for i in range(len(a)-1, -1, -1):
    ans += a[i] * level
    level *= 2

print(ans)