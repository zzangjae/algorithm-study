import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    n, m = map(int, input().split())
    front = m % n
    num_lst = list(map(int, input().split()))

    print(f'#{iteration + 1} {num_lst[front]}')

