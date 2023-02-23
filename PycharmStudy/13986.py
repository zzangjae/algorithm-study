import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t+1):
    e, n = map(int, input().split())
    e_lst = list(map(int, input().split()))
    tree = {}

    for idx in range(e):
        node1, node2 = e_lst[idx * 2], e_lst[idx * 2 + 1]

        if node1 not in tree:
            tree[node1] = [node2]

        else:
            tree[node1].append(node2)

    stack = [n]
    result = 0

    while stack:
        temp_node = stack.pop()

        if temp_node in tree:

            for node in tree[temp_node]:
                stack.append(node)

        result += 1

    print(f'#{test_case_num} {result}')
