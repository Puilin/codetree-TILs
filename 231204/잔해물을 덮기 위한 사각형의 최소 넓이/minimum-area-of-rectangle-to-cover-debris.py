def setting(str):
    return int(str) + 1000

arr = [[0 for _ in range(2000)] for _ in range(2000)]

x1, y1, x2, y2 = map(setting, input().split())
origin = [x1, y1, x2, y2]

for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i][j] = 1

x1, y1, x2, y2 = map(setting, input().split())

for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i][j] = 0

max_v = 0
row_count = 0
for i in range(origin[0], origin[2]):
    # 1의 개수(잔해물) 카운트
    count = 0
    for j in range(origin[1], origin[3]):
        if arr[i][j] == 1:
            count += 1
    # 현재 행에 잔해물이 남아있다면 행 개수를 하나 올림
    if count > 0:
        row_count += 1
    # 한 행이 가지는 1의 개수(잔해물) 최대값 업데이트
    if max_v < count:
        max_v = count

print(max_v * row_count)