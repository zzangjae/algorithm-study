import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for iteration in range(t):
    num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5,
                'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    # for key in num_dict:
    #     num_dict[num_dict[key]] = key

    test_case, n = input().split()
    num_lst = list(input().split())

    print(f'#{iteration + 1}')
    for key in num_dict:
        print((key + ' ') * num_lst.count(key), end='')
    print()

