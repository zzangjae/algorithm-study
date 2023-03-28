import sys
sys.stdin = open('input.txt', 'r')

t = int(input())


def is_baby_gin(cards_lst):

    card_dict = {}

    for card_num in range(10):
        card_dict[card_num] = 0

    for num in cards_lst:
        card_dict[num] += 1

    triplet_num = 0
    run_num = 0

    for key in card_dict:
        if card_dict[key] >= 3:
            card_dict[key] -= 3
            triplet_num += 1

    for idx in range(0, 8):
        while card_dict[idx] and card_dict[idx+1] and card_dict[idx+2]:
            card_dict[idx] -= 1
            card_dict[idx+1] -= 1
            card_dict[idx+2] -= 1
            run_num += 1

    if triplet_num or run_num:
        return True

    return False


for tc_num in range(1, t+1):

    cards_lst = list(map(int, input().split()))
    result = 0

    for card_num in range(3, 7):

        player_1 = is_baby_gin(cards_lst[: card_num*2: 2])
        player_2 = is_baby_gin(cards_lst[1: card_num*2 - 2: 2])

        if player_1 and player_2:
            break

        elif player_1 and not player_2:
            result = 1
            break

        elif player_2 and not player_1:
            result = 2
            break

        player_2 = is_baby_gin(cards_lst[1: card_num * 2: 2])

        if player_1 and player_2:
            break

        elif player_1 and not player_2:
            result = 1
            break

        elif player_2 and not player_1:
            result = 2
            break

    print(f'#{tc_num} {result}')


