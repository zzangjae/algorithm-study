import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    n = int(input())
    maze_lst = [list(map(int, list(input()))) for _ in range(n)]
    r = 0
    c = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    checker = [[False for _ in range(n)] for _ in range(n)]
    stack = []
    answer = 0

    for row in range(n):
        for column in range(n):
            if maze_lst[row][column] == 2:
                r = row
                c = column

    checker[r][c] = True

    while True:
        for direction in range(4):
            if 0 <= r + dr[direction] < n and 0 <= c + dc[direction] < n \
                    and (not maze_lst[r + dr[direction]][c + dc[direction]]\
                    or maze_lst[r + dr[direction]][c + dc[direction]] == 3)\
                    and not checker[r + dr[direction]][c + dc[direction]]:
                stack.append((r + dr[direction], c + dc[direction]))

        if maze_lst[r][c] == 3:
            answer = 1
            break

        if len(stack) == 0:
            answer = 0
            break

        r, c = stack.pop()
        checker[r][c] = True

    print(f'#{iteration + 1} {answer}')