import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

for iteration in range(T):
    n, m = map(int, input().split())
    num_lst = list(map(int, input().split()))
    temp_sum = sum(num_lst[:m])
    max = temp_sum
    min = temp_sum

    for idx in range(n-m):
        temp_sum += num_lst[idx+m] - num_lst[idx]
        if max < temp_sum:
            max = temp_sum
        if min > temp_sum:
            min = temp_sum

    print(f'#{iteration+1} {max - min}')