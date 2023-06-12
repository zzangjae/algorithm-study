import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):
    d, a, b, f = map(int, input().split())

    print(f'#{iteration+1} {(d/(a+b))*f}')