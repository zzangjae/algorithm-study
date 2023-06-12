import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_node(idx):

    if idx == 1:
        return

    parent_idx = idx // 2
    child_idx = idx

    if tree_lst[parent_idx] > tree_lst[child_idx]:
        tree_lst[parent_idx], tree_lst[child_idx] = tree_lst[child_idx], tree_lst[parent_idx]
        get_node(idx // 2)

    return


for test_case_num in range(1, t + 1):
    n = int(input())
    node_lst = [0] + list(map(int, input().split()))
    tree_lst = [None] * (n + 1)

    for idx in range(1, n+1):
        tree_lst[idx] = node_lst[idx]
        get_node(idx)

    idx = n // 2
    result = 0

    while idx >= 1:
        result += tree_lst[idx]
        idx = idx // 2

    print(f'#{test_case_num} {result}')

