n = int(input())

arr = ['N' for _ in range(200001)]
black_count = [0 for _ in range(200001)]
white_count = [0 for _ in range(200001)]

def check_gray(cursor):
    return black_count[cursor] >= 2 and white_count[cursor] >= 2

def print_tile(cursor, direction):
    now = arr[cursor]
    if direction == 'L':
        white_count[cursor] += 1
        if check_gray(cursor):
            arr[cursor] = 'G'
        else:
            arr[cursor] = 'W'
    else: # 'R'
        black_count[cursor] += 1
        if check_gray(cursor):
            arr[cursor] = 'G'
        else:
            arr[cursor] = 'B'

cursor = 100000
for _ in range(n):
    distance, direction = input().split()

    for i in range(int(distance)):
        print_tile(cursor, direction)
        if direction == 'L':
            cursor -= 1
        else:
            cursor += 1
    # 제자리에 멈춰야함
    if direction == 'L':
        cursor += 1
    else:
        cursor -= 1


w = arr.count('W')
b = arr.count('B')
g = arr.count('G')

print(w, b, g, sep=" ")