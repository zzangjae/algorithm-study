import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def combination(n, r):
    if n == 0 or n == 1:
        return 1

    if r == 0:
        return 1

    return n / r * combination(n-1, r-1)


for test_case in range(1, t + 1):
    n = int(input())

    print(f'#{test_case}')

    for idx in range(n):

        for r in range(idx + 1):

            print(f'{int(combination(idx, r))}', end = ' ')

        print()

