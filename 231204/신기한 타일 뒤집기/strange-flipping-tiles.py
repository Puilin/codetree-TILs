n = int(input())

arr = ["N" for _ in range(200000)]
cursor = 100000
for _ in range(n):
    distance, direction = tuple(input().split())
    # 왼쪽은 흰색
    if direction == 'L':
        for i in range(int(distance)):
            arr[cursor - i] = "W"
        cursor -= int(distance) - 1
    # 오른쪽은 검은색
    else:
        for i in range(int(distance)):
            arr[cursor + i] = "B"
        cursor += int(distance) - 1

white = arr.count("W")
black = arr.count("B")

print(white, black)