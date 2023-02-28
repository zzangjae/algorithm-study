import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_white(white_row_lst):
    temp_result = 0

    for row in white_row_lst:
        for color in row:
            if color != 'W':
                temp_result += 1

    return temp_result


def get_blue(blue_row_lst):
    temp_result = 0

    for row in blue_row_lst:
        for color in row:
            if color != 'B':
                temp_result += 1

    return temp_result


def get_red(red_row_lst):
    temp_result = 0

    for row in red_row_lst:
        for color in row:
            if color != 'R':
                temp_result += 1

    return temp_result


for tc_num in range(1, t+1):
    n, m = map(int, input().split())
    flag_lst = [list(input()) for _ in range(n)]
    color_min = 2500

    for white_end in range(0, n-2):
        temp_white = get_white(flag_lst[:white_end+1])

        for blue_end in range(white_end+1, n-1):
            temp_blue = get_blue(flag_lst[white_end+1: blue_end+1])
            temp_red = get_red(flag_lst[blue_end+1:])

            if color_min > temp_red + temp_blue + temp_white:
                color_min = temp_red + temp_blue + temp_white

    print(f'#{tc_num} {color_min}')