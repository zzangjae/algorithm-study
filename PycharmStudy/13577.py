import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):

    card_dict = {}

    for card_num in range(9):
        card_dict[card_num] = 0

    card_lst = list(map(int, [card for card in input()]))

    for num in card_lst:
        card_dict[num] += 1

    triplet_num = 0
    run_num = 0

    for key in card_dict:
        if card_dict[key] >= 3:
            card_dict[key] -= 3
            triplet_num += 1

    for idx in range(0, 7):
        while card_dict[idx] and card_dict[idx+1] and card_dict[idx+2]:
            card_dict[idx] -= 1
            card_dict[idx+1] -= 1
            card_dict[idx+2] -= 1
            run_num += 1

    result = 1 if triplet_num == 2 or run_num == 2 or (triplet_num and run_num) else 0

    print(f'#{iteration+1} {result}')
