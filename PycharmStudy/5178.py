import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_sum(idx = 1):

    if idx > n:
        return 0

    elif tree_lst[idx] is not None:
        return tree_lst[idx]

    else:
        tree_lst[idx] = get_sum(idx * 2) + get_sum(idx * 2 + 1)
        return tree_lst[idx]


for test_case_num in range(1, t + 1):
    n, m, l = map(int, input().split())
    tree_lst = [None] * (n + 1)

    for _ in range(m):
        idx, node = map(int, input().split())
        tree_lst[idx] = node

    get_sum(1)

    print(f'#{test_case_num} {tree_lst[l]}')

