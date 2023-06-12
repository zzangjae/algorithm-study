import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):
    n, m = map(int, input().split())

    n_lst = list(map(int, input().split()))
    m_lst = list(map(int, input().split()))

    max_sum = None

    if n >= m:

        for i in range(n-m+1):
            temp_sum = 0

            for j in range(i, m+i):
                temp_sum += n_lst[j] * m_lst[j-i]

            if max_sum is None or max_sum < temp_sum:
                max_sum = temp_sum

    else:

        for i in range(m-n+1):
            temp_sum = 0

            for j in range(i, n+i):
                temp_sum += n_lst[j-i] * m_lst[j]

            if max_sum is None or max_sum < temp_sum:
                max_sum = temp_sum

    print(f'#{iteration+1} {max_sum}')
