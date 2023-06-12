import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):
    room_size = int(input())
    num_lst = list(map(int, input().split()))
    max_height = 0
    fall_dict = {}

    for idx in range(room_size):
        if num_lst[idx] > max_height:
            max_height = num_lst[idx]
            fall_dict[max_height] = room_size - idx\
            - len([num for num in num_lst if num >= max_height])

    print(f'#{iteration+1} {max(fall_dict.values())}')

