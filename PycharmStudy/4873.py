import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):

    str_lst = list(input())
    stack = []
    temp_char = ''

    for char in str_lst:
        if temp_char == char and stack:
            stack.pop()
            temp_char = stack[-1] if stack else ''
        else:
            stack.append(char)
            temp_char = char

    print(f'#{iteration + 1} {len(stack)}')


