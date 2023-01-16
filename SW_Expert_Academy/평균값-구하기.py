test_case = int(input())

for iteration in range(test_case):

    num_list = list(map(int, input().split()))
    sum = 0

    for num in num_list:
        sum += num
    
    mean = round(sum/len(num_list))

    print(f'#{iteration+1} {mean}')
