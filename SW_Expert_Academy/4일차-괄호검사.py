import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    code_lst = list(input())
    stack = []

    for code_chr in code_lst:
        