import sys
sys.stdin = open('input.txt', 'r')


def get_max_price(idx=0):

    if idx >= n:
        return 0

    temp1 = consulting_lst[idx][1] + get_max_price(idx + consulting_lst[idx][0])\
    if idx + consulting_lst[idx][0] <= n else get_max_price(idx + consulting_lst[idx][0])

    temp2 = get_max_price(idx + 1)

    return max((temp1, temp2))


n = int(input())
consulting_lst = []

for _ in range(n):
    t, p = map(int, input().split())
    consulting_lst.append((t, p))

print(get_max_price())