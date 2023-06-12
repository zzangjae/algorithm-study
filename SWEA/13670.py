'''
Idea
    재귀를 이용하여 모든 부분집합의 합을 점검해보자

Solution
    1) idx == size 일 경우 종료, 합이 0일 경우 종료

    2) idx에 해당하는 원소를 더하거나 더하지 않고 합하고 1)을 반복
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def dfs(num_sum, idx):

    if num_sum == 0 and idx > 0:
        return 1
    elif idx == size:
        return 0

    return dfs(num_sum + num_lst[idx], idx + 1) + dfs(num_sum, idx + 1)


for iteration in range(T):

    num_lst = list(map(int, input().split()))
    size = len(num_lst)
    result = 1 if dfs(0, 0) > 1 else 0

    print(f'#{iteration+1} {result}')
