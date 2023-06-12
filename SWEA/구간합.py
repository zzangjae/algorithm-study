test_case = int(input())

for iteration in range(test_case):
    
    n, m = tuple(map(int, input().split()))
    num_list = list(map(int, input().split()))
    max_sum = 0
    min_sum = 1000000

    for start_index in range(n-m+1):

        temp_sum = sum(num_list[start_index: m+start_index])
        
        if max_sum < temp_sum:
            max_sum = temp_sum
        
        if min_sum > temp_sum:
            min_sum = temp_sum
    
    print(f'#{iteration+1} {max_sum-min_sum}')
            
