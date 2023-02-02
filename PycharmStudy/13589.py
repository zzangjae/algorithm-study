import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):

    n = int(input())
    card_lst = list(map(int, list(input())))
    card_dict = {}

    for card_num in card_lst:
        if card_num not in card_dict:
            card_dict[card_num] = 1
        else:
            card_dict[card_num] += 1

    max_card = 0
    max_key = 0

    for key in card_dict:
        if max_card <= card_dict[key] and max_key < key:
            max_key = key
            max_card = card_dict[key]

    print(f'#{iteration+1} {max_key} {max_card}')
