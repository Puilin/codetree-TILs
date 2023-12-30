def setting(str):
    return int(str) + 1000

arr = [[0 for _ in range(2001)] for _ in range(2001)]

x1_origin, y1_origin, x2_origin, y2_origin = map(setting, input().split())

for i in range(x1_origin, x2_origin):
    for j in range(y1_origin, y2_origin):
        arr[i][j] = 1

x1, y1, x2, y2 = map(setting, input().split()) # 993 999 1008 1002

for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i][j] = 0

max_v = 0
row_count = 0

# edge case (사각형이 2개로 쪼개지는 경우 [가로])
# if (x1 < x1_origin and x2 > x2_origin and y1_origin < y1 < y2 < y2_origin) or\
# x1_origin < x1 < x2 < x2_origin and y1 < y1_origin and y2 > y2_origin:
#     print((x2_origin-x1_origin) * (y2_origin-y1_origin))
# else:
for i in range(x1_origin, x2_origin): # 955 1005
    # 1의 개수(잔해물) 카운트
    count = 0
    for j in range(y1_origin, y2_origin):
        if arr[i][j] == 1:
            count += 1
    # 현재 행에 잔해물이 남아있다면 행 개수를 하나 올림
    if count > 0:
        row_count += 1
    # 한 행이 가지는 1의 개수(잔해물) 최대값 업데이트
    if max_v < count:
        max_v = count

print(max_v * row_count)