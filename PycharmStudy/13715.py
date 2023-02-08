import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    n, m = map(int, input().split())
    str_lst = [list(input()) for _ in range(n)]
    inv_str_lst = list(zip(*str_lst))
    result = ''

    for row in range(n):

        for column_start in range(n-m+1):
            if str_lst[row][column_start : column_start + m // 2] \
                    == str_lst[row][m + column_start - 1 : column_start + m // 2 + m % 2 - 1 : -1]:
                result = str_lst[row][column_start: column_start + m]

        for column_start in range(n - m + 1):
            if inv_str_lst[row][column_start: column_start + m // 2] \
                    == inv_str_lst[row][m + column_start - 1: column_start + m // 2 + m % 2 - 1: -1]:
                result = inv_str_lst[row][column_start: column_start + m]

    print(f'#{iteration + 1} ' + ''.join(result))
