import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    str_lst = list(input())
    size = len(str_lst)

    for idx in range(size):
        if str_lst[idx] == 'b':
            str_lst[idx] = 'd'

        elif str_lst[idx] == 'd':
            str_lst[idx] = 'b'

        elif str_lst[idx] == 'p':
            str_lst[idx] = 'q'

        elif str_lst[idx] == 'q':
            str_lst[idx] = 'p'

    print(f'#{iteration + 1} ' + ''.join(str_lst[-1::-1]))

