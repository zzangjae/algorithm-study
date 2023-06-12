import sys
sys.stdin = open("input.txt", "r")

for test_case_num in range(1, 11):
    n = int(input())
    maze_lst = [list(map(int, list(input()))) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if maze_lst[i][j] == 2:
                r, c = i, j

    queue = [(r, c)]
    visit = [[True for _ in range(100)] for _ in range(100)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    result = 0

    while queue:
        row, column = queue.pop(0)
        visit[row][column] = False

        if maze_lst[row][column] == 3:
            result = 1
            break

        for dr, dc in directions:

            if 0 <= row + dr < 100 and 0 <= column + dc < 100 and\
                    visit[row + dr][column + dc] and\
                    maze_lst[row + dr][column + dc] != 1:
                queue.append((row + dr, column + dc))

    print(f'#{test_case_num} {result}')


