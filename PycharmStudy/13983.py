import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    v, e = map(int, input().split())
    graph_dict = {}

    for _ in range(e):
        node1, node2 = map(int, input().split())

        if node1 not in graph_dict:
            graph_dict[node1] = [node2]
        else:
            graph_dict[node1].append(node2)

        if node2 not in graph_dict:
            graph_dict[node2] = [node1]
        else:
            graph_dict[node2].append(node1)

    s, g = map(int, input().split())
    depth = 0
    queue = [(s, 0)]
    visited = [True] * (v + 1)
    result = 0

    while queue:
        node, depth = queue.pop(0)
        visited[node] = False

        if node == g:
            result = depth
            break

        if node not in graph_dict:
            break

        for temp_node in graph_dict[node]:
            if visited[temp_node]:
                queue.append((temp_node, depth + 1))

    print(f'#{test_case_num} {result}')