import sys
sys.stdin = open('input.txt', 'r')

t = int(input())


def get_min(depth=0, cost=0, start=0):

    if depth == n-1:
        return cost + cost_lst[start][0]

    temp_lst = []

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            temp_lst.append(get_min(depth+1, cost+cost_lst[start][i], i))
            visit[i] = False

    return min(temp_lst)


for tc_num in range(1, t+1):
    n = int(input())
    cost_lst = [list(map(int, input().split())) for _ in range(n)]
    visit = [False for _ in range(n)]
    visit[0] = True
    print(f'#{tc_num} {get_min()}')