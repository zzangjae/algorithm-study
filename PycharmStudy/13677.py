import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    n = int(input())
    num_lst = list(map(int, input().split()))
    num_lst.sort()
    temp_lst = []

    for idx in range(n):
        if idx % 2:
            temp_lst.append(num_lst[(idx // 2)])
        else:
            temp_lst.append(num_lst[(idx // 2 + 1) * - 1])

    print(f'#{iteration + 1} ' + ' '.join(map(str, temp_lst[:10])))
