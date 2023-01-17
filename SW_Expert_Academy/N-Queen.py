def find_queen(grid, queen_list = []):
    size = len(grid)
    column = len(queen_list)
    global result
    
    if column == size:
        result += 1

    for queen_num in range(size):
        if grid[queen_num] == 0:
            temp_queen_list = queen_list[:]
            temp_queen_list.append((column, queen_num))
            find_queen(get_grid(temp_queen_list, size, column+1), temp_queen_list)


def get_grid(queen_list, size, column):
    grid = [0 for _ in range(size)]

    for tuple in queen_list:
        grid[tuple[1]] = 1
        if tuple[1] - column + tuple[0] >= 0:
            grid[tuple[1] - column + tuple[0]] = 1
        if tuple[1] + column - tuple[0] < size:
            grid[tuple[1] + column - tuple[0]] = 1
    
    return grid

n = int(input())
grid = [0 for _ in range(n)]
result = 0

find_queen(grid)
print(result)

        