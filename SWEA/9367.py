import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for iteration in range(T):

    n = int(input())
    carrot_lst = list(map(int, input().split()))
    result = 1
    count = 1

    for idx in range(n-1):
        if carrot_lst[idx] < carrot_lst[idx+1]:
            count += 1
        else:
            if count > result:
                result = count
                count = 1
            else:
                count = 1
    else:
        if count > result:
            result = count

    print(f'#{iteration+1} {result}')


