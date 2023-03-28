import sys
sys.stdin = open('input.txt', 'r')

n, l, r = map(int, input().split())
country_lst = [list(map(int, input().split())) for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]
count = 1

for i in range(n):
    for j in range(n):

        if not visit[i][j]:
            stack = []

