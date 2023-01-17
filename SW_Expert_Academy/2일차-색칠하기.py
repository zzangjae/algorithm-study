def color_grid(color_info, grid):
    
    for column in range(color_info[0], color_info[2]+1):
        for row in range(color_info[1], color_info[3]+1):
            if grid[column][row] == 1 and color_info[4] == 2:
                grid[column][row] = 3
            elif grid[column][row] == 2 and color_info[4] == 1:
                grid[column][row] = 3
            else:
                grid[column][row] = color_info[4]

def main():
    test_case = int(input())
    for iteration in range(test_case):

        n = int(input())
        grid = [[0 for _ in range(10)] for _ in range(10)]
        result = 0

        for _ in range(n):
            color_info = list(map(int, input().split()))
            color_grid(color_info, grid)

        for column in grid:
            result += column.count(3)
        
        print(f'#{iteration+1} {result}')


main()
