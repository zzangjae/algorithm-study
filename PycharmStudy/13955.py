import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    v, e = map(int, input().split())
    edge_dict = {}
    queue = [1]
    checker = [True for _ in range(v + 1)]
    checker[1] = False
    result = []

    for _ in range(e):

        node1, node2 = map(int, input().split())
        if node1 not in edge_dict:
            edge_dict[node1] = [node2]

        else:
            edge_dict[node1].append(node2)
            edge_dict[node1].sort()

        if node2 not in edge_dict:
            edge_dict[node2] = [node1]

        else:
            edge_dict[node2].append(node1)
            edge_dict[node2].sort()

    while queue:
        node = queue.pop(0)
        result.append(node)

        for temp_node in edge_dict[node]:
            if checker[temp_node]:
                queue.append(temp_node)
                checker[temp_node] = False

    print(f'#{test_case_num} {" ".join(map(str, result))}')




