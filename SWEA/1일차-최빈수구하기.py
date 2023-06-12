def get_score_distribution(math_score_list):

    temp_list = [0]*101

    for score in math_score_list:
        temp_list[score] += 1

    return temp_list

def get_maxi_distribution(score_distribution):
    max = 0
    max_index = 0
    
    for index in range(101):
        if score_distribution[index] >= max:
            max = score_distribution[index]
            max_index = index
    
    return max_index
        
    
def main():
    test_case = int(input())

    for _ in range(test_case):
        case_num = int(input())
        result = 0

        math_score_list = list(map(int, input().split()))
        result = get_maxi_distribution(get_score_distribution(math_score_list))

        print(f'#{case_num} {result}')

main()