import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):

    char_lst = list(input())
    stack = []
    result = 0

    for char in char_lst:

        if char == '(':
            stack.append(char)

        elif char == ')' and len(stack) and stack[-1] == '(':
            stack.pop()

        elif char == ')':
            result = 0
            break

    else:
        if len(stack) == 0:
            result = 1

    print(f'#{test_case} {result}')