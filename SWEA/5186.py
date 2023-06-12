import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    n = float(input())
    result = []

    for power in range(-1, -13, -1):
        result.append(int(n // (2 ** power)))
        n = n - (2 ** power) * (n // (2 ** power))
        if n % (2 ** power):
            continue
        else:
            break

    if n % (2 ** -13):
        result = 'overflow'

    print(f'#{test_case_num} {"".join(map(str, result))}')


