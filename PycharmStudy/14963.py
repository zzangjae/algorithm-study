import sys

sys.stdin = open("input.txt", "r")

t = int(input())


def log2n(n, count = 0):

    if n == 1:
        return count

    else:
        return log2n(n//2, count + 1)


def find_idx(num, maximum, minimum=0, count = 0):
    center = (maximum + minimum) // 2

    if count > log_2n + 1:
        return -1

    if num_lst[center] == num:
        return center
    elif num_lst[center] < num:
        return find_idx(num, maximum, center, count + 1)
    else:
        return find_idx(num, center, minimum, count + 1)


for iteration in range(t):
    n, d = map(int, input().split())
    num_lst = list(map(int, input().split()))
    log_2n = log2n(n)

    print(f'#{iteration + 1} {find_idx(d, n) + 1}')
