import sys

n = int(input())

check_points = []
for _ in range(n):
    x, y = map(int, input().split())
    check_points.append((x, y))

distance = sys.maxsize
for skip_i in range(1, len(check_points)-1):
    result = 0
    for i in range(0, len(check_points)-1):
        if i == skip_i:
            continue
        
        x1, x2, y1, y2 = 0, 0, 0, 0
        if i+1 == skip_i:
            x1, y1 = check_points[i]
            x2, y2 = check_points[i+2]

        else:
            x1, y1 = check_points[i]
            x2, y2 = check_points[i+1]

        result += abs(x1-x2) + abs(y1-y2)
    
    distance = min(distance, result)

print(distance)