test_case = int(input())

for iteration in range(test_case):
    n = int(input())
    num_list = list(map(int,list(input())))
    card_count = [0]*10

    for num in num_list:
        card_count[num] += 1

    max_count = 0
    max_num = 0
    for card_num in range(9,-1,-1):
        if card_count[card_num] > max_count:
            max_num = card_num
            max_count = card_count[card_num]

    print(f'#{iteration+1} {max_num} {max_count}')
