gear_dict = {}

for gear_num in range(1, 5):
    gear_dict[gear_num] = input()

k = int(input())

for _ in range(k):
    gear_num, rotation_d = map(int, input().split())
    stack = [(gear_num, rotation_d)]
    checker = [True] * 5
    turn_num = []

    while stack:

        g, r = stack.pop()
        checker[g] = False

        if g-1 > 0 and gear_dict[g-1][2] != gear_dict[g][6] and checker[g-1]:
            stack.append((g-1, r*-1))

        if g+1 <= 4 and gear_dict[g+1][6] != gear_dict[g][2] and checker[g+1]:
            stack.append((g+1, r*-1))

        turn_num.append((g, r))

    for g, r in turn_num:
        if r == 1:
            gear_dict[g] = gear_dict[g][7] + gear_dict[g][:7]

        else:
            gear_dict[g] = gear_dict[g][1:] + gear_dict[g][0]

result = 0

for i in range(1, 5):
    result += (2 ** (i-1)) * int(gear_dict[i][0])

print(result)
