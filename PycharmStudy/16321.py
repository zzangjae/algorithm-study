import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def check_squre(length, row, column):
    for i in range(length):
        for j in range(length):
            if square_lst[row + i][column + j] == '.':
                return False
    return True


for iteration in range(t):
    n = int(input())

    square_lst = [list(input()) for _ in range(n)]
    square_num_lst = [num * num for num in range(1, n + 1)]
    square = 0
    for squres in square_lst:
        square += squres.count('#')
    result = 'no'

    if square in square_num_lst:
        square_length = int(square ** 0.5)

        for row in range(n - square_length + 1):
            for column in range(n - square_length + 1):
                if check_squre(square_length, row, column):
                    result = 'yes'

    print(f'#{iteration + 1} {result}')



