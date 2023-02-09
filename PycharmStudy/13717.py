import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    a, b, = input().split()
    size_a, size_b = len(a), len(b)

    size_a -= a.count(b) * (size_b - 1)

    print(f'#{iteration + 1} {size_a}')