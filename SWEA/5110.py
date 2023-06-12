import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t+1):
    n, m = map(int, input().split())
    result = list(map(int, input().split()))

    for i in range(m - 1):
        temp_lst = list(map(int, input().split()))

        for idx in range((i + 1) * 4 ):

            if result[idx] > temp_lst[0]:
                result = result[:idx] + temp_lst + result[idx:]
                break

        else:
            result = result + temp_lst

    if n * m >= 10:
        print(f'#{test_case_num} {" ".join(map(str, result[:-11:-1]))}')
    else:
        print(f'#{test_case_num} {" ".join(map(str, result[::-1]))}')













