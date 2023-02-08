import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    element_lst = list(input().split())
    stack = []
    result = 0

    for element in element_lst[:-1]:
        if element != '+' and element != '-' and element != '*' and element != '/' :
            stack.append(int(element))
        else:
            try:
                num2 = stack.pop()
                num1 = stack.pop()
            except:
                result = 'error'
                break

            if element == '+':
                stack.append(num1 + num2)
            elif element == '-':
                stack.append(num1 - num2)
            elif element == '*':
                stack.append(num1 * num2)
            elif element == '/':
                stack.append(int(num1 / num2))
            else:
                result = 'error'
                break

    if len(stack) == 1:
        result = stack[0]
    else:
        result = 'error'

    print(f'#{iteration + 1} {result}')
