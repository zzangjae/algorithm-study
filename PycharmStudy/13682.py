import sys
sys.stdin = open("input.txt", "r")

for iteration in range(10):
    t = int(input())
    ladder_lst = [list(map(int, input().split())) for _ in range(100)]
    r = -1
    c = 0
    direction = 0

    for column in range(100):
        if ladder_lst[-1][column] == 2:
            c = column
            break

    dr = [-1, 0, 0]
    dc = [0, -1, 1]

    while r > -100:
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

    print(f'#{iteration + 1} {c}')





