import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):

    char_lst = list(input())
    stack = []

    for char in char_lst:

        if len(stack) == 0:

            stack.append(char)

        elif stack[-1] == char:
            stack.pop()

        else:
            stack.append(char)

    print(f'#{test_case} {len(stack)}')