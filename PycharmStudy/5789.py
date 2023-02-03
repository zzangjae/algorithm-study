import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):
    n, q = map(int, input().split())
    box_lst = [0] * n

    for i in range(1, q+1):
        l, r = map(int, input().split())
        box_lst[l-1: r] = [i for _ in range(r-l+1)]

    print(f'#{iteration+1} ' + ' '.join(map(str, box_lst)))
