from collections import deque
from sys import stdin
input = stdin.readline

y, x = map(int, input().split())
visit = [[[[False] * y for _ in range(x)] for _ in range(y)] for _ in range(x)]
board = []

for row in range(y):
    board.append(list(input()))    

for row in range(y):
    for column in range(x):
        if board[row][column] == 'R':
            red_x, red_y = column, row
        elif board[row][column] == 'B':
            blue_x, blue_y = column, row
        elif board[row][column] == 'O':
            hole_x, hole_y = column, row


def move(ball_x, ball_y, dx, dy, count):
    while board[ball_x + dx][ball_y + dy] != '#' and board[ball_x + dx][ball_y + dy] != 'O':
        return move(ball_x + dx, ball_y + dy, dx, dy, count + 1)
    return ball_x, ball_y, count

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(red_x, red_y, blue_x, blue_y, count):
    bfs_stack = deque()
    bfs_stack.append([red_x, red_y, blue_x, blue_y, count])
    visit[red_x][red_y][blue_x][blue_y] = True
    
    while bfs_stack:

        red_x, red_y, blue_x, blue_y, count = bfs_stack.popleft()

        if count > 10:
            break

        for i in range(4):
            moved_red_x, moved_red_y, red_move_count = move(red_x, red_y, dx[i], dy[i], 0)
            moved_blue_x, moved_blue_y, blue_move_count = move(blue_x, blue_y, dx[i], dy[i], 0)

            if board[moved_blue_x][moved_blue_y] != 'O':
                if board[moved_red_x][moved_red_y] != 'O':
                    print(count)
                    return
                if moved_blue_x == moved_red_x and moved_blue_y == moved_red_y:
                    if red_move_count > blue_move_count:
                        moved_red_x -= dx[i]
                        moved_red_y -= dy[i]
                    else:
                        moved_blue_x -= dx[i]
                        moved_blue_y -= dy[i]

                if not visit[moved_red_x][moved_red_y][moved_blue_x][moved_blue_y]:
                    visit[moved_red_x][moved_red_y][moved_blue_x][moved_blue_y] = True
                    bfs_stack.append([moved_red_x, moved_red_y, moved_blue_x, moved_blue_y, count+1])
                    print(bfs_stack)
        
    print(-1)



    # if count > 10:
    #     return -1

    # if (red_x, red_y) == (hole_x, hole_y) and (blue_x, blue_y) != (hole_x, hole_y):
    #     return count

    # if len(bfs_stack) != 0:
    #     if not(checker[red_x][red_y][blue_x][blue_y]):
    
    # if not(checker[red_x][red_y][blue_x][blue_y]):
    #     checker[red_x][red_y][blue_x][blue_y] = True

    #     for i, j in zip(dx, dy):
    #         moved_red_x, moved_red_y, red_move_count = move(red_x, red_y, i, j, 0)
    #         moved_blue_x, moved_blue_y, blue_move_count = move(blue_x, blue_y, i, j, 0)

    #         if (moved_red_x, moved_red_y) == (moved_blue_x, moved_blue_y):
    #             if red_move_count > blue_move_count:
    #                 moved_red_x -= i
    #                 moved_red_y -= j
    #             else:
    #                 moved_blue_x -= i
    #                 moved_blue_y -= j

    #         bfs_stack.append([moved_red_x, moved_red_y, moved_blue_x, moved_blue_y])


bfs(red_x, red_y, blue_x, blue_y, 1)




