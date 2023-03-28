import sys
sys.stdin = open('input.txt', 'r')

t = int(input())


def get_result(depth=0, temp_sum=0, start=0):

    global result

    if temp_sum == k:
        result += 1
        return

    if depth == n:
        return

    for idx in range(start, n):

        if not visit[idx] and temp_sum + num_lst[idx] <= k:
            visit[idx] = True
            get_result(depth + 1, temp_sum + num_lst[idx], idx)
            visit[idx] = False


for tc_num in range(1, t+1):
    n, k = map(int, input().split())
    num_lst = list(map(int, input().split()))
    visit = [False for _ in range(n)]
    result = 0
    get_result()
    print(f'#{tc_num} {result}')