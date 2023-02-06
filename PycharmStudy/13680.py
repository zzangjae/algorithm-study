import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def find_space(puzzle_row, idx = 0, count = 0):

    if idx == n - 1:
        if count == k - 1 and puzzle_row[idx] == 1:
            return 1
        elif count == k and puzzle_row[idx] == 0:
            return 1
        return 0

    if count == k and puzzle_row[idx] == 0:
        return 1 + find_space(puzzle_row, idx + 1)

    if puzzle_row[idx] == 1:
        return find_space(puzzle_row, idx + 1, count + 1)
    else:
        return find_space(puzzle_row, idx + 1)


for iteration in range(T):
    n, k = map(int, input().split())
    puzzle_lst = [list(map(int, input().split())) for _ in range(n)]
    inv_puzzle_lst = list(zip(*puzzle_lst))
    result = 0

    for row in puzzle_lst:
        result += find_space(row)

    for column in inv_puzzle_lst:
        result += find_space(column)

    print(f'#{iteration+1} {result}')