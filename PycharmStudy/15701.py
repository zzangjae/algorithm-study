import sys
sys.stdin = open("input.txt", "r")

for tc_num in range(1, 11):
    n = int(input())
    table_lst = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for column in range(n):
        checker = 0

        for row in range(n):

            if table_lst[row][column] == 1 and checker != 1:
                checker = 1

            elif table_lst[row][column] == 2 and checker == 1:
                checker = 2
                result += 1

    print(f'#{tc_num} {result}')
