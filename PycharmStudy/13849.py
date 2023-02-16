import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_min_sum(checker, row=0, temp_sum=0):

    global min_sum

    if row == n:
        if temp_sum < min_sum:
            min_sum = temp_sum

    else:
        for idx in range(n):
            if checker[idx] and temp_sum + num_lst[row][idx] < min_sum:
                temp_checker = checker[:]
                temp_checker[idx] = False
                get_min_sum(temp_checker, row + 1, temp_sum + num_lst[row][idx])


for test_case_num in range(1, t + 1):
    n = int(input())
    num_lst = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 100
    get_min_sum([True] * n)

    print(f'#{test_case_num} {min_sum}')
