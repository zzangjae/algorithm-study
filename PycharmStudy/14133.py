import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def do_turn(r, c, color):

    for direction in range(8):
        temp_r, temp_c = r + dr[direction], c + dc[direction]
        stack = []

        while True:

            if not(0 <= temp_r < n) or not(0 <= temp_c < n) or board[temp_r][temp_c] == 0:
                break

            elif board[temp_r][temp_c] == color:
                while stack:
                    temp_r, temp_c = stack.pop()
                    board[temp_r][temp_c] = color
                break

            else:
                stack.append((temp_r, temp_c))
                temp_r += dr[direction]
                temp_c += dc[direction]

    board[r][c] = color


for test_case_num in range(1, t + 1):
    n, m = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(n)]
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]

    for idx in range(n//2 - 1, n//2 + 1):
        board[idx][n - idx - 1] = 1
        board[idx][idx] = 2

    for _ in range(m):
        column, row, color = map(int, input().split())
        column_idx = column - 1
        row_idx = row - 1
        do_turn(row_idx, column_idx, color)

    black = 0
    white = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print(f'#{test_case_num} {black} {white}')







