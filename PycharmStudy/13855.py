import sys
sys.stdin = open("input.txt", "r")

for test_case_num in range(1, 11):
    n = int(input())
    str_lst = list(input())
    in_coming_priority = {'+': 1, '*': 2, '(' : 3, ')' : -1}
    in_stack_priority = {'+': 1, '*': 2, '(': 0}
    stack = []
    result = []

    for token in str_lst:

        if token in in_coming_priority:

            if not stack:
                stack.append(token)

            elif in_stack_priority[stack[-1]] < in_coming_priority[token]:
                stack.append(token)

            elif token == ')':
                while True:
                    temp_top = stack.pop()
                    if temp_top == '(':
                        break
                    else:
                        result.append(temp_top)

            else:
                while stack and in_stack_priority[stack[-1]] >= in_coming_priority[token]:
                    result.append(stack.pop())
                stack.append(token)

        else:
            result.append(token)

    while stack:
        result.append(stack.pop())

    for token in result:

        if token in in_coming_priority:

            num2, num1 = stack.pop(), stack.pop()

            if token == '+':
                stack.append(int(num1) + int(num2))

            elif token == '*':
                stack.append(int(num1) * int(num2))

        else:
            stack.append(token)

    print(f'#{test_case_num} {stack[0]}')





