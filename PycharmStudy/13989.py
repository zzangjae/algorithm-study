import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def bit_lst(i):
    temp_lst = []

    for j in range(3, -1, -1):
        temp_lst.append('1' if (i & (1 << j)) else '0')

    return temp_lst


for tc_num in range(1, t+1):
    n, num = input().split()
    result = []

    for i in num:
        result += bit_lst(int(i, 16))

    print(f'#{tc_num} {"".join(map(str, result))}')
