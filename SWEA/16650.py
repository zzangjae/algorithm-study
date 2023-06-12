import sys
sys.stdin = open("input.txt", "r")
t = int(input())

for test_case_num in range(1, t + 1):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    result = [0, 0, 0]

    for _ in range(n):
        x, y = map(int, input().split())

        if x1 <= x <= x2 and y1 <= y <= y2:

            if x == x1 or x == x2 or y == y1 or y == y2:
                result[1] += 1
            else:
                result[0] += 1

        else:
            result[2] += 1

    print(f'#{test_case_num} {" ".join(map(str, result))}')