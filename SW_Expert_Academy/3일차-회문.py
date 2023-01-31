import math

def get_palindrome(text, check_size):
    text_size = len(text)

    for idx in range(text_size - check_size + 1):
        if text[idx : idx + check_size//2] ==\
            text[idx + check_size : idx + math.ceil(check_size/2) -1 : -1]:
            return ''.join(text[idx : idx + check_size])
    else:
        return False

t = int(input())

for iteration in range(t):
    text_size, check_size = map(int, input().split())

    text_list = [list(input()) for _ in range(text_size)]
    transposition_text_list = list(zip(*text_list))

    for idx in range(text_size):
        if get_palindrome(text_list[idx], check_size):
            print(f'#{iteration+1} {get_palindrome(text_list[idx], check_size)}')
            break
        elif get_palindrome(transposition_text_list[idx], check_size):
            print(f'#{iteration+1} {get_palindrome(transposition_text_list[idx], check_size)}')

