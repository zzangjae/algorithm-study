def get_diagonal(case_list):

    temp_list = []
    
    for index in range(100):
            temp_list.append(case_list[index][index])

    return temp_list

def get_reverse_diagonal(case_list):

    temp_list = []
    
    for index in range(100):
            temp_list.append(case_list[99-index][index])

    return temp_list

def get_column(case_list, column):
    return case_list[column]

def get_row(case_list, row):
    
    temp_list = []

    for column in range(100):
        temp_list.append(case_list[column][row])

    return temp_list

def get_sum(num_list):
    
    temp_sum = 0

    for num in num_list:
        temp_sum += num

    return temp_sum

def get_caselist():

    temp_caselist = []

    for _ in range(100):
        temp_caselist.append(list(map(int, input().split())))

    return temp_caselist


def main():
    for _ in range(10):
        
        tc_num = int(input())
        result = 0
        case_list = get_caselist()

        for index in range(100):
            column_sum = get_sum(get_column(case_list, index))
            row_sum = get_sum(get_row(case_list, index))

            if column_sum > result:
                result = column_sum

            if row_sum > result:
                result = row_sum

        diagonal_sum = get_sum(get_diagonal(case_list))
        rev_diagonal_sum = get_sum(get_reverse_diagonal(case_list))

        if diagonal_sum > result:
            result = diagonal_sum
        
        if rev_diagonal_sum > result:
            result = rev_diagonal_sum

        print(f'#{tc_num} {result}')

main()




