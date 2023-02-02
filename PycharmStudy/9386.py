import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):
    n = int(input())

    num_list = list((input().split('0')))

    print(f'{iteration+1} {len(max(num_list))}')
