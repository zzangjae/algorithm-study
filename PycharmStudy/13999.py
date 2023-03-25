import sys
sys.stdin = open('input.txt', 'r')

t = int(input())


def get_fly(r, c):
    temp_return1 = 0
    temp_return2 = 0

    for row_idx in range(r-m+1, r+m):

        for column_idx in range(c-m+1, c+m):

            if 0 <= row_idx < n and 0 <= column_idx < n:

                if row_idx == r or column_idx == c:
                    temp_return1 += fly_lst[row_idx][column_idx]

                if abs(row_idx - r) == abs(column_idx - c):
                    temp_return2 += fly_lst[row_idx][column_idx]

    return temp_return1, temp_return2


for tc_num in range(1, t+1):
    n, m = map(int, input().split())
    fly_lst = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for row in range(n):
        for column in range(n):
            temp_result = get_fly(row, column)

            if temp_result[0] > result:
                result = temp_result[0]

            elif temp_result[1] > result:
                result = temp_result[1]

    print(f'#{tc_num} {result}')


