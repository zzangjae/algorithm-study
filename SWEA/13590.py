import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):

    k, n, m = map(int, input().split())
    charger_lst = list(map(int, input().split()))

    result = 0
    idx = 0

    while idx < n - k:
        for charger_num in range(idx+k, idx, -1):
            if charger_num in charger_lst:
                idx = charger_num
                result += 1
                break
        else:
            result = 0
            break

    print(f'#{iteration+1} {result}')

