import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    n, m, r, c, l = map(int, input().split())
    underground_lst = [list(map(int, input().split())) for _ in range(n)]
    pipe_dict = {0: [],
                 1: [(-1, 0), (0, 1), (1, 0), (0, -1)],
                 2: [(-1, 0), (1, 0)],
                 3: [(0, 1), (0, -1)],
                 4: [(-1, 0), (0, 1)],
                 5: [(0, 1), (1, 0)],
                 6: [(1, 0), (0, -1)],
                 7: [(0, -1), (-1, 0)]}
    connection_dict = {}

    for i in range(n):
        for j in range(m):
            directions = list(pipe_dict[underground_lst[i][j]])
            connection_dict[(i, j)] = []

            for dr, dc in directions:
                if 0 <= i + dr < n and 0 <= j + dc < m:
                    connection_dict[(i, j)].append((i + dr, j + dc))

    fugitive_lst = [[False for _ in range(m)] for _ in range(n)]
    stack = [(r, c, l)]

    while stack:

        row, column, time = stack.pop(0)
        fugitive_lst[row][column] = True
        time -= 1

        if time <= 0:
            continue

        for dr, dc in pipe_dict[1]:

            if 0 <= row + dr < n and 0 <= column + dc < m:

                if (row + dr, column + dc) in connection_dict[(row, column)] \
                        and (row, column) in connection_dict[(row + dr, column + dc)]\
                        and not fugitive_lst[row + dr][column + dc]:
                    stack.append((row + dr, column + dc, time))

    result = 0

    for lst in fugitive_lst:
        result += lst.count(True)

    print(f'#{test_case_num} {result}')
