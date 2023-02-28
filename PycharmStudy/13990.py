import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for tc_num in range(1, t+1):
    n = float(input())
    result = []
    while n > 0:

        if len(result) > 12:
            result = ['overflow']
            break

        result.append(int(n // 2 ** (-1 * len(result) - 1)))
        n = n % (2 ** (-1 * len(result)))

    print(f'#{tc_num} {"".join(map(str, result))}')
