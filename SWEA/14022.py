import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t+1):
    n = int(input())
    num_lst = list(map(int, input().split()))
    heap = [None] * (n + 1)

    for idx in range(1, n + 1):

        heap[idx] = num_lst[idx - 1]
        temp_idx = idx

        while temp_idx > 1:

            if heap[temp_idx // 2] > heap[temp_idx]:
                heap[temp_idx // 2], heap[temp_idx] = heap[temp_idx], heap[temp_idx // 2]
            else:
                break

            temp_idx = temp_idx // 2

    result = 0
    temp_idx = n

    while temp_idx > 1:
        temp_idx = temp_idx // 2
        result += heap[temp_idx]

    print(f'#{test_case_num} {result}')









