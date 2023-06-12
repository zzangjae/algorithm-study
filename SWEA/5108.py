import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):

    n, m, l = map(int, input().split())
    num_lst = list(map(int, input().split()))

    for _ in range(m):
        idx, num = map(int, input().split())
        num_lst.insert(idx, num)

    print(f'#{iteration + 1} {num_lst[l]}')

