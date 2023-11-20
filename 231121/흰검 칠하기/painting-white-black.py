n = int(input())

arr = ['N' for _ in range(200001)]
change_count = [0 for _ in range(200001)]

def print_tile(cursor, direction):
    now = arr[cursor]
    changed_num = change_count[cursor]
    if direction == 'L':
        if changed_num <= 2:
            arr[cursor] = 'W'
            change_count[cursor] += 1
        else:
            arr[cursor] = 'G'
    else: # 'R'
        if changed_num <= 2:
            arr[cursor] = 'B'
            change_count[cursor] += 1
        else:
            arr[cursor] = 'G'

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