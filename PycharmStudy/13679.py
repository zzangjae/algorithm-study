import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_mbym(row, column):
    temp_lst = []

    for i in range(m):
        for j in range(m):
            temp_lst.append(num_lst[i+row][j+column])

    return temp_lst


for iteration in range(t):
    n, m = map(int, input().split())
    num_lst = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for row in range(n-m+1):
        for column in range(n-m+1):
            temp_result = sum(get_mbym(row, column))

            if temp_result > result:
                result = temp_result

    print(f'#{iteration + 1} {result}')