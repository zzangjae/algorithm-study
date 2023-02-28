import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def bit_lst(i):
    temp_lst = []

    for j in range(3, -1, -1):
        temp_lst.append('1' if (i & (1 << j)) else '0')

    return temp_lst


for tc_num in range(1, t+1):
    code_lst = list(input())
    binary_code_lst = []
    last_1_idx = 0
    secret_code_dict = {
        0: '001101',
        1: '010011',
        2: '111011',
        3: '110001',
        4: '100011',
        5: '110111',
        6: '001011',
        7: '111101',
        8: '011001',
        9: '101111'
    }
    result = []

    for num in code_lst:
        binary_code_lst += bit_lst(int(num, 16))

    for idx in range(len(binary_code_lst)-1, -1, -1):
        if binary_code_lst[idx] == '1':
            last_1_idx = idx
            break

    for code_idx in range(idx-5, -1, -6):
        for number in range(9):
            if secret_code_dict[number] == "".join(binary_code_lst[code_idx: code_idx+6]):
                result.append(number)

    print(f'#{tc_num} {" ".join(map(str, result[::-1]))}')


