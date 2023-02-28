import sys
sys.stdin = open("input.txt", "r")

n = int(input())
result = 0

for square_num in range(1, n + 1):

    checker = []

    for check_num in range(1, square_num + 1):

        if check_num in checker:
            continue

        if square_num // check_num == 0:
            result += 1
            checker.append(check_num)
            checker.append(square_num // check_num)

print(result)

