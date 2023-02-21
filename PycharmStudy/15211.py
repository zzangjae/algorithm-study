import sys
sys.stdin = open("input.txt", "r")

for test_case_num in range(1, 11):
    n = int(input())
    maze_lst = [list(map(int, list(input()))) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze_lst[i][j] == 2:
                start_row, start_column = i, j

            elif maze_lst[i][j] == 3:
                end_row, end_column = i, j

    queue = [(start_row, start_column)]
    checker = [[True for _ in range(16)] for _ in range(16)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    result = 0

    while queue:
        row, column = queue.pop(0)
        checker[row][column] = False

        if maze_lst[row][column] == 3:
            result = 1
            break

        for direction in range(4):
            temp_row, temp_column = row + dr[direction], column + dc[direction]

            if (0 <= temp_row < 16) and (0 <= temp_column < 16):

                if maze_lst[temp_row][temp_column] != 1 and checker[temp_row][temp_column]:
                    queue.append((temp_row, temp_column))

    print(f'#{test_case_num} {result}')







