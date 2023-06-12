import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def bit_print(i):
    result = ''
    length = 4 * n - 1

    for j in range(length, -1, -1):
        result += '1' if (i & (1 << j)) else '0'

    return result


for test_case_num in range(1, t + 1):
    n, hexadecimal = input().split()
    n = int(n)
    hexadecimal = int(hexadecimal, 16)
    print(f'#{test_case_num} {bit_print(hexadecimal)}')

