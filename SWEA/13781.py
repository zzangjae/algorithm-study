import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):

    v, e = map(int, input().split())
    num_dict = {}
    stack = [1]
    result = []

    for _ in range(e):
        start, end = map(int, input().split())

        if start not in num_dict:
            num_dict[start] = [end]
        else:
            num_dict[start].append(end)

        if end not in num_dict:
            num_dict[end] = [start]
        else:
            num_dict[end].append(start)

    while stack:

        start_node = stack.pop()

        if start_node in result:
            continue

        result.append(start_node)
        nodes = [node for node in num_dict[start_node]]
        nodes.sort()

        for node in nodes[::-1]:
            stack.append(node)

    print(f'#{test_case} {" ".join(map(str, result))}')
