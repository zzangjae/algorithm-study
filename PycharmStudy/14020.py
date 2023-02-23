import sys
sys.stdin = open("input.txt", "r")


def in_order(idx = 1):

    if idx > n:
        return ''

    else:
        return in_order(idx * 2) + tree[idx] + in_order(idx * 2 + 1)


for test_case_num in range(1, 11):
    n = int(input())
    tree = [None] * (n + 1)

    for _ in range(n):
        temp_input = input().split()
        tree[int(temp_input[0])] = temp_input[1]

    print(f'#{test_case_num} {in_order()}')



