import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    n = int(input())
    maze_lst = [list(map(int, list(input()))) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze_lst[i][j] == 2:
                start_row, start_column = i, j

            elif maze_lst[i][j] == 3:
                end_row, end_column = i, j

    queue = [(start_row, start_column, 0)]
    checker = [[True for _ in range(n)] for _ in range(n)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    result = 0

    while queue:
        row, column, depth = queue.pop(0)
        checker[row][column] = False

        if maze_lst[row][column] == 3:
            result = depth - 1
            break

        for direction in range(4):
            temp_row, temp_column = row + dr[direction], column + dc[direction]

            if (0 <= temp_row < n) and (0 <= temp_column < n):

                if maze_lst[temp_row][temp_column] != 1 and checker[temp_row][temp_column]:
                    queue.append((temp_row, temp_column, depth + 1))

    print(f'#{test_case_num} {result}')







