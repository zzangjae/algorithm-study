import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    n, m = map(int, input().split())
    num_lst = list(map(int, input().split()))
    m = m % n

    print(f'#{test_case_num} {num_lst[m]}')
