import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1,T+1):
    # max index min index
    N = int(input())
    arr = [list(map(str , input())) for _ in range(N)]
    proof_lst = []
    mx_0, mx_1, mn_0,mn_1, cnt = 0,0,20,20, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                if i > mx_0:
                    mx_0 = i
                if i < mn_0:
                    mn_0 = i
                if j > mx_1:
                    mx_1 = j
                if j < mn_1:
                    mn_1 = j
                cnt+=1
    if mx_1 == mx_0 and mn_0 == mn_1:
        if (mx_1-mn_1+1)*(mx_0-mn_0+1) == cnt:
            result = 'yes'
        else:
            result = 'no'
    else:
        result = 'no'
    print(f'#{test_case} {result}')