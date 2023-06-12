import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def get_home_num(start_r, start_c):
    temp_dict = {}
    result = []

    for r, c in home_lst:
        temp_distance = abs(start_r - r) + abs(start_c - c)

        if temp_distance not in temp_dict:
            temp_dict[temp_distance] = 1

        else:
            temp_dict[temp_distance] += 1

    for k in range(1, 22):
        temp_sum = 0

        for num in range(0, k):
            if num in temp_dict:
                temp_sum += temp_dict[num]

        if temp_sum * m >= k_lst[k - 1]:
            result.append(temp_sum)

    return max(result) if len(result) > 0 else 0


for test_case_num in range(1, t + 1):
    n, m = map(int, input().split())
    map_lst = [list(map(int, input().split())) for _ in range(n)]
    k_lst = [k * k + (k - 1) * (k - 1) for k in range(1, 22)]
    home_lst = []
    result = []

    for i in range(n):
        for j in range(n):
            if map_lst[i][j] == 1:
                home_lst.append((i, j))

    for row in range(n):
        for column in range(n):
            result.append(get_home_num(row, column))

    print(f'#{test_case_num} {max(result)}')



