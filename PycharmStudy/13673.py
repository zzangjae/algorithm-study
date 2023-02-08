import sys
sys.stdin = open("input.txt", "r")

# t = int(input())

for iteration in range(10):
    t = int(input())
    num_lst = [list(map(int, input().split())) for _ in range(100)]
    rev_num_lst = list(zip(*num_lst))
    cross_sum = 0
    inv_cross_sum = 0
    result = 0

    for row in range(100):
        row_sum = sum(num_lst[row])
        column_sum = sum(rev_num_lst[row])

        if row_sum > result:
            result = row_sum

        if column_sum > result:
            result = column_sum

        cross_sum += num_lst[row][row]
        inv_cross_sum += num_lst[-1 * row - 1][row]

    if cross_sum > result:
        result = column_sum

    if inv_cross_sum > result:
        result = inv_cross_sum

    print(f'#{iteration + 1} {result}')



