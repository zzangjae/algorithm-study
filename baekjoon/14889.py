import sys

input = sys.stdin.readline

def get_result(idx=0, depth=0):
    global result

    if depth == n//2:
        temp_result = 0

        for i in range(n):
            for j in range(i+1, n):
                if visit[i] and visit[j]:
                    temp_result += power_lst[i][j] + power_lst[j][i]
                elif not visit[i] and not visit[j]:
                    temp_result -= power_lst[i][j] + power_lst[j][i]

        result = min(result, abs(temp_result))

    for i in range(idx, n):
        if visit[i]:
            visit[i] = False
            get_result(idx+1, depth+1)
            visit[i] = True


n = int(input())
result = 10000000000
power_lst = [list(map(int, input().split())) for _ in range(n)]
visit = [True]*n
get_result()
print(result)