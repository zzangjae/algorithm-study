import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):
    n = int(input())
    station_lst = [0] * 1001

    for _ in range(n):

        t, a, b = map(int, input().split())

        if t == 1:
            station_lst[a:b+1] = [i+1 for i in station_lst[a: b+1]]

        elif t == 2:
            if a % 2:
                station_lst[a:b+1] = \
                    [station_lst[idx] + int(idx % 2 or idx == a or idx == b) for idx in range(a, b+1)]
            else:
                station_lst[a:b + 1] = \
                    [station_lst[idx] + int(idx % 2 == 0 or idx == a or idx == b) for idx in range(a, b + 1)]

        elif t == 3:
            if a % 2:
                station_lst[a:b + 1] = \
                    [station_lst[idx] + int((idx % 3 == 0 and idx % 10 != 0) or idx == a or idx == b)for idx in range(a, b + 1)]
            else:
                station_lst[a:b + 1] = \
                    [station_lst[idx] + int(idx % 4 == 0 or idx == a or idx == b) for idx in range(a, b + 1)]

    print(f'#{iteration+1} {max(station_lst)}')


