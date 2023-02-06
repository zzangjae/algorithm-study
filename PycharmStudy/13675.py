import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def find_set(set_sum = 0, count = 0, idx = 0):

    if count == n and set_sum == k:
        return 1

    if idx == 12:
        return 0

    return find_set(set_sum + a[idx], count + 1, idx + 1) +\
           find_set(set_sum, count, idx + 1)


for iteration in range(T):
    n, k = map(int, input().split())
    a = list(range(1, 13))
    result = 0
    result = find_set()

    print(f'#{iteration+1} {result}')



