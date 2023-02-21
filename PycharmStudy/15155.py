import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def is_win(r, c, direction=0, counter=0):

    if counter == 5:
        return True

    elif not (0 <= r < n) or not (0 <= c < n) \
            or omok_lst[r][c] == '.':
        return False

    temp_r = r + dr[direction]
    temp_c = c + dc[direction]

    if omok_lst[r][c] == 'o':
        return is_win(temp_r, temp_c, direction, counter + 1)


for test_case_num in range(1, t + 1):
    n = int(input())
    omok_lst = [list(input()) for _ in range(n)]
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]
    result = 'NO'

    for row in range(n):

        for column in range(n):

            if omok_lst[row][column] == 'o':

                for direction in range(8):

                    if is_win(row, column, direction):
                        result = 'YES'
                        break

                else:
                    continue
                break

        else:
            continue
        break

    print(f'#{test_case_num} {result}')





