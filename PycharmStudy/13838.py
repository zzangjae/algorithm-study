import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    equation_lst = list(input())
    stack = []
    result = []
    equation_lst.append('+')

    for token in equation_lst:

        if token == '*':

            if not stack:
                stack.append(token)

            elif stack[-1] == '+':
                stack.append(token)

            else:
                result.append(stack.pop())
                stack.append(token)

        elif token == '+':

            if not stack:
                stack.append(token)

            elif stack[-1] == '+':
                result.append(stack.pop())
                stack.append(token)

            else:
                while stack:
                    result.append(stack.pop())

                stack.append(token)

        else:
            result.append(token)

    print(f'#{test_case_num} {"".join(result)}')
