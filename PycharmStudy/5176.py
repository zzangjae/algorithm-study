import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def dfs(idx):

    global number

    if idx <= n:

        dfs(idx * 2)

        tree[idx] = number
        number += 1

        dfs(idx * 2 + 1)


for test_case_num in range(1, t + 1):
    n = int(input())
    tree = [0 for _ in range(n + 1)]
    number = 1
    dfs(1)

    print(f'#{test_case_num} {tree[1]} {tree[n//2]}')