import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def dfs(start):
    if g in graph[start]:
        return 1

    val = 0

    for next_start in graph[start]:
        if next_start in graph:
            val += dfs(next_start)

    return val


for iteration in range(t):
    v, e = map(int, input().split())
    graph = {}
    result = 0

    for _ in range(e):
        start, end = map(int, input().split())

        if start not in graph:
            graph[start] = [end]
        else:
            graph[start].append(end)

    s, g = map(int, input().split())
    if s not in graph:
        result = 0
    else:
        temp_result = dfs(s)
        result = temp_result if temp_result == 0 else 1

    print(f'#{iteration + 1} {result}')




