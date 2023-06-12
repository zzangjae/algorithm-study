import sys

sys.stdin = open("input.txt", "r")

t = int(input())


for test_case in range(1, t + 1):
    n = int(input()) // 10
    num_lst = [1, 3]

    while len(num_lst) < n:
        num_lst.append(num_lst[-1] + num_lst[-2] * 2)

    print(f'#{test_case} {num_lst[n-1]}')
