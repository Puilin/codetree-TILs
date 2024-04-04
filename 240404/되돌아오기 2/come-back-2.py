strings = list(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0
x, y = 0, 0

sec = 0

def move(strings):
    global sec
    global x, y
    global dir_num
    for command in strings:
        if command == 'L':
            dir_num = (dir_num + 3) % 4
            sec += 1
        if command == 'R':
            dir_num = (dir_num + 1) % 4
            sec += 1
        if command == 'F':
            x = x + dx[dir_num]
            y = y + dy[dir_num]

            sec += 1

            if x == 0 and y == 0:
                return True
    return False

if move(strings):
    print(sec)
else:
    print(-1)