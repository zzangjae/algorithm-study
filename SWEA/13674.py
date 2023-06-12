import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):
    n = int(input())

    color_space = [[0 for _ in range(10)] for _ in range(10)]

    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        for row in range(r1, r2 + 1):
            for column in range(c1, c2 + 1):
                if color_space[row][column] == 0:
                    color_space[row][column] = color
                elif color_space[row][column] != color:
                    color_space[row][column] = 3

    result = 0
    for row in color_space:
        result += row.count(3)

    print(f'#{iteration + 1} {result}')
