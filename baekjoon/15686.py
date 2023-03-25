import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
city_lst = [list(map(int, input().split())) for _ in range(n)]
chicken_house = []
normal_house = []

for i in range(n):
    for j in range(n):
        if city_lst[i][j] == 1:
            normal_house.append((i, j))

        elif city_lst[i][j] == 2:
            chicken_house.append((i, j))

visit = [False] * len(chicken_house)
minimum = 100000000


def dfs(depth=0, idx=0):

    if depth == m:
        global minimum
        result = 0

        for house in normal_house:
            temp_result = 100

            for idx in range(len(chicken_house)):
                if visit[idx]:
                    temp_distance = 0
                    temp_distance += abs(chicken_house[idx][0] - house[0])
                    temp_distance += abs(chicken_house[idx][1] - house[1])

                    if temp_result > temp_distance:
                        temp_result = temp_distance

            result += temp_result

            if result > minimum:
                return

        if minimum > result:
            minimum = result

    for i in range(idx, len(chicken_house)):
        visit[i] = True
        dfs(depth+1, i+1)
        visit[i] = False

dfs()
print(minimum)



