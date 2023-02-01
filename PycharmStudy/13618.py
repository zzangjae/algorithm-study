import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):
    n = int(input())
    station_list = [0] * 5000

    for _ in range(n):
        a1, a2 = map(int, input().split())
        station_list[a1:a2+1] = [num+1 for num in station_list[a1:a2+1]]

    p = int(input())

    print(f'#{iteration+1}', end= ' ')
    for _ in range(p):
        print(station_list[int(input())], end = ' ')

