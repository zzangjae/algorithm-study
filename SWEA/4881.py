import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    n = int(input())
    num_lst = [list(map(int, input().split())) for _ in range(n)]
    stack = [[True] * n]
    answer = 1000

    while stack:

        checker = stack.pop()
        counter = 0
        for j in range(n):
            if checker[j] is True:
                counter += 1

        if not counter:
            temp_sum = sum(checker)
            answer = temp_sum if temp_sum < answer else answer
            continue

        for idx in range(n):

            if checker[idx] is True:
                temp_checker = checker[:]
                temp_checker[idx] = num_lst[n-counter][idx]
                stack.append(temp_checker)

    print(f'#{iteration + 1} {answer}')