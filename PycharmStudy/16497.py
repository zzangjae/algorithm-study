import sys
sys.stdin = open("input.txt", "r")

for test_case_num in range(10):
    n = int(input())
    str_lst = list(input())
    result = 0
    postfix_equation_lst = []
    stack = []

    for idx in range(n):

        if str_lst[idx] == '+':

            if not stack:
                stack.append('+')

            else:
                postfix_equation_lst.append(stack.pop())
                stack.append('+')

        else:
            postfix_equation_lst.append(str_lst[idx])

    else:
        while stack:
            postfix_equation_lst.append(stack.pop())

    for token in postfix_equation_lst:

        if token == '+':
            num2, num1 = int(stack.pop()), int(stack.pop())
            stack.append(num1 + num2)

        else:
            stack.append(token)

    if len(stack) == 1:
        result = stack[0]

    print(f'#{test_case_num + 1} {result}')


