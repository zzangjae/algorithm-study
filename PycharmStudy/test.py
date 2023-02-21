import sys
sys.stdin = open("input.txt", "r")

def check(arr):
    for i in range(n - 5 + 1):
        for j in range(n - 5 + 1):
            s = '' + arr[i][j] + arr[i+1][j+1] + arr[i+2][j+2] + arr[i+3][j+3] + arr[i+4][j+4]
            if s == "o" * 5:
                return True
    else: return False

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = [''.join(input()) for _ in range(n)]
    arr_ = [''.join(i) for i in zip(*arr)]
    ans = "NO"

    for s in arr + arr_:
        if 'o' * 5 in s:
            ans = "YES"
            break
    else:
        temp_arr = arr_[::-1]
        if check(arr) or check(arr_[::-1]):
            ans = "YES"
    print(f"#{t} {ans}")