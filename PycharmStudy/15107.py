import sys
sys.stdin = open("input.txt", "r")

for iteration in range(10):
    t = int(input())
    ladder_lst = [list(map(int, input().split())) for _ in range(100)]
    stack = []
    direction = 0

    for column in range(100):
        if ladder_lst[-1][column] == 1:
            c = column
            stack.append((-1, column))

    dr = [-1, 0, 0]
    dc = [0, -1, 1]
    result = 10000
    result_r = 0
    result_c = 0

    for start_r, start_c in stack:

        r, c = start_r, start_c
        counter = 0

        while r > -100:
            counter += 1

            if not direction and 0 <= c + dc[1] and ladder_lst[r][c + dc[1]]:
                direction = 1
                c += dc[1]
                continue
            elif not direction and c + dc[2] < 100 and ladder_lst[r][c + dc[2]]:
                direction = 2
                c += dc[2]
                continue
            elif not direction:
                r += dr[0]
                continue
            elif direction:
                if ladder_lst[r + dr[0]][c]:
                    direction = 0
                    r += dr[0]
                    continue
                else:
                    c += dc[direction]

        if result > counter:
            result = counter
            result_r, result_c = r, c

    print(f'#{iteration + 1} {result_c}')





