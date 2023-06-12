import sys
sys.stdin = open("input.txt", "r")

for iteration in range(10):
    n = int(input())
    str_lst = [list(input()) for _ in range(8)]
    rev_str_lst = list(zip(*str_lst))
    result = 0

    for row_idx in range(8):

        for column_idx in range(9-n):

            temp_lst = str_lst[row_idx][column_idx : column_idx + n]
            if temp_lst[0: n//2] == temp_lst[-1:n//2 + n % 2-1:-1]:
                result += 1

            temp_lst = rev_str_lst[row_idx][column_idx : column_idx + n]

            if temp_lst[0: n // 2] == temp_lst[-1:n//2 + n % 2-1: - 1]:
                result += 1

    print(f'#{iteration + 1} {result}')

