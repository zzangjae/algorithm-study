def check_case(a_list, b_list):  # a_list 의 길이가 b_list 보다 길게 설계
    len_diff = len(a_list) - len(b_list)
    sum = 0

    for start_index in range(len_diff+1):
        temp_sum = 0

        for index in range(len(b_list)):
            temp_sum += a_list[index+start_index] * b_list[index]
        
        if temp_sum > sum:
            sum = temp_sum

    return sum

def main():
    test_case = int(input())

    for iteration in range(test_case):
        n, m = tuple(map(int, input().split()))
        
        n_list = list(map(int, input().split()))
        m_list = list(map(int, input().split()))

        result = 0

        if n >= m:
            result = check_case(n_list, m_list)
        else:
            result = check_case(m_list, n_list)

        print(f'#{iteration+1} {result}')

main()



            
