import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def quick_sort(num_list):

    if len(num_list) < 2:
        return num_list

    else:
        pivot = num_list[-1]
        left_list = []
        right_list = []

        for num in num_list[:-1]:
            if pivot > num:
                left_list.append(num)
            else:
                right_list.append(num)

        return quick_sort(left_list) + [pivot] + quick_sort(right_list)


for test_case_num in range(1, t + 1):
    n = int(input())
    num_lst = list(map(int, input().split()))
    num_lst = quick_sort(num_lst)
    print(f'#{test_case_num} {num_lst[n//2]}')
