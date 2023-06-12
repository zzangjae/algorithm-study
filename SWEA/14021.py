import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def make_tree(i=1):

    if i > n:
        return 0

    elif node_lst[i] is None:
        node_lst[i] = make_tree(2 * i) + make_tree(2 * i + 1)
        return node_lst[i]

    else:
        return node_lst[i]


for test_case_num in range(1, t+1):
    n, m, l = map(int, input().split())
    node_lst = [None] * (n + 1)

    for _ in range(m):
        idx, num = map(int, input().split())
        node_lst[idx] = num

    make_tree()
    print(f'#{test_case_num} {node_lst[l]}')

