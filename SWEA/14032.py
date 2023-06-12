import sys
sys.stdin = open("input.txt", "r")
t = int(input())


def dfs(row, column):
    stack = [(row, column)]
    counter = 0

    while stack:
        r, c = stack.pop()

        if visit[r][c] is not None:
            visit[row][column] = counter + visit[r][c]
            break

        for dr, dc in directions:

            if 0 <= r + dr < n and 0 <= c + dc < n and\
                    room_lst[r + dr][c + dc] - room_lst[r][c] == 1:
                stack.append((r + dr, c + dc))

        counter += 1

    else:
        visit[row][column] = counter


for test_case_num in range(1, t + 1):
    n = int(input())
    room_lst = [list(map(int, input().split())) for _ in range(n)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visit = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visit[i][j] is None:
                dfs(i, j)

    result = [0, 0]
    for i in range(n):
        for j in range(n):
            if visit[i][j] > result[1]:
                result[0], result[1] = room_lst[i][j], visit[i][j]

            elif visit[i][j] == result[1] and result[0] > room_lst[i][j]:
                result[0] = room_lst[i][j]

    print(f'#{test_case_num} {result[0]} {result[1]}')
