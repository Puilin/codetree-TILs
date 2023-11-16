n = int(input())

arr = ['N' for _ in range(200001)]

def print_tile(cursor, direction):
    now = arr[cursor]
    if direction == 'L':
        if now == 'N':
            arr[cursor] = 'W'
        elif now == 'B':
            arr[cursor] = 'G'
    else: # 'R'
        if now == 'N':
            arr[cursor] = 'B'
        elif now == 'W':
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

# ['N', 'N', 'N', 'N', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'N', 'N', 'N', ...]
w = arr.count('W')
b = arr.count('B')
g = arr.count('G')

print(w, b, g, sep=" ")