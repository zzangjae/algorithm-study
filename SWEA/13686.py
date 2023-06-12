import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):

    n = int(input())
    price_lst = list(map(int, input().split()))
    temp_max = price_lst[-1]
    result = 0

    for price in price_lst[::-1]:

        if price > temp_max:
            temp_max = price

        elif price < temp_max:
            result += temp_max - price

    print(f'#{test_case} {result}')
