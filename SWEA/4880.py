import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def make_winner(i, j):

    if i == j:
        return i
    else:
        a_idx = make_winner(i, (i + j)//2)
        b_idx = make_winner((i + j)//2 + 1, j)
        a = card_lst[a_idx]
        b = card_lst[b_idx]

        if a == b:
            return a_idx
        elif a == 1 and b == 3 or\
            a == 2 and b == 1 or\
            a == 3 and b == 2:
            return a_idx
        else:
            return b_idx


for iteration in range(t):
    n = int(input())
    card_lst = list(map(int, input().split()))
    print(f'#{iteration + 1} {make_winner(0, n-1) + 1}')