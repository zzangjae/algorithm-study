import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):

    n, m, l = map(int, input().split())
    num_lst = list(map(int, input().split()))
    result = -1

    for _ in range(m):
        if len(num_lst) == 0:
            break

        edit = list(input().split())

        if edit[0] == 'I':
            edit[1], edit[2] = int(edit[1]), int(edit[2])
            num_lst.insert(edit[1], edit[2])

        elif edit[0] == 'D':

            edit[1] = int(edit[1])
            del num_lst[edit[1]]

        elif edit[0] == 'C':
            edit[1], edit[2] = int(edit[1]), int(edit[2])
            num_lst[edit[1]] = edit[2]

    if len(num_lst) and len(num_lst) > l:
        print(f'#{test_case} {num_lst[l]}')
    else:
        print(f'#{test_case} {result}')





