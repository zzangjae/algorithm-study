import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    n = int(input())
    box = [[0 for _ in range(n)] for _ in range(n)]
    dr = [0, 1, 0, -1] * (n // 2 + 1)
    dc = [1, 0, -1, 0] * (n // 2 + 1)
    count = 0
    r = 0
    c = -1

    for num in range(n ** 2):

        r += dr[count]
        c += dc[count]
        if 0 <= r < n and 0 <= c < n and not box[r][c]:
            box[r][c] = num + 1
        else:
            r -= dr[count]
            c -= dc[count]
            count += 1
            r += dr[count]
            c += dc[count]
            box[r][c] = num + 1

    print(f'#{iteration + 1}')

    for row in box:
        print(' '.join(map(str, row)))
