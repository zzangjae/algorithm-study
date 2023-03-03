import sys
sys.stdin = open('input.txt', 'r')

t = int(input())


def get_result(r, c):
    flower_powder = num_lst[r][c]
    temp_result = -flower_powder

    for row in range(r-flower_powder, r+flower_powder+1):
        if 0 <= row < n:
            temp_result += num_lst[row][c]

    for column in range(c-flower_powder, c+flower_powder+1):
        if 0 <= column < m:
            temp_result += num_lst[r][column]

    return temp_result


for tc_num in range(1, t+1):
    n, m = map(int, input().split())
    num_lst = [list(map(int, input().split())) for _ in range(n)]
    maximum = 0

    for i in range(n):
        for j in range(m):
            temp_max = get_result(i, j)
            if temp_max > maximum:
                maximum = temp_max

    print(f'#{tc_num} {maximum}')
