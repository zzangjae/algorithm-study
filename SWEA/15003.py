import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    bit_lst = list(map(int, list(input())))
    result = 0 if bit_lst[0] == 0 else 1

    for idx in range(len(bit_lst) - 1):

        if bit_lst[idx] != bit_lst[idx + 1]:
            result += 1

    print(f'#{test_case_num} {result}')


