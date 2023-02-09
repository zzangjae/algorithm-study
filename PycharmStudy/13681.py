import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_3by3(num):
    start_row = (num // 3) * 3 % 9
    start_column = num * 3 % 9
    temp_lst = []

    for idx in range(9):
        r = start_row + idx // 3
        c = start_column + idx % 3
        temp_lst.append(num_lst[r][c])

    return temp_lst


for iteration in range(t):
    num_lst = [list(map(int, input().split())) for _ in range(9)]
    inv_num_lst = list(zip(*num_lst))
    result = 1

    for row in range(1, 10):
        for column in range(1, 10):
            box = get_3by3(row - 1)

            if column not in num_lst[row - 1]:
                result = 0
                break

            if column not in inv_num_lst[row - 1]:
                result = 0
                break

            if column not in box:
                result = 0
                break

    print(f'#{iteration + 1} {result}')



