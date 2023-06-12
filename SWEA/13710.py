import sys
sys.stdin = open("input.txt", "r")

for iteration in range(10):
    input()
    str1 = input()
    str2 = input()

    print(f'#{iteration + 1} {str2.count(str1)}')