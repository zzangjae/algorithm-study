import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    n = int(input())
    queue = []

    for _ in range(n):
        alphabet, num = input().split()
        queue.extend([alphabet] * int(num))

    print(f'#{iteration + 1}')

    count = 0
    while queue:
        count += 1

        if count == 10:
            print(queue.pop(0))
            count = 0
        else:
            print(queue.pop(0), end='')

    print()



