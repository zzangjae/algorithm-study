import sys
sys.stdin = open("input.txt", "r")

# t = int(input())
# for test_case_num in range(1, t + 1):

n = int(input())
num_lst = list(map(int, input().split()))
result_lst = []

for idx in range(1, n + 1):

    result_lst.insert((len(result_lst) - num_lst[idx - 1]), idx)

print(" ".join(map(str, result_lst)))
