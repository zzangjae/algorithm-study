import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):

    str_lst = list(input())
    stack = []
    stick = 0
    result = 0

    for char in str_lst:

        if char == '(':
            stick += 1
            stack.append(char)

        elif char == ')':
            stick -= 1

            if stack[-1] == '(':
                result += stick

            else:
                result += 1

            stack.append(char)

    print(f'#{test_case} {result}')

