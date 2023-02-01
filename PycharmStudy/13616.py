import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):

    factor_list = [2, 3, 5, 7, 11]
    num = int(input())

    print(f'#{iteration+1}', end= ' ')

    for factor in factor_list:
        count = 0
        while num % factor == 0:
            count += 1
            num = num / factor
        print(count, end= " ")

    print()