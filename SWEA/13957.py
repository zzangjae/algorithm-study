import sys
sys.stdin = open("input.txt", "r")

for test_case_num in range(1, 11):
    t = int(input())
    password_que = list(map(int, input().split()))
    idx = 0
    count = 1

    while True:

        password_que[idx] -= count
        count = (count + 1) if count < 5 else 1

        if password_que[idx] <= 0:
            password_que[idx] = 0
            break
        else:
            idx = (idx + 1) % 8

    for idx in range(8):
        if password_que[idx] == 0:
            zero_start = idx

    password_que = password_que[zero_start:] + password_que[:zero_start] + [0]

    print(f'#{test_case_num} {" ".join(map(str, password_que[1:]))}')



