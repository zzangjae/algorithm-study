import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):

    equation_lst = list(input().split())
    stack = []
    result = 'error'

    for token in equation_lst[:-1]:

        if token == '-' or token == '+' or token == '*' or token == '/':

            try:
                num2, num1 = int(stack.pop()), int(stack.pop())

                if token == '-': stack.append(num1 - num2)
                elif token == '+': stack.append(num1 + num2)
                elif token == '*': stack.append(num1 * num2)
                elif token == '/': stack.append(num1 // num2)

            except:
                break

        else:
            stack.append(token)

    else:
        if len(stack) == 1:
            result = stack[0]

    print(f'#{test_case_num} {result}')

