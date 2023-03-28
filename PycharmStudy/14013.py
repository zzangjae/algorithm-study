import sys
sys.stdin = open('input.txt', 'r')

t = int(input())


def dfs(depth=0, temp_sum=0):

    global result

    if depth == n:
        result = temp_sum

    for idx in range(n):

        if not visit[idx] and temp_sum + cost_lst[depth][idx] < result:
            visit[idx] = True
            dfs(depth + 1, temp_sum + cost_lst[depth][idx])
            visit[idx] = False


for tc_num in range(1, t+1):
    n = int(input())
    cost_lst = [list(map(int, input().split())) for _ in range(n)]
    visit = [False for _ in range(n)]
    result = 100 * 15
    dfs()
    print(f'#{tc_num} {result}')
