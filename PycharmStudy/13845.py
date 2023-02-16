import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_winner(i, j):

    if j - i == 0:
        return i

    else:
        num1_idx, num2_idx = get_winner(i, (i + j) // 2),\
                     get_winner((i + j)//2 + 1, j)

        if card_lst[num1_idx] == card_lst[num2_idx]:
            return num1_idx

        elif (card_lst[num1_idx] == 1 and card_lst[num2_idx] == 3) or\
                (card_lst[num1_idx] == 2 and card_lst[num2_idx] == 1)or\
                (card_lst[num1_idx] == 3 and card_lst[num2_idx] == 2):
            return num1_idx

        else:
            return num2_idx


for test_case_num in range(1, t + 1):
    n = int(input())
    card_lst = list(map(int, input().split()))
    print(f'#{test_case_num} {get_winner(0, n-1) + 1}')

