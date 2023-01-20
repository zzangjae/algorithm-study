n, m = map(int, input().split())

def make_board():
    board = []

    for _ in range(n):
        board.append(list(input()))

    return board


def get_red_index(board):

    for y_index in range(n):
        for x_index in range(m):
            if board[y_index][x_index] == 'R':
                return [x_index, y_index]


def get_blue_index(board):

    for y_index in range(n):
        for x_index in range(m):
            if board[y_index][x_index] == 'B':
                return [x_index, y_index]

def get_hole_index(board):

    for y_index in range(n):
        for x_index in range(m):
            if board[y_index][x_index] == 'O':
                return [x_index, y_index]


board = make_board()
red_index = get_red_index(board)
blue_index = get_blue_index(board)
hole_index = get_hole_index(board)


def move_red(direction):
    global red_index
    direction_dict = {'up' : (-1, 0), 'down' : (1, 0), 'right' : (0, 1), 'left' : (0, -1)}
    dy = direction_dict[direction][0]
    dx = direction_dict[direction][1]
    x, y = red_index

    if board[y + dy][x + dx] == '#':
        return False
    elif board[y + dy][x + dx] == 'B':
        return False
    elif board[y + dy][x + dx] == '.':
        board[y][x] = '.'
        red_index = [x + dx, y + dy]
        board[y + dy][x + dx] = 'R'
        return True
    else:
        board[y][x] = '.'
        red_index = [x + dx, y + dy]
        return False


def move_blue(direction):
    global blue_index
    direction_dict = {'up' : (-1, 0), 'down' : (1, 0), 'right' : (0, 1), 'left' : (0, -1)}
    dy = direction_dict[direction][0]
    dx = direction_dict[direction][1]
    x, y = blue_index

    if board[y + dy][x + dx] == '#':
        return False
    elif board[y + dy][x + dx] == 'R':
        return False
    elif board[y + dy][x + dx] == '.':
        board[y][x] = '.'
        blue_index = [x + dx, y + dy]
        board[y + dy][x + dx] = 'B'
        return True
    else:
        board[y][x] = '.'
        blue_index = [x + dx, y + dy]
        return False


def tilt_board(direction):
    global board

    while True:
        if red_index != hole_index:
            red_bool = move_red(direction)
        else:
            red_bool = False

        if blue_index != hole_index:
            blue_bool = move_blue(direction)
        else:
            blue_bool = False
        
        if not(red_bool or blue_bool):
            break
    
    return None


def find_path():
    global red_index
    direction_dict = {'up' : (-1, 0), 'down' : (1, 0), 'right' : (0, 1), 'left' : (0, -1)}
    x, y = red_index
    path = []

    for direction in direction_dict:
        dy = direction_dict[direction][0]
        dx = direction_dict[direction][1]

        if board[y + dy][x + dx] == '.':
            path.append(direction)
        elif board[y + dy][x + dx] == 'B':
            path.append(direction)

    return path


def isfinished():
    if red_index == hole_index or blue_index == hole_index:
        return True
    else:
        False


def iswin():
    if red_index == hole_index and blue_index == hole_index:
        return False
    elif blue_index == hole_index:
        return False
    elif red_index == hole_index:
        return True


def make_boardcopy(board):
    temp_board = []
    
    for row in board:
        temp_board.append(row[:])
    
    return temp_board

count = 0
min_count = 11
path_stack = [[] for _ in range(10)]
board_list = [0] * 10


while True:
    if count == 0 and min_count < 11:
        print(min_count)
        break
    elif count == 0 and min_count == 11:
        print(-1)
        break

    if path_stack[count] == []:
        path_stack[count] = find_path()
        continue
    else:
        if board_list[count] == 0:
            board_list[count] = make_boardcopy(board)
        
        tilt_board[path_stack[count][0]]
        del path_stack[count][0]

        

    


# while True:
#     print('which direction you gonna move?')
#     tilt_board(input())
#     print(find_path())
#     for _ in board:
#         print(_)
#     if red_index == hole_index or blue_index == hole_index:
#         print('gone to the hole')
    

        

    


