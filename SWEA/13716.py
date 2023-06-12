import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    str1, str2 = input(), input()
    char_dict = {}
    for char in str1:
        char_dict[char] = 0

    for char in str2:
        if char in char_dict:
            char_dict[char] += 1

    print(f'#{iteration + 1} {max(char_dict.values())}')