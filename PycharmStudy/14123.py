import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_int_from_binary(binary_lst):
    temp_result = 0

    for i in range(6, -1, -1):
        temp_result += 2 ** i if binary_lst[6 - i] == '1' else 0

    return temp_result


for tc_num in range(1, t+1):
    binary_num_lst = list(input())
    result = []

    for binary_num_idx in range(0, len(binary_num_lst), 7):
        result.append(get_int_from_binary(binary_num_lst[binary_num_idx: binary_num_idx+7]))

    print(f'#{tc_num} {" ".join(map(str, result))}')