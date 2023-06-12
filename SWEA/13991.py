import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

def get_min(num_sum, r=0, c=0):

    if r+1 < n and visit[r+1][c] > num_sum + map_lst[r+1][c]:
        visit[r+1][c] = num_sum + map_lst[r+1][c]
        get_min(num_sum + map_lst[r+1][c], r+1, c)

    if c+1 < n and visit[r][c+1] > num_sum + map_lst[r][c+1]:
        visit[r][c+1] = num_sum + map_lst[r][c+1]
        get_min(num_sum + map_lst[r][c+1], r, c+1)


for tc_num in range(1, t+1):
    n = int(input())
    map_lst = [list(map(int, input().split())) for _ in range(n)]
    visit = [[1000 for _ in range(n)] for _ in range(n)]
    get_min(map_lst[0][0])
    print(f'#{tc_num} {visit[n-1][n-1]}')

