import sys
sys.stdin = open("input.txt", "r")

T = 10

for iteration in range(T):

    dump_num = int(input())
    box_lst = list(map(int, input().split()))
    max_height = 0
    min_height = 100
    height_dict = {}

    for box_height in box_lst:
        if box_height not in height_dict:
            height_dict[box_height] = 1
        else:
            height_dict[box_height] += 1

        if max_height < box_height:
            max_height = box_height

        if min_height > box_height:
            min_height = box_height

    while dump_num > 0:
        if max_height - min_height <= 1:
            break

        height_dict[max_height] -= 1

        if max_height - 1 not in height_dict:
            height_dict[max_height - 1] = 1
        else:
            height_dict[max_height - 1] += 1

        height_dict[min_height] -= 1

        if min_height + 1 not in height_dict:
            height_dict[min_height + 1] = 1
        else:
            height_dict[min_height + 1] += 1

        dump_num -= 1

        if height_dict[max_height] == 0:
            max_height -= 1

        if height_dict[min_height] == 0:
            min_height += 1

    print(f'#{iteration+1} {max_height-min_height}')




