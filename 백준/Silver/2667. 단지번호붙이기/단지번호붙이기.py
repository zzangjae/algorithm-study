"""
# 문제: 단지 번호 붙이기

## 조건
- 1초, 128MB
- 지도의 크기 n, 5 <= n <= 25
___

## idea
- 상하좌우로 dfs로 탐색하여 하나의 단지를 확정 짓는다. 각각의 집을 방문할 때 마다 is_visited로 방문 여부 체크한다.
    한번 방문하였다면 다시 방문할 필요가 없음이 보장된다. 또한 위 방법으로는 최대 25 * 25 * 4 번 방문함이 보장된다.
___

## solution
1. n을 입력받고, 정사각형 모양의 지도를 입력받는다.
2. is_visited, result_lst와 dfs 재귀함수를 선언한다.
    dfs:
    방문 여부를 갱신한다.
    상하좌우로 집이 있는지 확인한다.
    집이 있다면 해당 집을 기준으로 dfs를 돌린다.
    총 집의 개수를 반환하고 결과 result_lst에 추가한다.
3. 이중 for문을 돌려 방문했을경우 continue 미방문시 dfs를 돌린다.
4. result_lst를 오름차순으로 정렬하고 순서대로 출력한다.
"""

# 1. n을 입력받고, 정사각형 모양의 지도를 입력받는다.
n = int(input())
house_map = [list(map(int, list(input()))) for _ in range(n)]


# 2. is_visited, result_lst와 dfs 재귀함수를 선언한다.
visited = [[False for _ in range(n)] for _ in range(n)]
result_lst = []


def dfs(r, c):

    visited[r][c] = True

    result = 1

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:

        if not 0 <= r + dr < n or not 0 <= c + dc < n:
            continue

        if house_map[r+dr][c+dc] and not visited[r + dr][c + dc]:
            visited[r + dr][c + dc] = True
            result += dfs(r+dr, c+dc)

    return result


# 3. 이중 for문을 돌려 방문했을경우 continue 미방문시 dfs를 돌린다.
for i in range(n):
    for j in range(n):
        if not visited[i][j] and house_map[i][j]:
            result_lst.append(dfs(i, j))

# 4. result_lst를 오름차순으로 정렬하고 순서대로 출력한다.
result_lst.sort()

print(len(result_lst))

for result in result_lst:
    print(result)