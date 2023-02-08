import sys

sys.stdin = open("input.txt", "r")

t = int(input())


def turn_90(lst):
    temp_lst = []

    for x in range(n):
        temp_lst2 = []
        for y in range(n):
            temp_lst2.append(lst[n-1-y][x])
        temp_lst.append(temp_lst2)

    return temp_lst


for iteration in range(t):
    n = int(input())
    num_lst = [list(map(int, input().split())) for _ in range(n)]
    num_90_lst = turn_90(num_lst)
    num_180_lst = turn_90(num_90_lst)
    num_270_lst = turn_90(num_180_lst)

    print(f'#{iteration + 1}')
    for row in range(n):
        print(''.join(map(str, num_90_lst[row])), end=' ')
        print(''.join(map(str, num_180_lst[row])), end=' ')
        print(''.join(map(str, num_270_lst[row])), end=' ')
        print()

