import sys
sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
room_lst = [[0, 0] for _ in range(6)]
result = 0

for _ in range(n):

    s, y = map(int, input().split())
    room_lst[y - 1][s] += 1

for room1, room2 in room_lst:
    result += 0 if not room1 else (room1 - 1) // k + 1
    result += 0 if not room2 else (room2 - 1) // k + 1

print(result)
