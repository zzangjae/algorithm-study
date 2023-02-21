import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    n = int(input())
    result = -1

    for num in range(1, n + 1):

        temp_result = num ** 3

        if temp_result == n:
            result = num
            break

        elif temp_result > n:
            result = -1
            break

    print(f'#{test_case_num} {result}')
