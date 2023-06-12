def get_sudoku():
    sudoku = []
    for line in range(9):
        sudoku.append(list(map(int, input().split())))
    return sudoku


def get_column_sudoku(sudoku, column_index):
    return sudoku[column_index]
    
            
def get_row_sudoku(sudoku, row_index):
    row_list = []
    for column in range(9):
        row_list.append(sudoku[column][row_index])
    return row_list
    
    
def get_box_sudoku(sudoku, column_box_num, row_box_num):
    # sudoku 를 9개의 box로 분할하여 각각 column_box_num, row_box_num으로 구분함 
    box_list = []
    
    for column in range((column_box_num-1)*3, column_box_num*3):
        for row in range((row_box_num-1)*3, row_box_num*3):
            box_list.append(sudoku[column][row])
            
    return box_list
    

def check_numbers(num_list):
    for num in range(1, 10):
        if num not in num_list:
            return False
    else:
        return True
        
def check_column_sudoku(sudoku):
    for column_num in range(9):
        column_list = get_column_sudoku(sudoku, column_num)
        if not check_numbers(column_list):
            return False
    else:
        return True
        
        
def check_row_sudoku(sudoku):
    for row_num in range(9):
        row_list = get_row_sudoku(sudoku, row_num)
        if not check_numbers(row_list):
            return False
    else:
        return True
        
def check_box_sudoku(sudoku):
    for box_column_num in range(3):
        for box_row_num in range(3):
            box_list = get_box_sudoku(sudoku, box_column_num, box_row_num)
        if not check_numbers(box_list):
            return False
    else:
        return True
        
        
            
test_case = int(input())

for number in range(test_case):
    sudoku = get_sudoku()
    if check_column_sudoku(sudoku) and check_row_sudoku(sudoku) and check_box_sudoku(sudoku):
        print("#{} 1".format(number+1))
    else:
        print("#{} 0".format(number+1))