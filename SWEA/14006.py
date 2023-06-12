import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for tc_num in range(1, t + 1):
    n = int(input())
    sign_ups = []

    for _ in range(n):
        sign_ups.append(tuple(map(int, input().split())))

    start = 0
    result = 0

    while sign_ups:
        temp_e = 25

        for s, e in sign_ups:

            if temp_e > e:
                temp_e = e
                start = s

        result += 1

        temp_sign_ups = []

        for s, e in sign_ups:
            if s >= temp_e:
                temp_sign_ups.append((s, e))

        sign_ups = temp_sign_ups

    print(f'#{tc_num} {result}')
