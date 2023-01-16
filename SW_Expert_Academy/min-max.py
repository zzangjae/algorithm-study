test_case = int(input())

for iteration in range(test_case):

    n = int(input())

    num_list = list(map(int, input().split()))
    num_list_max = max(num_list)
    num_list_min = min(num_list)

    print(f'#{iteration+1} {num_list_max-num_list_min}')

