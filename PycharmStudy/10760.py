import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def is_candidate_site(r, c, direction=0, checker=0):

    if direction == 8:
        if checker >= 4:
            return True
        else:
            return False

    temp_r = r + dr[direction]
    temp_c = c + dc[direction]

    if not (0 <= temp_r < n) or not (0 <= temp_c < m):
        return is_candidate_site(r, c, direction + 1, checker)

    elif num_lst[temp_r][temp_c] < num_lst[r][c]:
        return is_candidate_site(r, c, direction + 1, checker + 1)

    else:
        return is_candidate_site(r, c, direction + 1, checker)


for test_case_num in range(1, t + 1):
    n, m = map(int, input().split())
    num_lst = [list(map(int, input().split())) for _ in range(n)]
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]
    result = 0

    for row in range(n):
        for column in range(m):
            if is_candidate_site(row, column):
                result += 1

    print(f'#{test_case_num} {result}')


