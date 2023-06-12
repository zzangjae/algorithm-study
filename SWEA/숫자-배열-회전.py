def turn_90(num_list):

    temp_list = []

    for column in range(len(num_list)):
        temp_list.append(get_column(num_list, column))

    return temp_list


def get_column(num_list, column_index):
    column_list = []
    length = len(num_list)
    for row in range(length):
        column_list.append(num_list[length-row-1][column_index])
    return column_list


def main():
    test_case = int(input())

    for case_num in range(test_case):

        print(f'#{case_num+1}')
        n = int(input())

        num_list = []
        for _ in range(n):
            num_list.append(list(map(int, input().split())))
        
        turned_90 = turn_90(num_list)
        turned_180 = turn_90(turned_90)
        turned_270 = turn_90(turned_180)

        for row in range(n):
            turned_90_str = ''
            turned_180_str = ''
            turned_270_str = ''
            for column in range(n):
                turned_90_str += str(turned_90[row][column])
                turned_180_str += str(turned_180[row][column])
                turned_270_str += str(turned_270[row][column])

            print(turned_90_str, turned_180_str, turned_270_str)

main()


