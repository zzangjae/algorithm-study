import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

for tc_num in range(1, t+1):
    n, m, k = map(int, input().split())
    customer_lst = [0] * 11112
    customer_time_lst = list(map(int, input().split()))

    for customer_idx in customer_time_lst:
        customer_lst[customer_idx] += 1

    bread = 0
    time = 0
    customer = len(customer_time_lst)
    result = 'Possible'

    while customer:

        while customer_lst[time]:
            bread -= 1
            customer_lst[time] -= 1
            customer -= 1

        if bread < 0:
            result = 'Impossible'
            break

        time += 1

        if time % m == 0:
            bread += k

    print(f'#{tc_num} {result}')