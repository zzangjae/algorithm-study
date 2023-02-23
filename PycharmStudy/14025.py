import sys
sys.stdin = open("input.txt", "r")


def get_result(idx= '1'):

    if int(idx) > n:
        return 0

    if tree[idx][0] == operator[0]:
        return get_result(tree[idx][1]) + get_result(tree[idx][2])

    elif tree[idx][0] == operator[1]:
        return get_result(tree[idx][1]) - get_result(tree[idx][2])

    elif tree[idx][0] == operator[2]:
        return get_result(tree[idx][1]) * get_result(tree[idx][2])

    elif tree[idx][0] == operator[3]:
        return get_result(tree[idx][1]) / get_result(tree[idx][2])

    else:
        return int(tree[idx][0])


for test_case_num in range(1, 11):
    n = int(input())
    operator = ['+', '-', '*', '/']
    tree = {}

    for _ in range(n):
        temp_lst = input().split()
        tree[temp_lst[0]] = temp_lst[1:]

    print(f'#{test_case_num} {int(get_result())}')
