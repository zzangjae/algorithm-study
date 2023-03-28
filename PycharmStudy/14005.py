import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for tc_num in range(1, t + 1):
    n, m = map(int, input().split())
    w_lst = list(map(int, input().split()))
    t_lst = list(map(int, input().split()))

    w_lst.sort(reverse=True)
    t_lst.sort(reverse=True)
    result = 0
    start_w = 0

    for t_idx in range(m):
        for w_idx in range(start_w, n):
            if w_lst[w_idx] <= t_lst[t_idx]:
                start_w = w_idx + 1
                result += w_lst[w_idx]
                break

    print(f'#{tc_num} {result}')
