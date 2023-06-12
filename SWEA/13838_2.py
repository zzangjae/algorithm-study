import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    equation_lst = list(input())
    stack = []
    result = []

# 우선순위를 생각해서 짜보자...시간될때
