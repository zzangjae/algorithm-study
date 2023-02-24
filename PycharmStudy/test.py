import sys
sys.stdin = open("input.txt", "r")
t = int(input())


def get_answer(lst):
    temp_lst = num_lst[:]

    for idx in range(len(temp_lst)):

        if temp_lst[idx] != lst[idx]:

            for temp_idx in range(len(temp_lst) - 1, -1, -1):
                if temp_lst[temp_idx] == lst[idx]:
                    temp_lst[idx], temp_lst[temp_idx] = temp_lst[temp_idx], temp_lst[idx]
                    break

            else:
                continue
            break

    return temp_lst


for test_case_num in range(1, t + 1):
    num_lst = list(map(int, list(input())))
    sorted_lst = num_lst[:]
    sorted_lst.sort()
    rev_sorted_lst = num_lst[:]
    rev_sorted_lst.sort(reverse=True)

    if not (num_lst.count(0) == len(num_lst)):

        counter = 0

        while sorted_lst[0] == 0:
            sorted_lst.pop(0)
            counter += 1

        for _ in range(counter):
            sorted_lst.insert(1, 0)

    print(f'#{test_case_num} {"".join(map(str, get_answer(sorted_lst)))} {"".join(map(str, get_answer(rev_sorted_lst)))}')


