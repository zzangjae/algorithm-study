import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    test_case_num, n = map(int, input().split())
    num_lst = list(map(int, input().split()))
    way_dict = {}
    check_lst = [1] * 100
    stack = [0]
    result = 0

    for idx in range(0, len(num_lst), 2):
        if num_lst[idx] not in way_dict:
            way_dict[num_lst[idx]] = [num_lst[idx + 1]]
        else:
            way_dict[num_lst[idx]].append(num_lst[idx + 1])

    while stack:

        node = stack.pop()

        if node == 99:
            result = 1
            break

        if node not in way_dict:
            continue

        for next_node in way_dict[node]:
            if check_lst[next_node]:
                stack.append(next_node)
                check_lst[next_node] = 0

    print(f'#{test_case_num} {result}')


