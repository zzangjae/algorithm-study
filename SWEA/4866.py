import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    code_lst = list(input())
    stack = []
    result = 0

    for code_chr in code_lst:
        if code_chr == '{' or code_chr == '(':
            stack.append(code_chr)
        elif code_chr == '}' or code_chr == ')':
            if not stack:
                break
            temp_chr = stack.pop()
            if temp_chr == '{' and code_chr == '}':
                continue
            elif temp_chr == '(' and code_chr == ')':
                continue
            else:
                break
    else:
        if not stack:
            result = 1

    print(f'#{iteration + 1} {result}')


