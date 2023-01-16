test_case = int(input())

for iteration in range(test_case):
    num_list = list(map(int, input().split()))
    sum = 0

    for num in num_list:
        if num % 2 == 1:
            sum += num
    
    print(f'#{iteration+1} {sum}')