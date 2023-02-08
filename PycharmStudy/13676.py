import sys

sys.stdin = open("input.txt", "r")

t = int(input())


def log2n(n, count = 0):

    if n == 1:
        return count

    else:
        return log2n(n//2, count + 1)


def find_idx(num, maximum, minimum=1, count = 0):
    center = (maximum + minimum) // 2

    if count > log_2n + 1:
        return -1

    if num_lst[center] == num:
        return count
    elif num_lst[center] < num:
        return find_idx(num, maximum, center, count + 1)
    else:
        return find_idx(num, center, minimum, count + 1)


for iteration in range(t):
    p, a, b = map(int, input().split())
    num_lst = range(p)
    log_2n = log2n(p)

    result_a = find_idx(a, p)
    result_b = find_idx(b, p)
    print(result_a, result_b)

    if result_a == result_b:
        result = 0
    elif result_a > result_b:
        result = 'B'
    else:
        result = 'A'

    print(f'#{iteration + 1} {result}')
