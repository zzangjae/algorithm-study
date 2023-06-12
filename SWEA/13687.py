import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    n = int(input())
    room_dict = {}
    result = 0

    for _ in range(n):
        start_room, end_room = map(int, input().split())
        room_dict[start_room] = end_room

    room_keys = list(room_dict.keys())
    room_keys.sort()

    while room_keys:

        result += 1
        room_checker = 0
        remover = []

        for key in room_keys:

            if key // 2 + key % 2 > room_checker and\
                    room_dict[key] // 2 + room_dict[key] % 2 > room_checker:
                room_checker = room_dict[key] // 2 + room_dict[key] % 2
                remover.append(key)

        for key in remover:
            room_keys.remove(key)

    print(f'#{test_case_num} {result}')





