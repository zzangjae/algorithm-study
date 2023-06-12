import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def get_abs_sum(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    temp_sum = 0

    for idx in range(4):
        if 0 <= x + dx[idx] < n and 0 <= y + dy[idx] < n:
            temp_sum += abs(num_lst[x + dx[idx]][y + dy[idx]] - num_lst[x][y])
        else:
            continue

    return temp_sum


for iteration in range(T):
    n = int(input())
    num_lst = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for y in range(n):
        for x in range(n):
            result += get_abs_sum(x, y)

    print(f'#{iteration+1} {result}')


