import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000)

n, l, r = map(int, input().split())
population_lst = [list(map(int, input().split())) for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 0
checker = True


def get_union(row, column, visit_lst = []):

    if visit[row][column]:
        return []

    visit[row][column] = True
    visit_lst.append((row, column))

    for dr, dc in directions:

        tr, tc = row + dr, column + dc

        if 0 <= tr < n and 0 <= tc < n and not visit[tr][tc] and\
            l <= abs(population_lst[row][column] - population_lst[tr][tc]) <= r:
            get_union(tr, tc, visit_lst)

    return visit_lst


while checker:
    visit = [[False for _ in range(n)] for _ in range(n)]
    checker = 0

    for i in range(n):
        for j in range(n):
            temp_union = get_union(i, j, [])
            temp_sum = 0

            if len(temp_union) > 1:
                checker += 1

                for union in temp_union:
                    temp_sum += population_lst[union[0]][union[1]]

                for union in temp_union:
                    population_lst[union[0]][union[1]] = int(temp_sum / len(temp_union))

    if checker > 0:
        result += 1

print(result)







