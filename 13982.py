import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    n, m = map(int, input().split())
    cheese_lst = list(map(int, input().split()))
    cheese_lst = list(enumerate(cheese_lst))

    print(cheese_lst)

