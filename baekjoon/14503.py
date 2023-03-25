import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
r, c, d = map(int, input().split())
directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
room_lst = [list(map(int, input().split())) for _ in range(n)]
stack = [(r, c, d)]
result = 0

while stack:

    row, column, direction = stack.pop()

    if room_lst[row][column] == 0:
        room_lst[row][column] = 2
        result += 1
        stack.append((row, column, direction))

    else:
        for i in range(4):
            temp_row, temp_column = row + directions[i][0],  column + directions[i][1]

            if 0 <= temp_row < n and 0 <= temp_column < m and room_lst[temp_row][temp_column] == 0:
                temp_direction = 3 if direction == 0 else direction - 1

                temp_row, temp_column = row + directions[temp_direction][0],  column + directions[temp_direction][1]

                if 0 <= temp_row < n and 0 <= temp_column < m and room_lst[temp_row][temp_column] == 0:
                    stack.append((temp_row, temp_column, temp_direction))
                    break

                else:
                    stack.append((row, column, temp_direction))
                    break

        else:
            temp_direction = direction - 2 if direction > 1 else 4 + direction - 2
            temp_row, temp_column = row + directions[temp_direction][0], column + directions[temp_direction][1]

            if 0 <= temp_row < n and 0 <= temp_column < m and room_lst[temp_row][temp_column] != 1:
                stack.append((temp_row, temp_column, direction))

            else:
                break

print(result)