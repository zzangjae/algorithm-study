import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_ksum_num(ksum=0, idx=0):

    if ksum == k:
        return 1

    if idx == n:
        return 0

    return get_ksum_num(ksum + num_lst[idx], idx + 1) + get_ksum_num(ksum, idx + 1)


for test_case_num in range(1, t + 1):
    n, k = map(int, input().split())
    num_lst = list(map(int, input().split()))
    print(f'#{test_case_num} {get_ksum_num()}')
