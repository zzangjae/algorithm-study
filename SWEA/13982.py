import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case_num in range(1, t + 1):
    n, m = map(int, input().split())
    cheese_lst = list(map(int, input().split()))
    cheese_lst = list(map(list, enumerate(cheese_lst)))
    stove_que, cheese_lst = cheese_lst[:n], cheese_lst[n:]
    idx = 0
    result = 0

    while True:

        if len(stove_que) == 1:
            result = stove_que[0][0]
            break

        elif stove_que[idx][1]:
            stove_que[idx][1] = stove_que[idx][1] // 2
            idx = (idx + 1) % n

        else:
            stove_que.pop(idx)

            if cheese_lst:
                stove_que.insert(idx, cheese_lst.pop(0))

            else:
                n -= 1
                idx = (idx) % n

    print(f'#{test_case_num} {result + 1}')




