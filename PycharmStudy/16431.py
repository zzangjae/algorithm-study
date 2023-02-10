import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    str_input = list(input())
    size = len(str_input)
    str_lst = []

    str_lst.append(list('..#.') * size + ['.'])
    str_lst.append(list('.#.#') * size + ['.'])
    str_lst.append(list('#...') * size + ['#'])
    str_lst.append(list('.#.#') * size + ['.'])
    str_lst.append(list('..#.') * size + ['.'])

    for idx in range(size):
        str_lst[2][idx * 4 + 2] = str_input[idx]

    for string in str_lst:
        print(''.join(string))

