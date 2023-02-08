import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_min_sum(checker, minimum=0, row=0):

    if row == n:
        return minimum

    temp_stack = []

    for idx in range(n):
        if checker[idx] is True:
            temp_checker = checker[:]
            temp_checker[idx] = False
            temp_stack.append(get_min_sum(temp_checker, minimum + num_lst[row][idx], row + 1))

    return min(temp_stack)


for iteration in range(t):
    n = int(input())
    num_lst = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{iteration + 1} {get_min_sum([True] * n)}')