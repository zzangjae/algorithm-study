import sys
sys.stdin = open("input.txt", "r")

for test_case_num in range(1, 11):
    n = int(input())
    str_lst = list(input())
    operation_dict = {'+': 1, '*': 2}
    stack = []
    result = []

    for token in str_lst:

        if token in operation_dict:

            if not stack:
                stack.append(token)

            elif operation_dict[stack[-1]] < operation_dict[token]:
                stack.append(token)

            else:
                while stack and operation_dict[stack[-1]] >= operation_dict[token]:
                    result.append(stack.pop())
                stack.append(token)

        else:
            result.append(token)

    while stack:
        result.append(stack.pop())

    for token in result:

        if token in operation_dict:

            num2, num1 = stack.pop(), stack.pop()

            if token == '+':
                stack.append(int(num1) + int(num2))

            elif token == '*':
                stack.append(int(num1) * int(num2))

        else:
            stack.append(token)

    print(f'#{test_case_num} {stack[0]}')





