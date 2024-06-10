import sys

n = int(input())

rooms = []
for _ in range(n):
    limit = int(input())
    rooms.append(limit)

min_dist = sys.maxsize # 현재 최소 거리
for i in range(n):
    dist = 0 # 이 방에서 시작해서 거리 총합 누적
    length = 0 # 출발점에서 현재 방까지의 거리
    for j in range(n):
        idx = (i+j)%n
        dist += rooms[idx] * length

        length += 1
    
    min_dist = min(min_dist, dist)

print(min_dist)