import sys
sys.stdin = open("input.txt", "r")

for test_case_num in range(1, 11):
    n, start_node = map(int, input().split())
    edge_lst = list(map(int, input().split()))
    edge_dict = {}
    queue = [start_node]
    checker = [0] * 101
    checker[start_node] = 1

    for idx in range(n//2):
        node1, node2 = edge_lst[idx * 2], edge_lst[idx * 2 + 1]

        if node1 not in edge_dict:
            edge_dict[node1] = [node2]

        else:
            edge_dict[node1].append(node2)

    while queue:
        node = queue.pop(0)
        counter = checker[node]

        if node not in edge_dict:
            continue

        for temp_node in edge_dict[node]:

            if not checker[temp_node]:
                checker[temp_node] = counter + 1
                queue.append(temp_node)

    max_checker = max(checker)
    for idx in range(100, -1, -1):
        if checker[idx] == max_checker:
            result = idx
            break

    print(f'#{test_case_num} {result}')


