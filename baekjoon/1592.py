import sys
sys.stdin = open("input.txt", "r")

n, m, l = map(int, input().split())
ball_position_lst = [0] * n
idx = 0
counter = 0

while True:

    ball_position_lst[idx] += 1

    if ball_position_lst[idx] == m:
        break

    elif ball_position_lst[idx] % 2:
        idx = (idx + l) % n

    else:
        idx = (idx - l) if idx - l >= 0 else n + (idx - l)

    counter += 1

print(counter)


