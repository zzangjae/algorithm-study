import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def in_order(idx=1):

    if idx > n:
        return ''

    else:
        return in_order(idx * 2) + num_lst[idx] + ' ' + in_order(idx * 2 + 1)


for test_case_num in range(1, t+1):
    n = int(input())
    num_lst = list(map(str, range(0, n + 1)))
    node_num = list(map(int, in_order().split()))
    bst_tree = {}

    for idx, num in zip(node_num, num_lst[1:]):
        bst_tree[idx] = num

    print(f'#{test_case_num} {bst_tree[1]} {bst_tree[n//2]}')

