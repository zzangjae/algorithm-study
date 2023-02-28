import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

for tc_num in range(1, t+1):
    n = int(input())
    farm_lst = [list(map(int, list(input()))) for _ in range(n)]
    center = n // 2
    result = 0

    for row in range(n):

        if row <= center:
            for column in range(center - row, center + row + 1):
                result += farm_lst[row][column]

        else:
            for column in range(row - center, center * 3 - row + 1):
                result += farm_lst[row][column]

    print(f'#{tc_num} {result}')



