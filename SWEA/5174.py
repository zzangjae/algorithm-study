import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    e, n = map(int, input().split())
    tree_dict = {}
    num_lst = list(map(int, input().split()))

    for idx in range(e):
        parent, child = num_lst[idx * 2], num_lst[idx * 2 + 1]
        if parent in tree_dict:
            tree_dict[parent].append(child)
        else:
            tree_dict[parent] = [child]

    result = 0
    stack = [n]

    while stack:

        parent = stack.pop()

        if parent in tree_dict:
            for child in tree_dict[parent]:
                stack.append(child)

        result += 1

    print(f'#{test_case_num} {result}')