n, m, k = map(int, input().split())

sheet = [0 for _ in range(n+1)]
found = False
for _ in range(m):
    violated = int(input())
    sheet[violated] += 1
    if sheet[violated] >= k:
        print(violated)
        found = True
        break

if not found:
    print(-1)