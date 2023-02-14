import sys
sys.stdin = open("input.txt", "r")


def get_power(n, m):
    if m == 1:
        return n

    return n * get_power(n, m - 1)


for test_case in range(1, 11):
    t = int(input())
    n, m = map(int, input().split())

    print(f'#{test_case} {get_power(n, m)}')
