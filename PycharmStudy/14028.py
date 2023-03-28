import sys
sys.stdin = open('input.txt', 'r')

t = int(input())


for tc_num in range(1, t+1):
    binary_num = input()
    ternary_num = input()
    binary_sum = int(binary_num, 2)
    ternary_sum = int(ternary_num, 3)

    possible_binary_lst = []
    result = 0

    for idx in range(len(binary_num)):

        if binary_num[idx] == '0':
            temp_binary = binary_num[:idx] + '1' + binary_num[idx+1: len(binary_num)]
            possible_binary_lst.append(int(temp_binary, 2))

        else:
            temp_binary = binary_num[:idx] + '0' + binary_num[idx + 1: len(binary_num)]
            possible_binary_lst.append(int(temp_binary, 2))

    for idx in range(len(ternary_num)):

        if ternary_num[idx] == '0':
            temp_ternary = ternary_num[:idx] + '1' + ternary_num[idx+1: len(ternary_num)]
            temp_sum = int(temp_ternary, 3)
            if temp_sum in possible_binary_lst:
                result = temp_sum
                break

            temp_ternary = ternary_num[:idx] + '2' + ternary_num[idx + 1: len(ternary_num)]
            temp_sum = int(temp_ternary, 3)
            if temp_sum in possible_binary_lst:
                result = temp_sum
                break

        elif ternary_num[idx] == '1':
            temp_ternary = ternary_num[:idx] + '0' + ternary_num[idx+1: len(ternary_num)]
            temp_sum = int(temp_ternary, 3)
            if temp_sum in possible_binary_lst:
                result = temp_sum
                break

            temp_ternary = ternary_num[:idx] + '2' + ternary_num[idx + 1: len(ternary_num)]
            temp_sum = int(temp_ternary, 3)
            if temp_sum in possible_binary_lst:
                result = temp_sum
                break

        else:
            temp_ternary = ternary_num[:idx] + '0' + ternary_num[idx+1: len(ternary_num)]
            temp_sum = int(temp_ternary, 3)
            if temp_sum in possible_binary_lst:
                result = temp_sum
                break

            temp_ternary = ternary_num[:idx] + '1' + ternary_num[idx + 1: len(ternary_num)]
            temp_sum = int(temp_ternary, 3)
            if temp_sum in possible_binary_lst:
                result = temp_sum
                break

    print(f'#{tc_num} {result}')

