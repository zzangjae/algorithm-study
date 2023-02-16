import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_log2(x):
    if x <= 1:
        return 0
    return 1 + get_log2(x//2)


for test_case_num in range(1, t + 1):
    n = int(input())
    num_lst = list(range(1, n+1))
    tree_lst = [0] * (n + 1)
    last_child_idx = n
    first_child_idx = get_log2(n) ** 2

    while first_child_idx >= 1:

        tree_lst[first_child_idx : last_child_idx + 1] =\
        num_lst[n - last_child_idx: n - first_child_idx + 1]

        last_child_idx = first_child_idx - 1
        first_child_idx = first_child_idx // 2

    print(f'#{test_case_num} {tree_lst[1]} {tree_lst[int(n/2)]}')

