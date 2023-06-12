import sys
sys.stdin = open("input.txt", "r")

t = int(input().strip())

for tc_num in range(1, t+1):
    input_lst = [list(input()) for _ in range(5)]

    result = ''

    for column in range(15):
        for row in range(5):

            if column < len(input_lst[row]):
                result += input_lst[row][column]

    print(f'#{tc_num} {result}')