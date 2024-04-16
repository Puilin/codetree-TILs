import sys

n = int(input())

arr = [0]
arr = arr + list(map(int, input().split()))

min_num = sys.maxsize
for i in range(1, n+1):
    dist = 0
    for j in range(1, n+1):
        dist += abs(j-i)*arr[j]
    if dist < min_num:
        min_num = dist

print(min_num)