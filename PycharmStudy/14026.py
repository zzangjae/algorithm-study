import sys
sys.stdin = open("input.txt", "r")

t = int(input().strip())


def bit_lst(i):
    temp_lst = []

    for j in range(3, -1, -1):
        temp_lst.append('1' if (i & (1 << j)) else '0')

    return temp_lst


def get_code_from_row(row_lst):
    temp_code = []
    multiplier = 1
    temp_binary_code = get_binary_code(row_lst)
    idx = len(temp_binary_code) - 1

    while idx >= 0:
        if temp_binary_code[idx] == '0':
            idx -= 1
            multiplier = 1

        else:
            if temp_binary_code[idx-7*multiplier + 1: idx+1: multiplier] in secret_code_dict\
                    and '0' + '1'*multiplier + '0' in temp_binary_code[idx - 56*multiplier + 1: idx+1]:
                    temp_code.append(get_secret_code(temp_binary_code[idx - 56*multiplier + 1: idx+1: multiplier]))
                    idx -= 56 * multiplier
                    multiplier += 1
                    continue

            else:
                multiplier += 1
                continue

    return temp_code


def get_binary_code(code):
    temp_bcode = []

    for num in code:
        temp_bcode += bit_lst(int(num, 16))

    return ''.join(temp_bcode)


def get_secret_code(b_code):
    last_1_idx = 0
    result = []
    b_code = '0' * 4 + b_code

    for idx in range(len(b_code)-1, -1, -1):
        if b_code[idx] != '0':
            last_1_idx = idx
            break

    for start_idx in range(last_1_idx - 56 + 1, last_1_idx + 1, 7):
        temp_code = b_code[start_idx : start_idx + 7]
        result.append(secret_code_dict[temp_code])

    return result


def check_secret_code(s_code):
    result = 0
    check = 0

    for idx in range(8):
        if idx % 2:
            check += s_code[idx]

        else:
            check += 3 * s_code[idx]

    result = sum(s_code) if check % 10 == 0 else 0
    return result


for tc_num in range(1, t+1):
    secret_code_dict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }
    n, m = map(int, input().split())
    num_lst = [input().strip() for _ in range(n)]
    row_set = set()
    binary_code = []
    secret_code = []
    result = []

    for row in num_lst:

       row_set.add(row)
    row_set.remove('0' * m)

    for row in row_set:
        secret_code += (get_code_from_row(row))

    secret_code = set(secret_code)

    # print(code_set)
    #
    # for code in code_set:
    #     binary_code.append(get_binary_code(code))
    #
    # for code in binary_code:
    #     secret_code.append(get_secret_code(code))
    #
    for code in secret_code:
        result.append(check_secret_code(code))

    print(f'#{tc_num} {sum(result)}')


