import sys
sys.stdin = open("input.txt", "r")

T = 10

for iteration in range(T):

    n = int(input())
    building_lst = list(map(int, input().split()))

    sum = 0

    for idx in range(2, n-2):
        tallest = max([building_lst[i] for i in [idx-2, idx-1, idx+1, idx+2]])
        sum += building_lst[idx] - tallest if building_lst[idx] - tallest > 0 else 0

    print(f'#{iteration+1} {sum}')



