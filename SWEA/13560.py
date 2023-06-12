T = int(input())

for iteration in range(T):
    input()
    num_list = list(map(int, input().split()))
    print(f'#{iteration+1} {max(num_list)-min(num_list)}')

