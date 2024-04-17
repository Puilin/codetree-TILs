seq = list(input())

cnt = 0
for i in range(len(seq)):
    for j in range(i+1, len(seq)):
        if seq[i] == "(" and seq[j] == ")":
            cnt += 1

print(cnt)