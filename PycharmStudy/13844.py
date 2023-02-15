import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    n = int(input())
    maze_lst = [list(map(int, list(input()))) for _ in range(n)]

    for row in range(n):
        for column in range(n):
            if maze_lst[row][column] == 2:
                start = (row, column)

            elif maze_lst[row][column] == 3:
                end = (row, column)

    stack = [start]
    checker = [[True] * n for _ in range(n)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    result = 0

    while stack:
        r, c = stack.pop()
        checker[r][c] = False

        if (r, c) == end:
            result = 1
            break

        for direction in range(4):
            if 0 <= r + dr[direction] < n and 0 <= c + dc[direction] < n:

                if checker[r + dr[direction]][c + dc[direction]] and\
                        maze_lst[r + dr[direction]][c + dc[direction]] != 1:
                    checker[r + dr[direction]][c + dc[direction]] = False
                    stack.append((r + dr[direction], c + dc[direction]))

    print(f'#{test_case_num} {result}')


