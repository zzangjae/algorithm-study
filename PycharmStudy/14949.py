import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_structure(row):
    counter = 0
    result = 0

    for data in row:
        if data == 1:
            counter += 1

        elif counter and data == 0:
            if counter > result:
                result = counter
            counter = 0

    if counter > result:
        result = counter

    return result


for test_case in range(1, t + 1):

    n, m = map(int, input().split())
    picture_lst = [list(map(int, input().split())) for _ in range(n)]
    tran_picture_lst = list(zip(*picture_lst))
    max_result = 0

    for row in picture_lst:
        temp_result = get_structure(row)

        if temp_result > max_result:
            max_result = temp_result

    for column in tran_picture_lst:
        temp_result = get_structure(column)

        if temp_result > max_result:
            max_result = temp_result

    print(f'#{test_case} {max_result}')


