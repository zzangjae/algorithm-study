import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for tc_num in range(1, t+1):
    n, m = map(int, input().split())
    screen_lst = [list(input()) for _ in range(n)]
    secret_code_dict = {
        0: '0001101',
        1: '0011001',
        2: '0010011',
        3: '0111101',
        4: '0100011',
        5: '0110001',
        6: '0101111',
        7: '0111011',
        8: '0110111',
        9: '0001011'
    }
    last_one_row = 0
    last_one_column = 0

    for i in range(n):
        for j in range(m):
            if screen_lst[i][j] == '1':
                last_one_row = i
                last_one_column = j

    code = screen_lst[last_one_row][last_one_column-55: last_one_column+1]
    result = []

    for idx in range(0, 56, 7):
        code_num = ''.join(code[idx: idx + 7])

        for num in range(10):
            if code_num == secret_code_dict[num]:
                result.append(num)

    checker = 0
    for num_idx in range(8):
        if num_idx % 2:
            checker += result[num_idx]

        else:
            checker += result[num_idx] * 3

    print(f'#{tc_num} {sum(result) if checker % 10 == 0 else 0}')


