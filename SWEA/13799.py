import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):

    v, e = map(int, input().split())
    node_dict = {}
    result = []

    for _ in range(e):
        start, end = map(int, input().split())
        if start not in node_dict:
            node_dict[start] = [end]
        else:
            node_dict[start].append(end)

    s, g = map(int, input().split())
    stack = [s]

    while stack:

        s_node = stack.pop()

        if s_node in result:
            continue

        result.append(s_node)

        if s_node in node_dict:
            next_nodes = node_dict[s_node]

            for node in next_nodes:
                stack.append(node)

    if g in result:
        result = 1
    else:
        result = 0

    print(f'#{test_case} {result}')


