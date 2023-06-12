import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):

    n, char_lst = input().split()
    char_lst = list(char_lst)
    stack = []

    for char in char_lst:

        if len(stack) == 0:

            stack.append(char)

        elif stack[-1] == char:
            stack.pop()

        else:
            stack.append(char)

    print(f'#{test_case} {"".join(stack)}')